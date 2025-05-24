import re
from typing import List

def remove_repeats(text: str) -> str:
    """Удаляет повторяющиеся слова, сохраняя пробелы."""
    return re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', text, flags=re.IGNORECASE)

def highlight(text: str, errors: List) -> str:
    """Точная подсветка ошибок."""
    highlighted = []
    last_pos = 0
    for error in sorted(errors, key=lambda x: x.offset):
        start = error.offset
        end = start + error.errorLength
        highlighted.append(text[last_pos:start])
        highlighted.append(f'[{text[start:end]}]')
        last_pos = end
    highlighted.append(text[last_pos:])
    return ''.join(highlighted)