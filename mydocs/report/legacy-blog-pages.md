# Earlier writing: on-site archive

- task_id: legacy-blog-pages
- spec_id: homepage-migration (follow-up)
- run_id: legacy-blog-pages-20260908

The homepage now links to /blog/. Nine chronological posts and two referenced readings have standalone pages in the homepage design. Original URLs also serve those pages. The reading layout supports images, code, tables, dark mode and common navigation. Body text remains in the original language; page controls support Chinese/English.

All eleven source body texts are preserved. All 49 copied assets match the archive. Six structural/content-routing tests and JavaScript interaction checks pass. Two files were already absent in the original snapshot (SasWrap.wsf and sas.zip); their links are explicitly marked unavailable. External source citations remain historical links and were not exhaustively revalidated.

Published: https://jinkelacrops.github.io/blog/. Implementation commit cf2c69743a3e27d51d0dbf2c51891be82a643e8c. All 25 checked live routes/assets returned HTTP 200 and matched local bytes.
