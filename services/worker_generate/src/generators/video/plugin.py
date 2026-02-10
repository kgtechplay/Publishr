from ..base import GeneratorPlugin

class VideoGenerator(GeneratorPlugin):
    def generate(self, draft: dict) -> dict:
        return {'type': 'video', 'content': 'Generated video content'}
