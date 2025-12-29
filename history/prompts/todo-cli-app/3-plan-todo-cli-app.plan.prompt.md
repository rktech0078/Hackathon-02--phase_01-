---
id: 3
title: Plan Todo CLI App
stage: plan
date_iso: 2025-01-07
surface: agent
model: Qwen
feature: todo-cli-app
branch: 001-todo-cli-app
user: user
command: /sp.plan
labels:
  - planning
  - todo
  - cli
  - architecture
links:
  - spec: specs/001-todo-cli-app/spec.md
  - plan: specs/001-todo-cli-app/plan.md
  - research: specs/001-todo-cli-app/research.md
  - data-model: specs/001-todo-cli-app/data-model.md
  - quickstart: specs/001-todo-cli-app/quickstart.md
  - contracts: specs/001-todo-cli-app/contracts/cli-contract.md
  - ticket: null
  - adr: null
  - pr: null
files_yaml:
  - "specs/001-todo-cli-app/plan.md"
  - "specs/001-todo-cli-app/research.md"
  - "specs/001-todo-cli-app/data-model.md"
  - "specs/001-todo-cli-app/quickstart.md"
  - "specs/001-todo-cli-app/contracts/cli-contract.md"
tests_yaml: []
prompt_text: |
  Execute the implementation planning workflow using the plan template to generate design artifacts.
  handoffs: 
    - label: Create Tasks
      agent: sp.tasks
      prompt: Break the plan into tasks
      send: true
    - label: Create Checklist
      agent: sp.checklist
      prompt: Create a checklist for the following domain...
  
  ## User Input
  
  ```text
  $ARGUMENTS
  ```
  
  You **MUST** consider the user input before proceeding (if not empty).
  
  ## Outline
  
  1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").
  
  2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).
  
  3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
     - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
     - Fill Constitution Check section from constitution
     - Evaluate gates (ERROR if violations unjustified)
     - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
     - Phase 1: Generate data-model.md, contracts/, quickstart.md
     - Phase 1: Update agent context by running the agent script
     - Re-evaluate Constitution Check post-design
  
  4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.
  
  ## Phases
  
  ### Phase 0: Outline & Research
  
  1. **Extract unknowns from Technical Context** above:
     - For each NEEDS CLARIFICATION → research task
     - For each dependency → best practices task
     - For each integration → patterns task
  
  2. **Generate and dispatch research agents**:
  
     ```text
     For each unknown in Technical Context:
       Task: "Research {unknown} for {feature context}"
     For each technology choice:
       Task: "Find best practices for {tech} in {domain}"
     ```
  
  3. **Consolidate findings** in `research.md` using format:
     - Decision: [what was chosen]
     - Rationale: [why chosen]
     - Alternatives considered: [what else evaluated]
  
  **Output**: research.md with all NEEDS CLARIFICATION resolved
  
  ### Phase 1: Design & Contracts
  
  **Prerequisites:** `research.md` complete
  
  1. **Extract entities from feature spec** → `data-model.md`:
     - Entity name, fields, relationships
     - Validation rules from requirements
     - State transitions if applicable
  
  2. **Generate API contracts** from functional requirements:
     - For each user action → endpoint
     - Use standard REST/GraphQL patterns
     - Output OpenAPI/GraphQL schema to `/contracts/`
  
  3. **Agent context update**:
     - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
     - These scripts detect which AI agent is in use
     - Update the appropriate agent-specific context file
     - Add only new technology from current plan
     - Preserve manual additions between markers
  
  **Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file
  
  ## Key rules
  
  - Use absolute paths
  - ERROR on gate failures or unresolved clarifications
  
  ---
  
  As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.
  
  1) Determine Stage
     - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general
  
  2) Generate Title and Determine Routing:
     - Generate Title: 3–7 words (slug for filename)
     - Route is automatically determined by stage:
       - `constitution` → `history/prompts/constitution/`
       - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
       - `general` → `history/prompts/general/`
  
  3) Create and Fill PHR (Shell first; fallback agent‑native)
     - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
     - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
     - If the script fails:
       - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
       - Allocate an ID; compute the output path based on stage from step 2; write the file
       - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT
  
  4) Validate + report
     - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
     - On failure: warn, don't block. Skip only for `/sp.phr`.
response_text: |
  I have successfully completed the implementation planning for the Todo CLI Application. Here's what was accomplished:

  1. Created the implementation plan at `specs/001-todo-cli-app/plan.md`:
     - Defined technical context with Python 3.13+, Rich library, and in-memory storage
     - Verified compliance with all constitutional requirements
     - Outlined project structure with clear separation of concerns

  2. Completed Phase 0 - Research:
     - Created `specs/001-todo-cli-app/research.md` with technology analysis and architecture decisions

  3. Completed Phase 1 - Design & Contracts:
     - Created `specs/001-todo-cli-app/data-model.md` defining the Todo entity structure
     - Created `specs/001-todo-cli-app/quickstart.md` with setup and usage instructions
     - Created `specs/001-todo-cli-app/contracts/cli-contract.md` defining the CLI interface contract
     - Updated agent context with new technology information

  4. All constitutional requirements were validated and confirmed to be met throughout the planning process.

  The implementation plan is now complete and ready for the next phase. You can proceed with `/sp.tasks` to break the plan into implementable tasks.
outcome: |
  Successfully completed implementation planning with all required artifacts generated and constitutional compliance verified.
evaluation: |
  All required planning artifacts were created according to the template structure. The plan includes technical context, constitution check, project structure, research findings, data model, quickstart guide, and contracts. All constitutional requirements were verified to be met.
---