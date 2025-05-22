import corrector.grammar

def test_correct_grammar(monkeypatch):
    def fake_correct_grammar(text):
        return "Исправленный текст", [{"rule": "fake"}]

    monkeypatch.setattr(corrector.grammar, "correct_grammar", fake_correct_grammar)

    corrected, matches = corrector.grammar.correct_grammar("ошибкой текст")
    assert corrected == "Исправленный текст"
    assert len(matches) == 1