import pytest
from corrector.spell import correct_spelling

def test_correct_spelling_simple():
    text = "превед медвед"
    corrected = correct_spelling(text)
    assert "привет" in corrected or "медведь" in corrected
