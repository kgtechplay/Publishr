# Solution Understanding

This repository uses a microservice-oriented architecture where each workflow node is isolated by responsibility.

## End-to-end flow
1. **Gateway API** receives topic/project/run commands and query requests.
2. **Orchestrator** owns workflow state and dispatches node work to workers.
3. **Worker Research** enriches the initial topic with live context (news/tools/posts).
4. **Worker Draft** combines topic + research + human feedback into a canonical draft.
5. **Worker Generate** fans out draft into artifact types via plugin generators.
6. **Worker Publish** routes artifacts to social/media destinations via destination plugins.
7. Results, artifact metadata, and publish jobs are persisted for retrieval and auditing.

## Key folders
- `services/gateway_api`: REST entrypoint, schemas, models, DB session.
- `services/orchestrator`: state machine and node dispatch logic.
- `services/worker_*`: task workers for each node.
- `packages/common`: shared infrastructure utilities.
- `packages/workflow_contracts`: canonical command/event contracts.
- `infra/migrations`: migration scripts placeholder.

## File-level map (high-level)
- Every `main.py` starts the service runtime.
- `api/routers/*` are endpoint groups.
- `workflow/nodes/*` are orchestrator node handlers.
- `generators/*/plugin.py` define artifact generation plugins.
- `destinations/*/plugin.py` define publish adapters.
- `registry.py` files provide discovery + registration for plugin extensibility.

Add new content type: create new `worker_generate/src/generators/<type>/plugin.py` and register it.
Add new destination: create new `worker_publish/src/destinations/<platform>/plugin.py` and register it.
