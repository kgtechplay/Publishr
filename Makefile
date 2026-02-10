.PHONY: setup test run-gateway

setup:
	python -m pip install -e ./packages/common
	python -m pip install -e ./packages/workflow_contracts
	python -m pip install -e ./services/gateway_api
	python -m pip install -e ./services/orchestrator
	python -m pip install -e ./services/worker_research
	python -m pip install -e ./services/worker_draft
	python -m pip install -e ./services/worker_generate
	python -m pip install -e ./services/worker_publish

run-gateway:
	uvicorn services.gateway_api.src.main:app --reload --port 8000

test:
	python -m compileall services packages
