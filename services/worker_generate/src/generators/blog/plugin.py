from ..base import GeneratorPlugin

class BlogGenerator(GeneratorPlugin):
    def generate(self, draft: dict) -> dict:
        return {'type': 'blog', 'content': 'Generated blog content'}
