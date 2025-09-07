# BMAD Automation Product Requirements Document (PRD)

## Executive Summary
BMAD Automation is a system that takes a human’s input idea and drives it through the full BMAD‑METHOD workflow automatically, producing high‑quality artifacts (PRD, Architecture, Stories, QA gates, UX specs) with minimal manual intervention. It orchestrates BMAD agents and tasks (PM/PO/SM/UX/QA/Dev/Architect) using templates and checklists, provides configurable automation modes (Automatic, Semi‑Automatic with checkpoints, and Interactive), and integrates with Git/VCS to persist outputs.

Primary value: drastically reduce time from concept to a production‑ready set of documents and stories while preserving rigor, traceability, and quality gates of the BMAD framework.

## Problem Statement
- Creating consistent, comprehensive BMAD artifacts is time‑consuming and requires expert familiarity with agents and tasks.
- Teams want to bootstrap new projects (or features) rapidly without compromising quality, compliance, or traceability.
- Current flows are highly manual; cross‑agent handoffs are error‑prone, and context is scattered.

## Goals & Success Metrics
- Reduce time from idea to “Epic 1 stories ready for Dev” by 80%.
- Produce complete, standards‑aligned artifacts with ≥ 90% checklist pass rate (PO/Architect/QA checklists) on first run.
- Human edits decrease over time (≤ 15% of content routinely requires revision after 3 uses).
- Automation modes used: 70% automatic/semi‑automatic, 30% interactive (by choice, not necessity).

## Target Users
- Product owners/managers wanting fast, high‑quality planning.
- Tech leads/architects seeking structured documentation with minimal overhead.
- Startup founders and teams needing to spin up projects quickly.
- Agencies and consultancies standardizing deliverables at scale.

## MVP Scope
### In-Scope (MVP)
- Idea Intake: short prompt + optional attachments.
- Orchestrated Agent Flow: PM → PRD → Architect → Architecture → SM → Stories → QA review → UX optional → Dev scaffold prompt.
- Automation Modes: Automatic, Semi‑Automatic (checkpoint approvals), Interactive.
- Task Runner: Executes BMAD tasks/templates/checklists from `.bmad-core` with yolo where permitted and checkpointed elicitation otherwise.
- Artifact Persistence: Write outputs to repo (docs/*), track versions, and generate consolidated indexes.
- VCS Integration: Local Git actions, optional GitHub push (when configured).
- Quality Gates: Auto-run story/PRD/architecture checklists; generate a final Validation Report.

### Out of Scope (MVP)
- Live code implementation or dependency installs (Dev agent remains advisory/scaffold stage only).
- Advanced multi-repo orchestration.
- Human identity management or SSO.

## Requirements
### Functional Requirements (FR)
1. FR1: Idea Intake API/UI: accept idea text, metadata (project name, target users), and optional seed docs.
2. FR2: Agent Orchestration Engine: sequence PM → PRD → Architect → Architecture → SM → Stories → QA → (optional) UX, with configurable order.
3. FR3: Automation Modes: automatic (yolo where possible), semi‑automatic (checkpoints), interactive (full elicitation) selectable per run.
4. FR4: Elicitation Handling: when tasks require `elicit: true`, support strategies: 
   - (a) Auto‑heuristics (prompt templates, defaults), 
   - (b) Ask‑for‑approval at checkpoints, 
   - (c) Full interactive Q&A.
5. FR5: Task Runner: discover and execute `.bmad-core` tasks/templates, pass parameters, collect outputs.
6. FR6: Artifact Synthesis: write outputs to `docs/` (PRD, architecture, stories, UX, QA gates), add ToCs and shard as configured.
7. FR7: Quality Checks: run checklists (PO, Architect, Story, QA) and produce a gate decision summary (PASS/CONCERNS/FAIL).
8. FR8: Storage & Versioning: local filesystem writes and Git commits (optional push to remote).
9. FR9: Runbook & Logs: store execution logs, prompts, and decisions for traceability.
10. FR10: Configuration: per‑project config (agents enabled, templates, shard policy, naming conventions).

### Non‑Functional Requirements (NFR)
1. NFR1: Reliability: deterministic task orchestration; recoverable from mid‑flow crashes (idempotent steps).
2. NFR2: Performance: end‑to‑end automated run for typical greenfield project finishes ≤ 5 minutes on standard hardware.
3. NFR3: Extensibility: plugin architecture for new agents/tasks and external tool hooks (e.g., VCS providers).
4. NFR4: Observability: structured logs; summary report; optional telemetry (opt‑in, privacy‑respecting).
5. NFR5: Security/Privacy: minimize sensitive data; redact secrets; respect local sandbox policies; no unintended network access unless approved.
6. NFR6: Portability: run via CLI (Node.js LTS) on Windows, macOS, Linux; no heavy external dependencies by default.
7. NFR7: Compliance: honor BMAD guardrails (e.g., QA and Dev section editing constraints), license compliance for templates.

## Technical Assumptions
- Runtime: Node.js LTS (20.x), TypeScript strict.
- Interface: CLI first (with support for Codex CLI/Codium integration), optional simple API server.
- BMAD Core: consume `.bmad-core` tasks/templates/checklists in the target repo or a provided path.
- Storage: filesystem (workspace), Git for versioning, optional GitHub push.
- LLM provider(s): abstracted behind an adapter; support prompt templates and few‑shot patterns.
- Config: YAML/JSON config file controlling agents, shard locations, automation mode, checkpoints.

## User Experience (High-Level)
- CLI Command: `bmad-auto run --mode=auto --project-name "X" --out docs/`
- Checkpoints (semi‑auto): present a concise diff/summary and ask “Approve/Amend/Skip.”
- Interactive mode: surface elicitation prompts as numbered options (consistent with BMAD), capture inputs, resume flow.
- Dashboard (optional): basic HTML/markdown report with progress, artifacts links, gates summary.

## Integration & Automation Modes
- Automatic: default strategies + heuristics answer elicitation; skip optional UX if not requested.
- Semi‑Automatic: pause at key milestones (PRD ready, Architecture ready, Stories ready) for approval/edits.
- Interactive: fully honor every `elicit:true` step, using BMAD’s 1–9 options flow.

## Quality & Gates
- Run the following automatically:
  - PO Master Checklist on PRD.
  - Architect Checklist on Architecture.
  - Story Draft Checklist on every generated story.
  - QA Gate (advisory) on first epic’s first story as a dry run.
- Produce a final Validation Report with pass/concerns/fail and recommended next steps.

## MVP Epics Overview
- Epic 1: Core Orchestrator & Task Runner
  - Build a sequencer to execute BMAD tasks/templates; implement automation modes; produce logs.
- Epic 2: Artifact Generation & Sharding
  - Generate PRD/Architecture/Stories; shard and link ToCs; persist with Git commits.
- Epic 3: Elicitation Strategies & Checkpoints
  - Implement heuristics/templates to answer common elicitation; add semi‑auto checkpoints.
- Epic 4: Quality Gates & Reports
  - Run checklists/gates; build Validation Report; expose status summary in CLI output.
- Epic 5: VCS Integration & Project Bootstrap
  - Initialize Git, optional GitHub integration; seed repo with BMAD core if missing.
- Epic 6: Observability & Configuration
  - Add structured logs, run metadata, and a configuration system; add test harness.

## Selected Epic Details (MVP)
### Epic 1: Core Orchestrator & Task Runner
- Goals: deterministically run PM→PRD→Architect→Architecture→SM→Stories→QA→UX.
- Stories:
  1. Orchestration pipeline with step registry and retries.
  2. BMAD task executor (load `.bmad-core/tasks/*`, `.bmad-core/templates/*`).
  3. Mode switch: auto / semi‑auto / interactive.
  4. Execution logs and run IDs.

### Epic 2: Artifact Generation & Sharding
- Goals: create PRD/architecture/stories; shard; write ToCs.
- Stories:
  1. PRD generator: goals, requirements, scope, assumptions; write docs/BMAD_PRD.md.
  2. Architecture generator: high‑level + decomposition.
  3. Stories generator: Epic 1 stories; run story checklist.
  4. Shard & ToC injection for long docs.

### Epic 3: Elicitation Strategies & Checkpoints
- Goals: reduce human workload while honoring BMAD guardrails.
- Stories:
  1. Heuristic answerer for common 1–9 prompts (defaults, patterns, seed config).
  2. Checkpoint UX: show diff + rationale; Approve/Amend/Skip.
  3. Resume from checkpoint after edits.

## Constraints & Policies
- Respect BMAD editing constraints (e.g., QA writes only QA Results, Dev only Dev Agent Record sections).
- Avoid bypassing “elicit:true” in interactive mode; in auto/semi‑auto, use documented heuristics and record that auto‑answers were used.
- Keep artifacts editable by humans; do not produce binary or locked outputs.

## Risks & Mitigations
- Risk: Over‑automation yields shallow artifacts. Mitigation: semi‑auto checkpoints; QA/PO checklists; Validation Report.
- Risk: BMAD task changes break automation. Mitigation: versioned adapters; tests against sample repos.
- Risk: Vendor lock‑in (LLM). Mitigation: adapter pattern for providers.
- Risk: VCS/remote failures. Mitigation: local commits first; retry/prompt for re‑auth.

## Compliance & Ethics
- Log when auto‑answers are used; expose provenance in final report.
- Avoid storing sensitive data; offer redaction and local‑only mode.
- Honor project sandbox and approval policies for network or destructive actions.

## Operational Policies
- Node LTS; TypeScript strict; ESLint/Prettier enforced.
- Structured logs; opt‑in telemetry; no default network access without approval.
- Sample CI: run unit tests for orchestrator, dry‑run on sample BMAD repo.

## Next Steps
1. Approve MVP epics and scope.
2. Architect: design orchestrator, task adapter interfaces, and mode controller.
3. Create sample fixtures of BMAD repos for test automation.
4. Implement Epic 1 and Epic 2; iterate with semi‑auto checkpoints enabled by default.

### Architect Prompt
Use this PRD to produce an architecture plan for BMAD Automation:
- Orchestrator design (state machine), task adapters for BMAD tasks/templates, automation mode controller.
- Elicitation handling (auto heuristics, checkpoint UX flows), artifact writers and sharders.
- Logging/observability, config system, and VCS module for local Git and optional GitHub push.
- Security/runtime constraints: sandbox, approvals, and provenance logging.
- Output: diagrams, module contracts, error handling & retry strategy, and a phased implementation roadmap aligned to the epics above.

