import re
from dataclasses import dataclass

@dataclass
class Tasks:
    title: str
    completed: bool

    @staticmethod
    def to_camel_case(s: str) -> str:
        words: list[str] = re.split(r'[_\-\s]+', s)
        if not words:
            return ''
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


