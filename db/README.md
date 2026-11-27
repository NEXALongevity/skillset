# Knowledge-base database

The YAML files under `data/` remain the open-source source of truth. This folder loads them into a
PostgreSQL database (Supabase) so the MCP server and internal tools can query doctors and hospitals live.

## Three layers, kept apart

| Layer | What | Where | Who can read |
|---|---|---|---|
| Public (`kb` schema) | Hospitals, rankings, published doctor profiles, sources | This database, schema in this repo | Anyone (published rows only) |
| Internal | Partnerships, contacts, commercial terms, internal notes | Same database, separate schema, **not in this public repo** | NEXA staff only |
| Patient | Records, consultations, consent | NEXA Care, never this database | Care team, under PIPL / PDPO / GDPR rules |

The MCP server only ever reads the public layer. When a user asks to be connected to NEXA,
the MCP hands a lead to NEXA Care with the user's explicit consent; it does not store it here.

## Load

```bash
psql "$DATABASE_URL" -f db/migrations/0001_public_kb.sql   # once
python db/seed.py > db/seed.sql && psql "$DATABASE_URL" -f db/seed.sql   # after each data change (idempotent)
```

Rules carried over from the data files: every record cites a source and a verified date; doctors
are stored as `draft` until a licence check against the NHC registry is done, and only `published`
rows are visible to the public. No licence numbers, phone numbers of individuals or patient data.
