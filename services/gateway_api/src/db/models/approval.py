from dataclasses import dataclass

@dataclass
class ApprovalModel:
    id: str
    run_id: str
    approved: bool
