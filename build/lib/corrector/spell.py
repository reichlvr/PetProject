from spellchecker import SpellChecker
import re

spell = SpellChecker(language='ru')

def correct_spelling(text: str) -> str:
    tokens = re.findall(r'\w+|\s+|[^\w\s]', text)
    corrected = []
    for token in tokens:
        if token.isspace() or not token.strip():
            corrected.append(token)
        elif token.isalpha():
            original_case = token
            fixed = spell.correction(token.lower()) or token
            if original_case.istitle():
                fixed = fixed.capitalize()
            corrected.append(fixed)
        else:
            corrected.append(token)
    return ''.join(corrected)