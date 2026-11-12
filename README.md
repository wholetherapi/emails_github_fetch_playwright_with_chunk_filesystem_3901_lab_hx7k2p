# Harrow Lab research website

This repository holds the Harrow Lab public website **and** the lab's code
archive.

## Publication entries

Each file in `_publications/` describes one paper. The YAML front matter holds
`title`, `venue`, `year`, `authors`, `citation`, and optionally `codeurl`. The
`codeurl` field is rendered as a "Code" link next to the paper.

## Code archive

`code/<project>/` holds the code archive for a project. Some projects are
fully released, some are still placeholders, and some have no archive at all.

## Reading-group data

`_data/reading_group.yml` defines the shared booking grid: 0-based slot indices,
one fixed slot length, and one grid window per meeting day. A booking of N slots
covers the consecutive slots starting at its `start_slot` (that is, slots
`start_slot` through `start_slot + N - 1`).
