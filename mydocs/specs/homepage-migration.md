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
Complete: implementation commit 55728eccbc8b6cd758efa26e4f58f1842cd24cc6 pushed without force. GitHub Pages reported built. Live HTML, CSS, JS, robots and sitemap returned HTTP 200 and matched local bytes. Retired article URL returned the custom archive 404. Browser visual QA is not recorded as performed.

## Project Sync Candidates
README documents the verified static editing/publishing workflow.

## Follow-up: legacy-blog-pages
User requested an on-site blog list and independently readable pages in the homepage style. This supersedes the earlier archive-to-GitHub/404 behavior.

Done Contract: nine listed posts, two linked readings, preserved original body text/assets, functioning internal routes and anchors, shared theme/navigation, old URL compatibility, verified publishing.

Implementation: src/blog content and assets are built into /blog/ plus original URL aliases. Source body text of all eleven documents matches the archive, excluding the explicit missing-attachment labels. All 49 copied assets are byte-identical. The two originally absent downloads are labeled unavailable. Original attribution remains. Six Python checks and JavaScript theme/language checks pass. No browser visual QA is claimed.

Checkpoint: complete. Implementation commit cf2c69743a3e27d51d0dbf2c51891be82a643e8c published. All 25 checked live routes/assets returned HTTP 200 and matched local bytes, covering the list, eleven article pages, eleven old routes, homepage and CSS. No new project-wide policy changes.
