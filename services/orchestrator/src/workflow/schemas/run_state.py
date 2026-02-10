from dataclasses import dataclass

@dataclass
class RunState:
    run_id: str
    state: str
