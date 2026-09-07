# Homepage migration — current spec

- task_id: github-home-migration
- spec_id: homepage-migration
- run_id: github-home-migration-20260908

## Goal / Restated Understanding
Publish the user-provided HTML prototype as the personal website, preserving its visual design, bilingual content, themes, mobile layout and expandable outlines.

## Done Contract
Preserve the previous website history; verify production assets, navigation and interactive state; synchronize GitHub and verify the live page.

## Scope / Facts / Constraints
Use existing static GitHub Pages publishing from master/root. Preserve the supplied prototype CSS without visual redesign. Split maintainable source into src/ and publish generated assets at root. Proposed projects remain proposed. Private implementation and internal documents are excluded.

## Open Questions
Resolved: user supplied the original prototype archive. No Astro rewrite is necessary to publish the existing standalone prototype.

## Checkpoint Summary
The user explicitly requested migration, reconstruction and synchronization. Prior website preserved at 2587917178fceb9c10a831371d60442fe0c78614 and verified in an independent archive before replacing active files.

## Implementation and Validation
Removed preview banner/noindex; added canonical URL, robots and sitemap. Added archive link and custom 404 for retired pages. Preserved all six expandable outlines and original responsive CSS. Local checks: 3 Python tests passed; JavaScript syntax and language/theme/storage/accessibility state tests passed; local HTTP 200.

## Change Log
2026-09-08: Prototype migrated into deployable static website. Historical website removed from active publishing tree after independent backup verification.

## Resume / Handoff
Next: commit, push without force, verify GitHub Pages build and live assets. Browser visual QA is not recorded as performed.

## Project Sync Candidates
README documents the verified static editing/publishing workflow.
