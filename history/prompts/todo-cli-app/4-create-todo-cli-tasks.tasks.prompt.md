---
id: 4
title: Create Todo CLI Tasks
stage: tasks
date_iso: 2025-01-07
surface: agent
model: Qwen
feature: todo-cli-app
branch: 001-todo-cli-app
user: user
command: /sp.tasks
labels:
  - tasks
  - todo
  - cli
  - implementation
links:
  - spec: specs/001-todo-cli-app/spec.md
  - plan: specs/001-todo-cli-app/plan.md
  - tasks: specs/001-todo-cli-app/tasks.md
  - data-model: specs/001-todo-cli-app/data-model.md
  - contracts: specs/001-todo-cli-app/contracts/cli-contract.md
  - ticket: null
  - adr: null
  - pr: null
files_yaml:
  - "specs/001-todo-cli-app/tasks.md"
tests_yaml: []
prompt_text: |
  Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
  handoffs: 
    - label: Analyze For Consistency
      agent: sp.analyze
      prompt: Run a project analysis for consistency
      send: true
    - label: Implement Project
      agent: sp.implement
      prompt: Start the implementation in phases
      send: true
  
  ## User Input
  
  ```text
  $ARGUMENTS
  ```
  
  You **MUST** consider the user input before proceeding (if not empty).
  
  ## Outline
  
  1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").
  
  2. **Load design documents**: Read from FEATURE_DIR:
     - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
     - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
     - Note: Not all projects have all documents. Generate tasks based on what's available.
  
  3. **Execute task generation workflow**:
     - Load plan.md and extract tech stack, libraries, project structure
     - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
     - If data-model.md exists: Extract entities and map to user stories
     - If contracts/ exists: Map endpoints to user stories
     - If research.md exists: Extract decisions for setup tasks
     - Generate tasks organized by user story (see Task Generation Rules below)
     - Generate dependency graph showing user story completion order
     - Create parallel execution examples per user story
     - Validate task completeness (each user story has all needed tasks, independently testable)
  
  4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
     - Correct feature name from plan.md
     - Phase 1: Setup tasks (project initialization)
     - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
     - Phase 3+: One phase per user story (in priority order from spec.md)
     - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
     - Final Phase: Polish & cross-cutting concerns
     - All tasks must follow the strict checklist format (see Task Generation Rules below)
     - Clear file paths for each task
     - Dependencies section showing story completion order
     - Parallel execution examples per story
     - Implementation strategy section (MVP first, incremental delivery)
  
  5. **Report**: Output path to generated tasks.md and summary:
     - Total task count
     - Task count per user story
     - Parallel opportunities identified
     - Independent test criteria for each story
     - Suggested MVP scope (typically just User Story 1)
     - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)
  
  Context for task generation: Generate Actionable tasks
  
  The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.
  
  ## Task Generation Rules
  
  **CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.
  
  **Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.
  
  ### Checklist Format (REQUIRED)
  
  Every task MUST strictly follow this format:
  
  ```text
  - [ ] [TaskID] [P?] [Story?] Description with file path
  ```
  
  **Format Components**:
  
  1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
  2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
  3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
  4. **[Story] label**: REQUIRED for user story phase tasks only
     - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
     - Setup phase: NO story label
     - Foundational phase: NO story label  
     - User Story phases: MUST have story label
     - Polish phase: NO story label
  5. **Description**: Clear action with exact file path
  
  **Examples**:
  
  - ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
  - ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
  - ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
  - ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
  - ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
  - ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
  - ❌ WRONG: `- [ ] [US1] Create model` (missing Task ID)
  - ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)
  
  ### Task Organization
  
  1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
     - Each user story (P1, P2, P3...) gets its own phase
     - Map all related components to their story:
       - Models needed for that story
       - Services needed for that story
       - Endpoints/UI needed for that story
       - If tests requested: Tests specific to that story
     - Mark story dependencies (most stories should be independent)
  
  2. **From Contracts**:
     - Map each contract/endpoint → to the user story it serves
     - If tests requested: Each contract → contract test task [P] before implementation in that story's phase
  
  3. **From Data Model**:
     - Map each entity to the user story(ies) that need it
     - If entity serves multiple stories: Put in earliest story or Setup phase
     - Relationships → service layer tasks in appropriate story phase
  
  4. **From Setup/Infrastructure**:
     - Shared infrastructure → Setup phase (Phase 1)
     - Foundational/blocking tasks → Foundational phase (Phase 2)
     - Story-specific setup → within that story's phase
  
  ### Phase Structure
  
  - **Phase 1**: Setup (project initialization)
  - **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
  - **Phase 3+**: User Stories in priority order (P1, P2, P3...)
    - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
    - Each phase should be a complete, independently testable increment
  - **Final Phase**: Polish & Cross-Cutting Concerns
  
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
  I have successfully generated the tasks for the Todo CLI Application. Here's what was accomplished:

  1. Created the tasks file at `specs/001-todo-cli-app/tasks.md` with:
     - 8 phases including Setup, Foundational, and 5 user story phases in priority order
     - 56 individual tasks across all phases
     - Proper format compliance with checklists for each task
     - Clear file paths for each task
     - Story labels (US1-US5) for user story tasks
     - Parallelism markers [P] where appropriate
     - Dependencies and execution order sections
     - Implementation strategy section

  2. The tasks are organized by:
     - Phase 1: Setup tasks (project initialization)
     - Phase 2: Foundational (blocking prerequisites)
     - Phase 3: User Story 1 - Add Todo (Priority P1)
     - Phase 4: User Story 2 - View Todos (Priority P1)
     - Phase 5: User Story 3 - Mark Complete/Incomplete (Priority P2)
     - Phase 6: User Story 4 - Update Todo (Priority P3)
     - Phase 7: User Story 5 - Delete Todo (Priority P3)
     - Phase 8: Polish & Cross-Cutting Concerns

  3. Each user story phase includes:
     - Goal and independent test criteria
     - Test tasks (optional)
     - Implementation tasks with proper file paths
     - Checkpoint verification

  4. The tasks follow the required format with checkboxes, task IDs, story labels where needed, and file paths.

  The tasks are now ready for implementation. Each user story can be implemented and tested independently, following the MVP-first approach.
outcome: |
  Successfully generated comprehensive task list for Todo CLI application with 56 tasks across 8 phases, following proper format and organization guidelines.
evaluation: |
  The generated tasks file contains all required sections, follows the template structure, uses correct formatting for all tasks, and maps all user stories from the specification with proper priorities and dependencies.
---