from spellchecker import SpellChecker

spell = SpellChecker(language='ru')

def correct_spelling(text: str) -> str:
    words = text.split()
    result = []
    for w in words:
        if w.lower() in spell:
            result.append(w)
        else:
            corr = spell.correction(w)
            result.append(corr or w)
    return ' '.join(result)
