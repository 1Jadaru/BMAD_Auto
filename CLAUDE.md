# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **BMAD Automation** project - a system that automates the BMAD-METHOD workflow to drive ideas through a complete development lifecycle, producing high-quality artifacts (PRDs, Architecture, Stories, QA gates, UX specs) with minimal manual intervention.

## Architecture

### Core Structure
- `.bmad-core/` - Contains the BMAD-METHOD framework with agents, tasks, templates, and workflows
- `docs/` - Generated artifacts (PRDs, architecture docs, stories, QA results)
- `AGENTS.md` - Auto-generated agent definitions for the BMAD system

### Agent System
The system uses specialized agents that orchestrate development workflows:
- **bmad-master** - Universal task executor across all domains
- **bmad-orchestrator** - Workflow coordination and multi-agent task management
- **Specialist agents** - PM, PO, Architect, Dev, QA, UX, SM agents in `.bmad-core/agents/`

### Key Components
- **Tasks** (`.bmad-core/tasks/`) - Executable workflow definitions
- **Templates** (`.bmad-core/templates/`) - Document templates for artifacts
- **Checklists** (`.bmad-core/checklists/`) - Quality gates and validation rules
- **Configuration** (`.bmad-core/core-config.yaml`) - Project-specific settings

## Development Workflow

### Automation Modes
- **Automatic** - Full automation with minimal human intervention
- **Semi-Automatic** - Checkpoints for approval at key milestones
- **Interactive** - Full elicitation for all user inputs

### Core Pipeline
The system orchestrates: PM → PRD → Architect → Architecture → SM → Stories → QA → UX → Dev

### Document Generation
- PRDs generated to `docs/prd.md` (or sharded in `docs/prd/`)
- Architecture docs to `docs/architecture.md` (or sharded in `docs/architecture/`)
- Stories in `docs/stories/`
- QA results in `docs/qa/`

## Important Patterns

### BMAD Agent Activation
When working with BMAD agents, they require specific activation:
1. Read the complete agent definition file
2. Load `bmad-core/core-config.yaml` for project configuration  
3. Follow activation instructions exactly as specified
4. Tasks with `elicit: true` require user interaction - cannot be bypassed

### Task Execution
- Tasks are executable workflows, not reference material
- Follow task instructions exactly as written
- Interactive workflows require user participation
- Present options as numbered lists for user selection

## Configuration

Key configuration in `.bmad-core/core-config.yaml`:
- Document locations and versioning
- Sharding preferences for large documents
- QA and development file patterns
- Markdown processing settings

## Quality Gates

The system includes automated quality checks:
- PO Master Checklist for PRDs
- Architect Checklist for architecture
- Story Draft Checklist for stories
- QA gates for validation

When working with this codebase, respect the BMAD methodology constraints and always honor the elicitation requirements for interactive workflows.