from typing import List
import language_tool_python

def get_grammar_errors(text: str) -> List[dict]:
    """Возвращает список грамматических и орфографических ошибок."""
    tool = language_tool_python.LanguageToolPublicAPI('ru-RU')
    matches = tool.check(text)
    errors = []
    for match in matches:
        if match.ruleId != 'RULE_IGNORE' and 'PUNCTUATION' not in match.category:
            errors.append({
                'type': match.category,
                'offset': match.offset,
                'errorLength': match.errorLength,
                'message': match.message,
                'replacements': match.replacements
            })
    return errors
