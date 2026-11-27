# NEXA Medical Travel MCP

A free, read-only [Model Context Protocol](https://modelcontextprotocol.io) server that pairs with the Skills in this repo. "Skills attract, MCP connects": the Skills teach an agent the workflow, the MCP gives it facts that change quickly (with sources and dates) and calculations it should not do by hand.

**Endpoint:** `https://mcp.nxlongevity.com/mcp` (Streamable HTTP, stateless, JSON responses, no login)

| Path | Tools |
|---|---|
| `/mcp` | all tools below |
| `/mcp/visa` | `visa_entry_options`, `visa_policy_sources` |
| `/mcp/cost` | `cost_checklist`, `cost_estimate`, `compare_quotes` |
| `/mcp/credentials` | `credential_lookup`, `verification_guide` |

## What each server does, and does not do

**Visa & entry policy.** Matches a nationality and stay length against China's unilateral visa-free list, the MFA mutual visa-exemption list (ordinary passports), the 240-hour transit and Hainan 30-day policies, and always returns "apply for a visa" as a fallback. Flags that published visa-free purposes do not list medical treatment, and warns when a stay crosses a policy end date. Data in [`data/visa.json`](data/visa.json), every entry linked to an official source, `as_of` 2026-11-27. Nationalities not in the dataset are reported as not covered, never guessed.

**Cost estimate & quote comparison.** Holds **no prices**. It lists the cost items to ask about per direction, computes a low/high range from amounts the user or a written quote supplies (with contingency and user-supplied FX), and compares quotes item by item to expose missing items.

**Doctor & facility credential check.** Looks a hospital up in the NEXA knowledge base (public ranking source, year, verified date) and returns the official channels to verify a doctor, facility, aesthetic scope, drug or device (NHC physician registry, NHC facility lists, NMPA database). It does not perform the official lookup itself.

## Connect

Claude Code:

```bash
claude mcp add --transport http nexa-travel https://mcp.nxlongevity.com/mcp
```

Any MCP client that supports remote HTTP servers: add `https://mcp.nxlongevity.com/mcp` as a server URL.

## Develop

```bash
python mcp/build.py     # bundles mcp/data + data/hospitals into mcp/dist/worker.js
node mcp/test.mjs       # smoke tests
```

`mcp/dist/worker.js` is a single-file Cloudflare Worker. Edit `mcp/src/worker.js` and `mcp/data/*.json`, rebuild, then deploy the dist file (Cloudflare dashboard editor or `wrangler deploy` with [`wrangler.toml`](wrangler.toml)).

When you update data, change `as_of`, cite the official source URL, and keep the rule: if a fact cannot be traced to an official source, it does not go in.

## Licence

Code Apache-2.0, data CC BY 4.0. Attribution: Based on NEXA Medical Travel Skills by NEXA Longevity (nxlongevity.com). Information only; not medical, legal or immigration advice.
