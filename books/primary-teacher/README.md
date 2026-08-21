# Primary Teacher Library

This directory is the canonical source for the Primary Teacher product.

## Authoring order

1. Read `PRIMARY_LIBRARY_TAXONOMY.md`.
2. Read `001-master-framework.md`.
3. For a subject, read its `framework.md` before its prompt files.
4. Add concise prompt specifications only after the module taxonomy and framework are stable.

## Status

The existing long-form prompt files are retained as source material during migration. They are not the target architecture.

## VS Code synchronisation

GitHub `main` is the canonical repository. The local VS Code project should be kept as a normal git working copy. Do not manually recreate the GitHub structure independently.

When the migration baseline is agreed, pull the canonical structure into VS Code and use git status before committing any local changes.
