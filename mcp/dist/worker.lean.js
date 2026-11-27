const SERVER = { name: "nexa-medical-travel", version: "0.3.0" };
const PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"];
const DISCLAIMER =
"Information only, not medical, legal or immigration advice. Verify with the official source before acting. 仅供参考，以官方与执业医生意见为准。";
const SITE = "https://skills.nxlongevity.com";
const TERMS_URL = "https://github.com/NEXALongevity/skillset/blob/main/mcp/TERMS.md";
const CARE_ORIGIN = "https://care.nxlongevity.com";
let ENV = {};
const careCache = new Map();
async function careGet(path, params) {
const base = ENV.CARE_MCP_BASE;
if (!base) return null;
const u = new URL(base.replace(/\/+$/, "") + path);
for (const [k, v] of Object.entries(params || {})) if (v !== undefined && v !== null && v !== "") u.searchParams.set(k, String(v));
const key = u.toString();
const hit = careCache.get(key);
if (hit && Date.now() - hit.at < 300000) return hit.body;
try {
const r = await fetch(key, { headers: { Accept: "application/json", "X-NEXA-Client": "nexa-mcp/" + SERVER.version }, cf: { cacheTtl: 300 } });
if (!r.ok) return { error: "care_unavailable", status: r.status };
const body = await r.json();
careCache.set(key, { at: Date.now(), body });
return body;
} catch (e) { return { error: "care_unavailable" }; }
}
const DATA_URL = "https://raw.githubusercontent.com/NEXALongevity/skillset/main/mcp/dist/data.json";
let DATA = globalThis.__NEXA_DATA || null;
let loadedAt = 0;
async function ensureData() {
if (globalThis.__NEXA_DATA) return;
if (DATA && Date.now() - loadedAt < 600000) return;
const r = await fetch(DATA_URL, { cf: { cacheTtl: 600, cacheEverything: true } });
if (!r.ok) { if (DATA) return; throw new Error("data unavailable: " + r.status); }
DATA = await r.json(); loadedAt = Date.now();
}
const norm = (s) => String(s || "").trim().toLowerCase().replace(/[\s._-]+/g, " ");
const daysBetween = (a, b) => Math.round((Date.parse(b) - Date.parse(a)) / 86400000);
const addDays = (d, n) => new Date(Date.parse(d) + n * 86400000).toISOString().slice(0, 10);
const round2 = (n) => Math.round(n * 100) / 100;
function resolveCountry(input) {
const v = DATA.visa;
const raw = String(input || "").trim();
if (!raw) return null;
if (v.aliases[raw]) return v.aliases[raw];
const n = norm(raw);
for (const [k, val] of Object.entries(v.aliases)) if (norm(k) === n) return val;
const all = [...v.unilateral_visa_free, ...v.mutual_exemption_ordinary].map((e) => e.country)
.concat(Object.keys(v.regional));
return all.find((c) => norm(c) === n) || raw;
}
const src = (id) => ({ id, ...DATA.visa.sources[id] });
function visaEntryOptions(a) {
const v = DATA.visa;
const country = resolveCountry(a.nationality);
if (!country) throw new Error("nationality is required");
const passport = norm(a.passport_type || "ordinary");
const stay = Number(a.stay_days || 0);
const entry = a.entry_date || null;
const exit = entry && stay ? addDays(entry, stay) : null;
const purpose = norm(a.purpose || "medical");
const medical = /medic|treat|surg|hospital|就医|治疗|手术|住院|体检|check|exam/.test(purpose);
const options = [], risks = [], ask = [];
if (v.regional[country]) {
return { nationality: country, as_of: v.as_of, summary: v.regional[country], options: [], risks: [], ask_embassy: [], sources: [], disclaimer: DISCLAIMER };
}
if (passport !== "ordinary") {
ask.push("Diplomatic, service and official passports follow separate agreements: check the MFA Mutual Visa Exemption List and confirm with the embassy.");
}
const uni = v.unilateral_visa_free.find((e) => e.country === country);
if (uni && passport === "ordinary") {
const o = { route: "Unilateral visa-free entry 单方面免签", may_apply: true, max_days: uni.max_days, valid_from: uni.valid_from || null, valid_until: uni.valid_until, listed_purposes: uni.purposes, medical_listed: false, source: src(uni.source) };
if (stay > uni.max_days) { o.may_apply = false; o.reason = `Stay of ${stay} days exceeds ${uni.max_days}-day limit`; }
if (entry && uni.valid_from && entry < uni.valid_from) { o.may_apply = false; o.reason = `Policy starts ${uni.valid_from}`; }
if (entry && entry > uni.valid_until) { o.may_apply = false; o.reason = `Policy currently published only until ${uni.valid_until}`; }
if (exit && exit > uni.valid_until && entry <= uni.valid_until) risks.push(`Planned exit ${exit} is after the published end date ${uni.valid_until}. Re-check before travel; the policy may or may not be extended.`);
options.push(o);
}
const mut = v.mutual_exemption_ordinary.find((e) => e.country === country);
if (mut && passport === "ordinary") {
const o = { route: "Mutual visa exemption agreement 互免签证协定", may_apply: stay < 30 || !stay, in_force_since: mut.in_force_since, max_days: "less than 30 days per entry (official note)", medical_listed: false, source: src(mut.source) };
if (stay >= 30) o.reason = `Stay of ${stay} days is not less than 30 days`;
if (mut.note) o.note = mut.note;
options.push(o);
}
if (a.onward_ticket) {
options.push({ route: "240-hour visa-free transit 240 小时过境免签", may_apply: stay <= 10 ? "check nationality list" : false, conditions: v.transit_240h.conditions, activities: v.transit_240h.activities, eligible_countries: v.transit_240h.countries_count, ports: v.transit_240h.ports_count, nationality_list_bundled: false, reason: stay > 10 ? "Stay longer than 240 hours" : undefined, source: src(v.transit_240h.source) });
}
if (/hainan|海南/.test(norm(a.destination_province))) {
options.push({ route: "Hainan 30-day visa-free entry 海南 30 天免签", may_apply: stay <= 30 ? "check nationality list" : false, conditions: v.hainan_30d.conditions, eligible_countries: v.hainan_30d.countries_count, nationality_list_bundled: false, source: src(v.hainan_30d.source) });
}
options.push({ route: "Apply for a visa 申请签证", may_apply: true, note: "Always available. Ask the Chinese embassy or consulate (or the official visa application service centre) which category fits medical treatment and what hospital documents are needed." });
if (!uni && !mut && country !== "China") {
risks.push(`${country} is not in this dataset's visa-free lists (as of ${v.as_of}). Treat a visa as required unless the official sources say otherwise.`);
}
if (medical && options.some((o) => o.medical_listed === false && o.may_apply === true)) {
risks.push(v.medical_purpose_note);
ask.push("Does visa-free entry cover outpatient visits, check-ups, admission or surgery for this traveller?");
}
if (stay > 25) risks.push("Long stays leave little buffer for complications or delayed discharge; a visa usually gives more room.");
const viable = options.filter((o) => o.may_apply === true && o.route.indexOf("Apply") !== 0);
let summary;
if (!viable.length) summary = "Apply for a visa.";
else if (medical) summary = `${viable.map((o) => o.route).join(" / ")} may apply by nationality and length of stay, but medical treatment is not a listed purpose. Confirm with the embassy, or apply for a visa (safest for admission or surgery).`;
else summary = `${viable.map((o) => o.route).join(" / ")} may apply. Verify before booking.`;
return { nationality: country, passport_type: passport, stay_days: stay || null, entry_date: entry, estimated_exit: exit, as_of: v.as_of, summary, options, risks, ask_embassy: ask, sources_checked: Object.keys(v.sources).map(src), next: "Hand over to the visa-itinerary Skill for documents and day-by-day plan: " + SITE + "/skills/visa-itinerary.html", disclaimer: DISCLAIMER };
}
function visaPolicySources() {
const v = DATA.visa;
return { as_of: v.as_of, dataset: v.dataset, sources: Object.keys(v.sources).map(src), unilateral_countries: v.unilateral_visa_free.map((e) => e.country), mutual_exemption_ordinary_countries: v.mutual_exemption_ordinary.map((e) => e.country), not_bundled: ["240-hour transit nationality list (57)", "Hainan 30-day nationality list (61)"], disclaimer: DISCLAIMER };
}
function costChecklist(a) {
const c = DATA.costs;
const dir = norm(a.direction).replace(/ /g, "-");
const items = c.directions[dir];
if (!items) throw new Error(`Unknown direction. Use one of: ${Object.keys(c.directions).join(", ")}`);
return { direction: dir, as_of: c.as_of, medical_items: items, travel_items: c.common.travel, service_items: c.common.service, note: c.note };
}
function costEstimate(a) {
const items = Array.isArray(a.items) ? a.items : [];
if (!items.length) throw new Error("items is required: [{category, name, amount | amount_min+amount_max, currency, source}]");
const pct = a.contingency_pct === undefined ? 15 : Number(a.contingency_pct);
const fx = a.fx; // {from, to, rate, date}
const byCur = {}, pending = [], unsourced = [];
for (const it of items) {
const lo = it.amount_min ?? it.amount, hi = it.amount_max ?? it.amount;
if (lo === undefined || lo === null || lo === "") { pending.push(it.name); continue; }
const cur = (it.currency || "CNY").toUpperCase();
const cat = ["medical", "travel", "service"].includes(it.category) ? it.category : "other";
byCur[cur] ??= { medical: [0, 0], travel: [0, 0], service: [0, 0], other: [0, 0] };
byCur[cur][cat][0] += Number(lo); byCur[cur][cat][1] += Number(hi);
if (!it.source) unsourced.push(it.name);
}
const totals = {};
for (const [cur, cats] of Object.entries(byCur)) {
const low = Object.values(cats).reduce((s, x) => s + x[0], 0);
const highBase = Object.values(cats).reduce((s, x) => s + x[1], 0);
totals[cur] = { subtotals: Object.fromEntries(Object.entries(cats).filter(([, x]) => x[1]).map(([k, x]) => [k, { low: round2(x[0]), high: round2(x[1]) }])), low: round2(low), high: round2(highBase * (1 + pct / 100)) };
}
let converted = null;
if (fx && fx.from && fx.to && fx.rate) {
const F = fx.from.toUpperCase(), T = fx.to.toUpperCase(), r = Number(fx.rate);
const t = { low: 0, high: 0 };
for (const [cur, x] of Object.entries(totals)) {
if (cur === T) { t.low += x.low; t.high += x.high; }
else if (cur === F) { t.low += x.low * r; t.high += x.high * r; }
else { t.unconverted = (t.unconverted || []).concat(cur); }
}
converted = { currency: T, low: round2(t.low), high: round2(t.high), rate: `1 ${F} = ${r} ${T}`, rate_date: fx.date || "not given", rate_source: "user-supplied", unconverted: t.unconverted };
}
let missing = [];
if (a.direction) {
try {
const names = items.map((i) => norm(i.name));
missing = costChecklist({ direction: a.direction }).medical_items.filter((m) => !names.some((n) => n && (norm(m).includes(n) || n.includes(norm(m).split(" ")[0]))));
} catch (_) {}
}
return { method: `low = sum of minimums; high = sum of maximums × (1 + ${pct}% contingency)`, totals_by_currency: totals, converted, pending_quote: pending, without_source: unsourced, checklist_items_not_in_quote: missing, stay_days: a.stay_days || null, notes: ["All amounts were supplied by the user or a written quote; this tool holds no price data.", "Final charges are settled by the hospital; deposits are refunded or topped up at discharge."], disclaimer: DISCLAIMER };
}
function compareQuotes(a) {
const quotes = Array.isArray(a.quotes) ? a.quotes : [];
if (quotes.length < 2) throw new Error("quotes needs at least two entries: [{label, currency, items:[{name, amount, included?}]}]");
const rows = new Map();
quotes.forEach((q, qi) => (q.items || []).forEach((it) => {
const key = norm(it.name);
if (!rows.has(key)) rows.set(key, { item: it.name, values: Array(quotes.length).fill(null) });
rows.get(key).values[qi] = it.amount ?? (it.included ? "included" : "listed, no amount");
}));
const table = [...rows.values()];
const gaps = quotes.map((q, qi) => ({ quote: q.label, missing_items: table.filter((r) => r.values[qi] === null).map((r) => r.item) }));
const totals = quotes.map((q) => ({ quote: q.label, currency: q.currency || "CNY", listed_total: round2((q.items || []).reduce((s, i) => s + (typeof i.amount === "number" ? i.amount : 0), 0)) }));
let not_in_any = [];
if (a.direction) {
try { not_in_any = costChecklist({ direction: a.direction }).medical_items.filter((m) => !table.some((r) => norm(m).includes(norm(r.item)) || norm(r.item).includes(norm(m).split(" ")[0]))); } catch (_) {}
}
return { table, gaps, listed_totals: totals, checklist_items_not_in_any_quote: not_in_any, caution: "Totals are only comparable when scopes match. Ask each provider to quote the missing items before comparing.", disclaimer: DISCLAIMER };
}
function credentialLookup(a) {
const q = norm(a.name);
if (!q) throw new Error("name is required");
const hits = DATA.hospitals.filter((h) => norm(h.name_zh).includes(q) || norm(h.name_en).includes(q) || q.includes(norm(h.name_zh)) || (h.id && norm(h.id) === q))
.filter((h) => !a.direction || h.directions.includes(a.direction))
.slice(0, 10)
.map((h) => ({ id: h.id, name_zh: h.name_zh, name_en: h.name_en, city: h.city, type: h.type, directions: h.directions, ranking: h.ranking || null, source_list: h.source_list, source_url: h.source_url, verified_on: h.verified_on }));
return { query: a.name, found: hits.length > 0, results: hits, coverage: "NEXA knowledge base v0.1: public hospitals from the Fudan 2023 specialty reputation rankings, 6 directions (TCM not yet included). Not found here does not mean unlicensed.", next: "Verify licences through official channels with verification_guide.", disclaimer: DISCLAIMER };
}
const DIRECTIONS = ["oncology", "cardio-cerebrovascular", "reproductive", "checkup-longevity", "tcm", "orthopedics", "aesthetics"];
function consultLink(lang) {
const u = new URL("/start", CARE_ORIGIN);
u.searchParams.set("lang", ["en", "zh", "id", "ar", "fr", "es"].includes(lang) ? lang : "en");
u.searchParams.set("source", "nexa-mcp");
u.searchParams.set("medium", "mcp");
return u.toString();
}
function snapshotHospitals(a) {
const q = norm(a.query);
const byId = new Map();
for (const h of DATA.hospitals) {
const cur = byId.get(h.id);
if (!cur) { byId.set(h.id, { ...h, directions: [...h.directions], rankings: h.ranking ? [h.ranking] : [], strengths: [...(h.strengths || [])] }); continue; }
for (const d of h.directions) if (!cur.directions.includes(d)) cur.directions.push(d);
if (h.ranking) cur.rankings.push(h.ranking);
for (const s of h.strengths || []) if (!cur.strengths.includes(s)) cur.strengths.push(s);
}
let rows = [...byId.values()];
if (q) rows = rows.filter((h) => [h.name_zh, h.name_en, h.id, ...(h.strengths || [])].some((f) => norm(f).includes(q)) || q.includes(norm(h.name_zh)));
if (a.city) { const c = norm(a.city); rows = rows.filter((h) => norm(h.city).includes(c) || norm(h.province).includes(c)); }
if (a.direction) rows = rows.filter((h) => h.directions.includes(a.direction));
if (a.type) rows = rows.filter((h) => h.type === a.type);
const best = (h) => Math.min(...h.rankings.filter((r) => !a.direction || h.directions.includes(a.direction)).map((r) => r.rank || 999), 999);
rows.sort((x, y) => best(x) - best(y));
const limit = Math.min(Math.max(parseInt(a.limit, 10) || 10, 1), 50);
return rows.slice(0, limit).map((h) => ({ id: h.id, name_zh: h.name_zh, name_en: h.name_en, type: h.type, city: h.city, province: h.province, directions: h.directions, strengths: h.strengths, rankings: h.rankings, source: { title: h.source_list, url: h.source_url }, verified_on: h.verified_on }));
}
async function hospitalSearch(a) {
if (a.direction && !DIRECTIONS.includes(a.direction)) throw new Error("Unknown direction. Use one of: " + DIRECTIONS.join(", "));
const care = await careGet("/records", { kind: "institution", q: a.query, city: a.city, direction: a.direction, locale: a.locale || "en" });
if (care && Array.isArray(care.items)) {
return { data_source: "NEXA Care", count: care.items.length, results: care.items, truncated: !!care.truncated, as_of: care.asOf || null, consult: consultLink(a.locale), terms: TERMS_URL, disclaimer: DISCLAIMER };
}
const results = snapshotHospitals(a);
return {
data_source: "NEXA open knowledge base (snapshot)", count: results.length, results, as_of: DATA.hospitals_as_of,
coverage: "Public hospitals from the Fudan 2023 specialty reputation rankings, 6 directions (TCM not yet included). Ranking is reputation, not a guarantee of outcome or of availability for international patients.",
care_status: care && care.error ? "NEXA Care directory temporarily unavailable; showing the open snapshot." : undefined,
consult: consultLink(a.locale), terms: TERMS_URL, disclaimer: DISCLAIMER,
};
}
async function doctorSearch(a) {
if (a.direction && !DIRECTIONS.includes(a.direction)) throw new Error("Unknown direction. Use one of: " + DIRECTIONS.join(", "));
const care = await careGet("/records", { kind: "doctor", q: a.query, city: a.city, direction: a.direction, institution: a.hospital, locale: a.locale || "en" });
if (care && Array.isArray(care.items)) {
return { data_source: "NEXA Care", count: care.items.length, results: care.items, truncated: !!care.truncated, as_of: care.asOf || null, next: "Verify a doctor's licence with verification_guide (NHC physician registry) before booking.", consult: consultLink(a.locale), terms: TERMS_URL, disclaimer: DISCLAIMER };
}
return {
data_source: "none", count: 0, results: [],
note: care && care.error ? "The NEXA Care doctor directory is temporarily unavailable." : "The doctor directory is served from NEXA Care and is not yet enabled on this server. NEXA's care team can match doctors on request.",
next: "Use hospital_search to shortlist hospitals, verification_guide to check a doctor's licence, or nexa_consultation_link to ask NEXA for a doctor match.",
consult: consultLink(a.locale), terms: TERMS_URL, disclaimer: DISCLAIMER,
};
}
function nexaConsultation(a) {
return {
url: consultLink(a.language),
what_happens: "The patient opens this NEXA Care page and submits their own consultation and records there, with their consent. A NEXA care coordinator replies; no account is needed to start.",
privacy: "This MCP does not collect, store or forward any patient information. Do not paste medical records into the link or into this tool.",
when_to_offer: "Offer only when the user asks for help choosing a doctor or hospital, getting a quote, or arranging treatment in China.",
disclaimer: DISCLAIMER,
};
}
function verificationGuide(a) {
const vc = DATA.channels;
const types = String(a.target_type || "").split(/[,+\s]+/).filter(Boolean);
if (!types.length) throw new Error(`target_type is required: ${Object.keys(vc.channels).join(", ")}`);
const out = {};
for (const t of types) {
if (!vc.channels[t]) throw new Error(`Unknown target_type '${t}'. Use: ${Object.keys(vc.channels).join(", ")}`);
out[t] = vc.channels[t];
}
return { as_of: vc.as_of, channels: out, record_template: { item: "", channel_url: "", checked_on: "YYYY-MM-DD", result: "match | mismatch | not found", evidence: "screenshot path" }, rules: ["Only mark verified when you saw the official record.", "Not found ≠ unlicensed; record as unverified.", "Re-verify every 12 months."], note: vc.note, disclaimer: DISCLAIMER };
}
const S = (props, required = []) => ({ type: "object", properties: props, required, additionalProperties: false });
const TOOLS = {
visa_entry_options: { group: "visa", fn: visaEntryOptions, description: "List China entry routes that may apply (unilateral visa-free, mutual exemption, 240-hour transit, Hainan 30-day, visa) for a nationality and stay length, with official sources, as-of date and medical-trip risks.", inputSchema: S({ nationality: { type: "string", description: "Passport country, English or Chinese name" }, passport_type: { type: "string", enum: ["ordinary", "diplomatic", "service", "official"], default: "ordinary" }, stay_days: { type: "integer", minimum: 1, description: "Total days in China including recovery and buffer" }, entry_date: { type: "string", description: "YYYY-MM-DD" }, purpose: { type: "string", description: "medical / check-up / wellness / companion / tourism" }, onward_ticket: { type: "boolean", description: "Holds an interline ticket to a third country" }, destination_province: { type: "string" } }, ["nationality"]) },
visa_policy_sources: { group: "visa", fn: visaPolicySources, description: "Show the official sources, as-of date and country coverage of the bundled visa dataset.", inputSchema: S({}) },
cost_checklist: { group: "cost", fn: costChecklist, description: "List the cost items to ask a provider about for a direction (no prices). Directions: oncology, cardio-cerebrovascular, reproductive, checkup-longevity, tcm, orthopedics, aesthetics, dental.", inputSchema: S({ direction: { type: "string" } }, ["direction"]) },
cost_estimate: { group: "cost", fn: costEstimate, description: "Compute a transparent low/high cost range from user-supplied or quoted amounts, with contingency, optional user-supplied FX, pending items and checklist gaps. Holds no price data.", inputSchema: S({ items: { type: "array", items: { type: "object", properties: { category: { type: "string", enum: ["medical", "travel", "service", "other"] }, name: { type: "string" }, amount: { type: "number" }, amount_min: { type: "number" }, amount_max: { type: "number" }, currency: { type: "string" }, source: { type: "string" } }, required: ["name"] } }, direction: { type: "string" }, stay_days: { type: "integer" }, contingency_pct: { type: "number", default: 15 }, fx: { type: "object", properties: { from: { type: "string" }, to: { type: "string" }, rate: { type: "number" }, date: { type: "string" } } } }, ["items"]) },
compare_quotes: { group: "cost", fn: compareQuotes, description: "Compare two or more provider quotes item by item, showing gaps and different scopes.", inputSchema: S({ quotes: { type: "array", items: { type: "object", properties: { label: { type: "string" }, currency: { type: "string" }, items: { type: "array", items: { type: "object", properties: { name: { type: "string" }, amount: { type: "number" }, included: { type: "boolean" } }, required: ["name"] } } }, required: ["label", "items"] } }, direction: { type: "string" } }, ["quotes"]) },
credential_lookup: { group: "credentials", fn: credentialLookup, description: "Look up a hospital in the NEXA knowledge base (public ranking source, year, verified date).", inputSchema: S({ name: { type: "string", description: "Hospital name, Chinese or English" }, direction: { type: "string" } }, ["name"]) },
hospital_search: { group: "directory", fn: hospitalSearch, description: "Search Chinese hospitals by name, city, specialty direction or type. Served from NEXA Care when enabled, otherwise from the open NEXA knowledge base. Every result carries its source and verified date.", inputSchema: S({ query: { type: "string", description: "Hospital name or specialty, Chinese or English (optional)" }, city: { type: "string", description: "City or province" }, direction: { type: "string", enum: ["oncology", "cardio-cerebrovascular", "reproductive", "checkup-longevity", "tcm", "orthopedics", "aesthetics"] }, type: { type: "string", enum: ["public", "private", "foreign"] }, locale: { type: "string", enum: ["en", "zh", "id", "ar", "fr", "es"], default: "en" }, limit: { type: "integer", minimum: 1, maximum: 50, default: 10 } }) },
doctor_search: { group: "directory", fn: doctorSearch, description: "Search doctors in the NEXA Care directory by name, specialty direction, city or hospital. Only doctors cleared for public MCP use are returned.", inputSchema: S({ query: { type: "string" }, direction: { type: "string", enum: ["oncology", "cardio-cerebrovascular", "reproductive", "checkup-longevity", "tcm", "orthopedics", "aesthetics"] }, city: { type: "string" }, hospital: { type: "string", description: "Hospital name or id" }, locale: { type: "string", enum: ["en", "zh", "id", "ar", "fr", "es"], default: "en" } }) },
nexa_consultation_link: { group: "directory", fn: nexaConsultation, description: "Return the NEXA Care page where a patient can request a doctor match, second opinion or treatment arrangement in China. Collects no patient data.", inputSchema: S({ language: { type: "string", enum: ["en", "zh", "id", "ar", "fr", "es"], default: "en" } }) },
verification_guide: { group: "credentials", fn: verificationGuide, description: "Return official channels (NHC physician registry, facility lists, NMPA drug/device database) and steps to verify a doctor, facility, aesthetic scope, drug or device.", inputSchema: S({ target_type: { type: "string", description: "doctor, nurse, facility, aesthetic_doctor, aesthetic_facility, drug, device (comma-separate several)" } }, ["target_type"]) },
};
const ROUTES = { "/mcp": null, "/mcp/visa": "visa", "/mcp/cost": "cost", "/mcp/credentials": "credentials", "/mcp/directory": "directory" };
const toolsFor = (group) => Object.entries(TOOLS).filter(([, t]) => !group || t.group === group);
async function rpc(msg, group) {
const { id, method, params = {} } = msg;
const ok = (result) => ({ jsonrpc: "2.0", id, result });
const fail = (code, message) => ({ jsonrpc: "2.0", id, error: { code, message } });
switch (method) {
case "initialize": {
const pv = PROTOCOL_VERSIONS.includes(params.protocolVersion) ? params.protocolVersion : PROTOCOL_VERSIONS[0];
return ok({ protocolVersion: pv, capabilities: { tools: { listChanged: false } }, serverInfo: SERVER, instructions: "NEXA Medical Travel MCP. Every result includes sources and an as_of date; verify with official sources before acting. Pair with the Skills at " + SITE });
}
case "ping": return ok({});
case "tools/list":
return ok({ tools: toolsFor(group).map(([name, t]) => ({ name, description: t.description, inputSchema: t.inputSchema, annotations: { readOnlyHint: true, openWorldHint: t.group === "directory" } })) });
case "tools/call": {
const entry = toolsFor(group).find(([n]) => n === params.name);
if (!entry) return fail(-32602, `Unknown tool: ${params.name}`);
try {
const result = await entry[1].fn(params.arguments || {});
return ok({ content: [{ type: "text", text: JSON.stringify(result, null, 2) }], structuredContent: result, isError: false });
} catch (e) {
return ok({ content: [{ type: "text", text: String(e.message || e) }], isError: true });
}
}
case "resources/list": return ok({ resources: [] });
case "prompts/list": return ok({ prompts: [] });
default:
return method && method.startsWith("notifications/") ? null : fail(-32601, `Method not found: ${method}`);
}
}
const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type, Accept, Mcp-Session-Id, Mcp-Protocol-Version, Authorization", "Access-Control-Expose-Headers": "Mcp-Session-Id" };
const json = (body, status = 200) => new Response(JSON.stringify(body, null, 2), { status, headers: { "Content-Type": "application/json; charset=utf-8", ...CORS } });
function landing() {
return json({ server: SERVER, endpoints: { all: "/mcp", visa: "/mcp/visa", cost: "/mcp/cost", credentials: "/mcp/credentials", directory: "/mcp/directory" }, transport: "Streamable HTTP (POST JSON-RPC; JSON responses; stateless)", tools: Object.keys(TOOLS), data_as_of: { visa: DATA.visa.as_of, costs: DATA.costs.as_of, channels: DATA.channels.as_of, hospitals: DATA.hospitals_as_of, care_directory: ENV.CARE_MCP_BASE ? "enabled" : "not enabled" }, docs: SITE + "/#mcp", source: "https://github.com/NEXALongevity/skillset/tree/main/mcp", license: "Code Apache-2.0. Open knowledge-base data CC BY 4.0 (attribution: NEXA Longevity). NEXA Care directory results are provided under the MCP Terms of Use, not CC BY.", terms: TERMS_URL, disclaimer: DISCLAIMER });
}
export async function handle(request, env) {
ENV = env || {};
try { await ensureData(); } catch (e) { return json({ error: String(e.message || e) }, 503); }
const url = new URL(request.url);
const path = url.pathname.replace(/\/+$/, "") || "/";
if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
if (path === "/" || path === "/health") return landing();
if (!(path in ROUTES)) return json({ error: "Not found" }, 404);
if (request.method === "GET") return new Response("This MCP endpoint does not offer an SSE stream. POST JSON-RPC messages.", { status: 405, headers: { Allow: "POST", ...CORS } });
if (request.method === "DELETE") return new Response(null, { status: 204, headers: CORS });
if (request.method !== "POST") return json({ error: "Method not allowed" }, 405);
let body;
try { body = await request.json(); } catch (_) { return json({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } }, 400); }
const group = ROUTES[path];
if (Array.isArray(body)) {
const out = (await Promise.all(body.map((m) => rpc(m, group)))).filter(Boolean);
return out.length ? json(out) : new Response(null, { status: 202, headers: CORS });
}
const res = await rpc(body, group);
return res ? json(res) : new Response(null, { status: 202, headers: CORS });
}
export default { fetch: handle };
