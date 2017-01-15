from pathlib import Path

class MarkdownConverter:
    converters = []

    @classmethod
    def Register(cls, converter_class):
        cls.converters.append(converter_class())
        return converter_class

    def __init__(self, file):
        self.file = file

    def convert(self):
        text = Path(self.file).read_text()
        # TODO solve this functional-style instead of mutating text
        for converter in MarkdownConverter.converters:
            text = converter.convert(text)
        return text