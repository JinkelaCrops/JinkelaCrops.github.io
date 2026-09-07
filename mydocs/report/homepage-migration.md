# Homepage migration

- task_id: github-home-migration
- spec_id: homepage-migration
- run_id: github-home-migration-20260908

The supplied prototype is now a production static website with its original layout and interactions. It retains explicit proposed-project and outline labels. Old content remains recoverable from Git history and independent backup.

Validation: three structural/release tests, JavaScript interaction tests (language/theme, saved preference and blocked storage), syntax check, local HTTP 200. No scientific results or new open-source releases are claimed. Visual browser QA has not been performed.

Published at https://jinkelacrops.github.io/. Implementation commit: 55728eccbc8b6cd758efa26e4f58f1842cd24cc6. GitHub Pages build succeeded; five live files returned HTTP 200 and matched local bytes. A retired article URL correctly returned the archive navigation 404.
