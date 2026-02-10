from ..base import GeneratorPlugin

class LinkedinGenerator(GeneratorPlugin):
    def generate(self, draft: dict) -> dict:
        return {'type': 'linkedin', 'content': 'Generated linkedin content'}
