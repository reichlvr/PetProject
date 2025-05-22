from typing import Tuple, List
import language_tool_python

def correct_grammar(text: str) -> Tuple[str, List]:
    tool = language_tool_python.LanguageToolPublicAPI('ru-RU')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return corrected, matches
