from ..base import GeneratorPlugin

class XGenerator(GeneratorPlugin):
    def generate(self, draft: dict) -> dict:
        return {'type': 'x', 'content': 'Generated x content'}
