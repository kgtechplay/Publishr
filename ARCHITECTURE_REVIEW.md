# Publishr architecture review

Your proposed structure is a strong foundation for a plugin-driven, extensible publishing system.

## What is already strong

- Clear separation of concerns across API, orchestration, workers, shared packages, and infra.
- Plugin-oriented design for both **content generation types** and **publish destinations**.
- Distinct workflow steps that map to your intended nodes.

## Recommended changes

### 1) Add a canonical workflow contracts package

You currently share some types in `packages/common`, but workflow-specific contracts should be versioned centrally so all services stay compatible.

Suggested addition:

```text
packages/
  workflow_contracts/
    pyproject.toml
    src/
      workflow_contracts/
        commands.py     # StartRun, RegenerateAsset, PublishRun, etc.
        events.py       # ResearchCompleted, DraftCompleted, AssetGenerated, PublishCompleted
        enums.py        # statuses, artifact types, destinations
        versions.py     # schema version constants
```

Why: this prevents drift between `orchestrator`, workers, and gateway DTOs.

### 2) Split gateway API into command/query routers and add idempotency

Your router list is good; add explicit command endpoints and idempotency handling for safe retries.

Suggested additions in `services/gateway_api/src/api/`:

```text
routers/
  commands.py   # create project/topic/run, trigger publish
  queries.py    # list/get run state and artifacts
middleware/
  idempotency.py
```

Why: queue-based systems will retry; API consumers should be able to safely retry too.

### 3) Add explicit run lifecycle + human feedback checkpoints

You already have node sequence. Add a strict state model and user feedback checkpoint between research and draft (and optionally before publish).

Suggested additions:

```text
services/orchestrator/src/workflow/
  state_machine.py
  checkpoints.py   # waiting_for_user_feedback, approved_for_publish, etc.
```

Why: this aligns with your requirement that user updates inform final content.

### 4) Add a content planning layer before generators

Node 3 currently jumps from draft to content plugins. Add a planner that maps draft -> required artifacts.

Suggested addition:

```text
services/worker_generate/src/generators/
  planner.py   # decides which generators to invoke + dependencies
```

Why: supports future asset types without changing orchestration logic.

### 5) Add a platform capability matrix for destinations

Different social platforms support different media, text limits, and auth scopes.

Suggested addition:

```text
services/worker_publish/src/destinations/
  capabilities.py  # per-destination constraints and supported artifact types
```

Why: makes routing and validation deterministic and extensible.

### 6) Add persistence model for provenance and revisions

You have `artifact.py` and `publish_job.py`; add revision/provenance tracking.

Suggested DB model additions:

```text
services/gateway_api/src/db/models/
  artifact_revision.py
  source_citation.py
  approval.py
```

Why: needed for auditability and iterative edits.

### 7) Add worker reliability primitives (retry/DLQ/backoff)

Suggested additions:

```text
services/orchestrator/src/queue/
  retry_policy.py
  dead_letter.py
```

Why: failures from LLM/tool APIs are common; resilient workflows need standard handling.

### 8) Add policy and safety modules

Given automated publishing, add validation and moderation before publish.

Suggested additions:

```text
services/worker_generate/src/
  validation/
    policy.py        # banned terms, style constraints, platform compliance

services/worker_publish/src/
  validation/
    preflight.py     # destination-specific checks before send
```

Why: prevents publishing invalid or unsafe output.

### 9) Add test scaffolding by service + contract tests

Suggested top-level addition:

```text
tests/
  contract/
  integration/
  e2e/
```

And per-service tests under each service package.

Why: contract tests are critical in distributed plugin architectures.

### 10) Add local developer workflow files

Suggested additions:

```text
Makefile
scripts/
  dev_up.sh
  dev_migrate.sh
  seed_demo_data.py
```

Why: easier onboarding and reproducible development.

## Revised high-level structure (minimal diff)

```text
publishr/
  README.md
  ARCHITECTURE_REVIEW.md
  docker-compose.dev.yml
  .env.example
  Makefile
  scripts/
    dev_up.sh
    dev_migrate.sh
    seed_demo_data.py

  services/
    gateway_api/
      ...
      src/api/
        routers/
          commands.py
          queries.py
        middleware/
          idempotency.py

    orchestrator/
      ...
      src/workflow/
        engine.py
        state_machine.py
        checkpoints.py

    worker_generate/
      ...
      src/generators/
        planner.py
        ... existing plugins ...
      src/validation/
        policy.py

    worker_publish/
      ...
      src/destinations/
        capabilities.py
      src/validation/
        preflight.py

  packages/
    common/
      ...
    workflow_contracts/
      pyproject.toml
      src/workflow_contracts/
        commands.py
        events.py
        enums.py
        versions.py

  tests/
    contract/
    integration/
    e2e/

  infra/
    migrations/
    railway/
    nginx/
```

## Priority order for implementation

1. `workflow_contracts` package
2. Orchestrator state machine + checkpoints
3. Generator planner + destination capabilities
4. Idempotency + retries/DLQ
5. Policy/preflight validation
6. Provenance/revision DB models
7. Contract/integration test suite

This sequence gives you extensibility first, then reliability and compliance.
