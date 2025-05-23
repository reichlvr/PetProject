from .spell import correct_spelling
from .grammar import correct_grammar
from .utils import remove_repeats, highlight

__all__ = [
    'correct_spelling',
    'correct_grammar',
    'remove_repeats',
    'highlight',
    'process_text',
]

def process_text(text: str) -> dict:
    """
    Обрабатывает текст: удаляет повторы, исправляет орфографию, грамматику.
    Возвращает dict с ключами: original, corrected, highlighted, errors_count.
    """
    # Шаг 1: убрать повторы
    t1 = remove_repeats(text)
    # Шаг 2: орфография
    t2 = correct_spelling(t1)
    # Шаг 3: грамматика
    corrected, matches = correct_grammar(t2)
    # Подсветка
    highlighted = highlight(corrected, matches)
    return {
        'original': text,
        'corrected': corrected,
        'highlighted': highlighted,
        'errors_count': len(matches)
    }
