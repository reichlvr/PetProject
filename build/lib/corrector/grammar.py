from typing import Tuple, List
import language_tool_python

def correct_grammar(text: str) -> Tuple[str, List]:
    tool = language_tool_python.LanguageToolPublicAPI('ru-RU')
    matches = tool.check(text)
    # Фильтруем ложные срабатывания
    filtered = [
        m for m in matches 
        if not (m.ruleId == 'RULE_IGNORE' or 'PUNCTUATION' in m.category)
    ]
    corrected = tool.correct(text)
    return corrected, filtered