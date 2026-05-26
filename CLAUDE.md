## Design Context

### Users
Software developers and technical partners building integrations on top of Frame.io's V4 API. Two primary audiences: (1) **Platform developers** — engineers building workflow, DAM, and creative tooling integrations who want fast access to API data and credentials; (2) **C2C partners** — hardware/firmware engineers at camera manufacturers needing device-level upload analytics and provisioning. Both are technical and task-oriented — they come to build, debug, and monitor, not browse.

### Brand Personality
Cinematic. Precise. Authoritative.

Modeled after **next.frame.io** — deep-space dark backgrounds, confident serif/sans type pairing, a blue/teal accent palette that feels premium without being cold. The portal should feel like a first-class surface in the Frame.io product family.

### Aesthetic Direction
- **Theme**: Dark mode only. `#060810` backgrounds, layered surface cards, minimal intentional glow effects
- **Typography**: DM Serif Display for hero/editorial headings, DM Sans for UI text, monospace for code/credentials
- **Color**: `#4b8ef7` blue (primary), `#0bc5ea` teal (C2C), `#f59e0b` amber (Premier tier), semantic green/red for status
- **Motion**: Purposeful and restrained. Honor `prefers-reduced-motion`
- **References**: next.frame.io + next.developer.frame.io (primary), Stripe (typographic precision), Vercel (dark-mode developer platform)
- **Anti-references**: Generic SaaS dashboards, startup playfulness, legacy enterprise density

### Design Principles

1. **Cinematic confidence** — Every screen belongs in the Frame.io product family. Dark, immersive, precise. No generic UI chrome.
2. **Data earns its place** — Every number, chart, and table serves a clear developer job-to-be-done. Remove anything decorative that doesn't inform.
3. **Tier clarity without friction** — Developer / Partner / Premier access levels should feel aspirational, not punishing. Locked sections make users want to upgrade.
4. **Typography does the heavy lifting** — DM Serif Display / DM Sans pairing creates hierarchy without decorative elements. Let type scale, weight, and contrast do the work.
5. **Developer trust first** — Credentials, API keys, and usage data are high-stakes. The UI must feel secure, organized, and reliable.

---

## Scout — Frame.io code search

Scout indexes 70+ Frame.io repos and should be used for any Frame.io-specific code searches, pattern lookups, or cross-repo validation before making changes.

Scout lives at `~/Desktop/JT Claude Code/agent-framework/` and runs as an MCP server once set up. **Setup required before first use** — run `python3 scripts/scout_setup.py` from inside agent-framework (requires Rust/cargo; coordinate with Zane).

Until Scout is set up, use the knowledge docs in `agent-framework/knowledge/repos/` for cross-repo reference.

---

## Handoff file

Global handoff rules apply (see ~/.claude/CLAUDE.md). The `handoff.md` template for this project:

```
# Frame.io Dev Portal — Handoff
_[DATE]_

## What We Were Working On
[One sentence — UI section, feature, content update]

## Accomplished This Session
-

## Current State
[What's rendering correctly vs. broken or placeholder]

## Files Touched
-

## Key Decisions Made
[Design/layout choices with the why]
-

## Known Issues / Blockers
-

## Exact Next Steps
1.
2.
3.
```
