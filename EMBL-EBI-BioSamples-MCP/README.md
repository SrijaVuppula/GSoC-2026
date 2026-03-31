# EMBL-EBI BioSamples MCP

## Project focus
This work is an early prototype for an AI-assisted BioSamples workflow.

## Current prototype scope
- Parse natural-language sample descriptions into structured metadata
- Detect missing required fields
- Generate clarification questions
- Parse natural-language search queries into structured search filters

## Current files
- `biosamples_parser.py`
- `biosamples_search_parser.py`
- `submission_demo_output.txt`
- `search_demo_output.txt`
- `validation_rules.txt`
- `project_understanding.txt`
- `work_done_summary.txt`

## Current status
The current prototype demonstrates an initial submission-side and search-side flow for BioSamples-style metadata interaction.

## Next possible extensions
- stronger field validation
- checklist-aware metadata rules
- API integration
- MCP tool wrapping
- normalized result formatting