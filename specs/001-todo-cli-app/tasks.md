---

description: "Task list for Todo CLI Application implementation"
---

# Tasks: Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python project with rich dependency in pyproject.toml
- [x] T003 [P] Configure linting and formatting tools (ruff, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create base Todo model in src/models/todo.py
- [x] T005 [P] Create TodoService in src/services/todo_service.py
- [x] T006 Create CLI entry point in main.py
- [x] T007 Create CLI interface in src/cli/cli.py
- [x] T008 Configure in-memory storage mechanism with TodoService
- [x] T009 Set up basic CLI command handling

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: User can add new tasks to their todo list with title and description

**Independent Test**: Add command with title and description works, and viewing shows the task with correct details

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for Todo model validation in tests/unit/test_todo.py
- [x] T011 [P] [US1] Integration test for adding todos in tests/integration/test_todo_service.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Implement Todo model with validation rules in src/models/todo.py
- [x] T013 [US1] Implement add_todo method in TodoService in src/services/todo_service.py
- [x] T014 [US1] Create add command handler in src/cli/cli.py
- [x] T015 [US1] Add command parsing for 'add' in main.py
- [x] T016 [US1] Add error handling for empty title in src/services/todo_service.py
- [x] T017 [US1] Add success message for added todo in src/cli/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: User can view all tasks with proper formatting and visual distinction between completed/incomplete

**Independent Test**: View command shows all todos in a formatted table with visual indicators

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T018 [P] [US2] Unit test for todo display formatting in tests/unit/test_todo.py
- [x] T019 [P] [US2] Integration test for viewing todos in tests/integration/test_todo_service.py

### Implementation for User Story 2

- [x] T020 [P] [US2] Implement view_all_todos method in TodoService in src/services/todo_service.py
- [x] T021 [US2] Create view command handler in src/cli/cli.py
- [x] T022 [US2] Add table formatting using rich library in src/cli/cli.py
- [x] T023 [US2] Add visual distinction for completed/incomplete tasks in src/cli/cli.py
- [x] T024 [US2] Add command parsing for 'view' in main.py
- [x] T025 [US2] Handle case when no todos exist in src/cli/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: User can mark tasks as complete or incomplete with visual feedback

**Independent Test**: Mark commands change the status of a task and viewing shows the updated status

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T026 [P] [US3] Unit test for marking todos complete/incomplete in tests/unit/test_todo.py
- [x] T027 [P] [US3] Integration test for marking todos in tests/integration/test_todo_service.py

### Implementation for User Story 3

- [x] T028 [P] [US3] Implement mark_complete method in TodoService in src/services/todo_service.py
- [x] T029 [P] [US3] Implement mark_incomplete method in TodoService in src/services/todo_service.py
- [x] T030 [US3] Create complete command handler in src/cli/cli.py
- [x] T031 [US3] Create incomplete command handler in src/cli/cli.py
- [x] T032 [US3] Add command parsing for 'complete' and 'incomplete' in main.py
- [x] T033 [US3] Add error handling for invalid todo ID in src/services/todo_service.py
- [x] T034 [US3] Add success messages for status changes in src/cli/cli.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo (Priority: P3)

**Goal**: User can update the title and description of existing tasks

**Independent Test**: Update command modifies details of a task and viewing shows the updated details

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T035 [P] [US4] Unit test for updating todos in tests/unit/test_todo.py
- [x] T036 [P] [US4] Integration test for updating todos in tests/integration/test_todo_service.py

### Implementation for User Story 4

- [x] T037 [US4] Implement update_todo method in TodoService in src/services/todo_service.py
- [x] T038 [US4] Create update command handler in src/cli/cli.py
- [x] T039 [US4] Add command parsing for 'update' in main.py
- [x] T040 [US4] Add validation for updated title in src/services/todo_service.py
- [x] T041 [US4] Add error handling for invalid todo ID in src/services/todo_service.py
- [x] T042 [US4] Add success message for updated todo in src/cli/cli.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: User can delete tasks they no longer need

**Independent Test**: Delete command removes a task and viewing confirms it's gone

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T043 [P] [US5] Unit test for deleting todos in tests/unit/test_todo.py
- [x] T044 [P] [US5] Integration test for deleting todos in tests/integration/test_todo_service.py

### Implementation for User Story 5

- [x] T045 [US5] Implement delete_todo method in TodoService in src/services/todo_service.py
- [x] T046 [US5] Create delete command handler in src/cli/cli.py
- [x] T047 [US5] Add command parsing for 'delete' in main.py
- [x] T048 [US5] Add error handling for invalid todo ID in src/services/todo_service.py
- [x] T049 [US5] Add success message for deleted todo in src/cli/cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T050 [P] Add help command with available commands in main.py
- [x] T051 [P] Add exit command functionality in main.py
- [x] T052 Add comprehensive error handling across all commands in src/cli/cli.py
- [x] T053 [P] Add input validation across all commands in src/cli/cli.py
- [x] T054 Add rich library styling to all CLI output in src/cli/cli.py
- [x] T055 [P] Add additional unit tests in tests/unit/
- [x] T056 Create comprehensive README with usage instructions
- [x] T057 Run quickstart.md validation to ensure all features work as specified

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model validation in tests/unit/test_todo.py"
Task: "Integration test for adding todos in tests/integration/test_todo_service.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo model with validation rules in src/models/todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence