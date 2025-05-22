import re
from typing import List


def remove_repeats(text: str) -> str:
    """Удаляет повторяющиеся подряд слова."""
    pattern = re.compile(r"\b(\w+)( \1\b)+", flags=re.IGNORECASE)
    return pattern.sub(r"\1", text)


def highlight(text: str, errors: List) -> str:
    """Подсвечивает ошибки в квадратных скобках по offset и errorLength."""
    offset = 0
    for e in errors:
        start = e.offset
       # уменьшаем длину подсветки на 1, но не менее 1
        length = max(1, e.errorLength - 1)
        text = (
           text[: start + offset]
           + '['
          + text[start + offset : start + offset + length]
           + ']'
          + text[start + offset + length :])
        offset += 2
    return text
