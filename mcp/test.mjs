// Smoke tests: node mcp/test.mjs
import worker from "./dist/worker.js";
import assert from "node:assert/strict";
const call = async (path, body) => {
  const r = await worker.fetch(new Request("https://x" + path, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) }));
  return r.status === 202 ? null : r.json();
};
const tool = async (name, args, path = "/mcp") => (await call(path, { jsonrpc: "2.0", id: 1, method: "tools/call", params: { name, arguments: args } })).result;

const init = await call("/mcp", { jsonrpc: "2.0", id: 0, method: "initialize", params: { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "t", version: "1" } } });
assert.equal(init.result.serverInfo.name, "nexa-medical-travel");
assert.equal(await call("/mcp", { jsonrpc: "2.0", method: "notifications/initialized" }), null);
const all = await call("/mcp", { jsonrpc: "2.0", id: 2, method: "tools/list" });
assert.equal(all.result.tools.length, 7);
const visaOnly = await call("/mcp/visa", { jsonrpc: "2.0", id: 3, method: "tools/list" });
assert.deepEqual(visaOnly.result.tools.map((t) => t.name), ["visa_entry_options", "visa_policy_sources"]);

let v = (await tool("visa_entry_options", { nationality: "法国", stay_days: 28, entry_date: "2026-12-10", purpose: "surgery" })).structuredContent;
assert.equal(v.nationality, "France");
assert.ok(v.risks.some((r) => r.includes("2026-12-31")));
assert.ok(v.risks.some((r) => r.includes("Medical treatment is not listed")));
v = (await tool("visa_entry_options", { nationality: "Singapore", stay_days: 5, purpose: "check-up" })).structuredContent;
assert.ok(v.options.some((o) => o.route.startsWith("Mutual") && o.may_apply === true));
v = (await tool("visa_entry_options", { nationality: "United States", stay_days: 14 })).structuredContent;
assert.ok(v.risks[0].includes("not in this dataset"));
assert.equal(v.summary, "Apply for a visa.");
v = (await tool("visa_entry_options", { nationality: "UK", stay_days: 40, entry_date: "2027-01-10" })).structuredContent;
assert.equal(v.options[0].may_apply, false);
v = (await tool("visa_entry_options", { nationality: "台湾" })).structuredContent;
assert.ok(v.summary.includes("台胞证"));

let c = (await tool("cost_estimate", { direction: "reproductive", contingency_pct: 20, items: [
  { category: "medical", name: "促排与监测", amount: 18000, source: "A" }, { category: "medical", name: "取卵", amount: 6000, source: "A" },
  { category: "medical", name: "胚胎培养", amount: 8000, source: "A" }, { category: "medical", name: "移植", amount: 5000, source: "A" },
  { category: "medical", name: "促排药费" }, { category: "travel", name: "住宿", amount: 11250 }, { category: "service", name: "口译", amount: 6400 }] })).structuredContent;
assert.equal(c.totals_by_currency.CNY.low, 54650);
assert.equal(c.totals_by_currency.CNY.high, 65580);
assert.deepEqual(c.pending_quote, ["促排药费"]);
c = (await tool("cost_estimate", { contingency_pct: 15, fx: { from: "AUD", to: "CNY", rate: 4.7, date: "2026-11-26" }, items: [
  { category: "medical", name: "手术及住院", amount_min: 95000, amount_max: 120000, source: "Q" }, { category: "travel", name: "机票", amount: 3200, currency: "AUD" },
  { category: "travel", name: "住宿", amount: 10800 }, { category: "service", name: "口译", amount: 2700 }] })).structuredContent;
assert.equal(c.converted.low, 123540);
assert.equal(c.converted.high, 170821);
const q = (await tool("compare_quotes", { direction: "reproductive", quotes: [{ label: "A", items: [{ name: "取卵", amount: 6000 }] }, { label: "B", items: [{ name: "取卵", included: true }, { name: "移植", included: true }] }] })).structuredContent;
assert.deepEqual(q.gaps[0].missing_items, ["移植"]);
const k = (await tool("credential_lookup", { name: "积水潭" })).structuredContent;
assert.ok(k.found && k.results[0].source_url.startsWith("https://"));
const g = (await tool("verification_guide", { target_type: "aesthetic_doctor,device" })).structuredContent;
assert.ok(g.channels.device[0].url.includes("datasearch.nmpa.gov.cn"));
const bad = await tool("cost_checklist", { direction: "unknown" });
assert.equal(bad.isError, true);
console.log("all MCP smoke tests passed");
