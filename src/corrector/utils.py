import re
from typing import List

def remove_repeats(text: str) -> str:
    """Удаляет повторяющиеся слова, сохраняя пробелы."""
    return re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', text, flags=re.IGNORECASE)

def highlight(text: str, errors: List) -> str:
    """Подсвечивает ошибки в квадратных скобках по offset и errorLength."""
    sorted_errors = sorted(errors, key=lambda x: x.offset, reverse=True)
    highlighted = list(text)
    offset = 0
    for error in sorted_errors:
        start = error.offset + offset
        end = start + error.errorLength
        # Вставляем скобки
        highlighted.insert(end, ']')
        highlighted.insert(start, '[')
        offset += 2
    return ''.join(highlighted)
