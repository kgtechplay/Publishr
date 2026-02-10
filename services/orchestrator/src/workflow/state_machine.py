class RunStateMachine:
    def __init__(self):
        self.state = 'created'

    def transition(self, new_state: str):
        self.state = new_state
