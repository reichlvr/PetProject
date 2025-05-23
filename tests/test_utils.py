import pytest
from corrector.utils import remove_repeats, highlight

class DummyError:
    def __init__(self, offset, length):
        self.offset = offset
        self.errorLength = length

def test_remove_repeats():
    assert remove_repeats("а а а б б") == "а б"

def test_highlight():
    text = "ошибка"
    err = DummyError(0, 3)
    assert highlight(text, [err]).startswith("[оши]бка")
