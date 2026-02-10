from .state_machine import RunStateMachine

class WorkflowEngine:
    def __init__(self):
        self.machine = RunStateMachine()

    def status(self):
        return {'state': self.machine.state}
