from .spell import correct_spelling
from .grammar import correct_grammar
from .utils import remove_repeats, highlight

def process_text(text: str) -> dict:
    corrected_grammar, grammar_errors = correct_grammar(text)
    corrected_spelling = correct_spelling(corrected_grammar)
    final_text = remove_repeats(corrected_spelling)
    highlighted = highlight(text, grammar_errors)
    return {
        'original': text,
        'corrected': final_text,
        'highlighted': highlighted,
    }
