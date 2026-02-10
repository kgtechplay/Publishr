from ..base import GeneratorPlugin

class AnimationGenerator(GeneratorPlugin):
    def generate(self, draft: dict) -> dict:
        return {'type': 'animation', 'content': 'Generated animation content'}
