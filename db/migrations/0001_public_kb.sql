-- NEXA Medical Travel knowledge base — PUBLIC layer (open data, CC BY 4.0)
-- Target: PostgreSQL 15+ (Supabase). Holds only information that is already public
-- (rankings, licences, departments, published doctor profiles). No patient data, ever.
-- Internal/commercial data and patient data live elsewhere; see db/README.md.

create schema if not exists kb;

create type kb.direction as enum (
  'oncology','cardio-cerebrovascular','reproductive','checkup-longevity','tcm','orthopedics','aesthetics');
create type kb.facility_type as enum ('public','private','foreign');
create type kb.record_status as enum ('draft','published','retired');

-- Every fact traces to a source.
create table kb.sources (
  id          bigint generated always as identity primary key,
  title       text not null,              -- e.g. 复旦大学医院管理研究所《2023年度中国医院专科声誉排行榜》
  url         text,
  publisher   text,
  published_on date,
  unique (title, url)
);

create table kb.hospitals (
  id            text primary key check (id ~ '^[a-z0-9-]+$'),
  name_zh       text not null,
  name_en       text not null,
  type          kb.facility_type not null,
  grade         text,                     -- 三级甲等 / Grade 3A
  city          text not null,
  province      text not null,
  website       text,
  intl_dept_name  text,
  intl_dept_phone text,
  intl_dept_url   text,
  strengths     text[] not null default '{}',
  notes         text,
  status        kb.record_status not null default 'published',
  verified_on   date not null,
  updated_at    timestamptz not null default now()
);

create table kb.hospital_directions (
  hospital_id text references kb.hospitals(id) on delete cascade,
  direction   kb.direction,
  primary key (hospital_id, direction)
);

create table kb.hospital_rankings (
  id          bigint generated always as identity primary key,
  hospital_id text not null references kb.hospitals(id) on delete cascade,
  source_id   bigint not null references kb.sources(id),
  list_name   text not null,
  year        int not null,
  specialty   text not null,
  rank        int,
  unique (hospital_id, source_id, specialty)
);

-- Doctors: only what is published by the hospital / official registry.
create table kb.doctors (
  id            text primary key check (id ~ '^[a-z0-9-]+$'),
  name_zh       text not null,
  name_en       text,
  title         text,                     -- 主任医师 / Chief Physician
  academic_title text,                    -- 教授 / Professor
  specialties   text[] not null default '{}',
  languages     text[] not null default '{}',
  bio_zh        text,
  bio_en        text,
  profile_url   text,                     -- official hospital profile page
  licence_checked_on date,                -- last NHC registry check (no licence number stored)
  status        kb.record_status not null default 'draft',
  verified_on   date not null,
  source_id     bigint references kb.sources(id),
  updated_at    timestamptz not null default now()
);

create table kb.doctor_directions (
  doctor_id text references kb.doctors(id) on delete cascade,
  direction kb.direction,
  primary key (doctor_id, direction)
);

create table kb.doctor_affiliations (
  doctor_id   text references kb.doctors(id) on delete cascade,
  hospital_id text references kb.hospitals(id) on delete cascade,
  department  text,
  is_primary  boolean not null default true,
  primary key (doctor_id, hospital_id)
);

create index on kb.hospitals (city);
create index on kb.hospital_directions (direction);
create index on kb.doctor_directions (direction);
create index on kb.doctor_affiliations (hospital_id);

-- updated_at trigger
create or replace function kb.touch() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
create trigger hospitals_touch before update on kb.hospitals for each row execute function kb.touch();
create trigger doctors_touch   before update on kb.doctors   for each row execute function kb.touch();

-- Read access: anyone may read PUBLISHED rows (this is open data). Writes: editors only (service role / authenticated editors).
alter table kb.sources              enable row level security;
alter table kb.hospitals            enable row level security;
alter table kb.hospital_directions  enable row level security;
alter table kb.hospital_rankings    enable row level security;
alter table kb.doctors              enable row level security;
alter table kb.doctor_directions    enable row level security;
alter table kb.doctor_affiliations  enable row level security;

create policy read_sources   on kb.sources             for select using (true);
create policy read_hospitals on kb.hospitals           for select using (status = 'published');
create policy read_hdir      on kb.hospital_directions for select using (exists (select 1 from kb.hospitals h where h.id = hospital_id and h.status = 'published'));
create policy read_hrank     on kb.hospital_rankings   for select using (exists (select 1 from kb.hospitals h where h.id = hospital_id and h.status = 'published'));
create policy read_doctors   on kb.doctors             for select using (status = 'published');
create policy read_ddir      on kb.doctor_directions   for select using (exists (select 1 from kb.doctors d where d.id = doctor_id and d.status = 'published'));
create policy read_daff      on kb.doctor_affiliations for select using (exists (select 1 from kb.doctors d where d.id = doctor_id and d.status = 'published'));

grant usage on schema kb to anon, authenticated;
grant select on all tables in schema kb to anon, authenticated;
