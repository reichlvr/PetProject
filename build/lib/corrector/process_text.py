from .grammar import get_grammar_errors
from .utils import find_repeats, highlight

def process_text(text: str) -> dict:
    """Обрабатывает текст и возвращает ошибки для интерактивного режима."""
    repeat_errors = find_repeats(text)  
    grammar_errors = get_grammar_errors(text)
    all_errors = repeat_errors + grammar_errors
    all_errors.sort(key=lambda x: x['offset'])  
    highlighted = highlight(text, all_errors)   
    return {
        'original': text,
        'errors': all_errors,
        'highlighted': highlighted,
        'errors_count': len(all_errors)
    }