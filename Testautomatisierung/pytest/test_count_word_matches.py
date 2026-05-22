import pytest
from count_word_matches import count_word_matches


"""
Basis-Tests mit Parametrisierung
Schreibe einen parametrisierten Test, um die Funktion für einfache, 
gemischte und einfache Randfallszenarien zu validieren.
"""
@pytest.mark.parametrize("text, target, expected", [
    ("The cat sat on the mat", "cat", 1),
    ("Dog dog DOG dOg", "dog", 4), # groß- kleinschreibung ignoriert
    ("Hello world", "world", 1),
    ("hello hello HELLO", "hello", 3),
    ("No matches here", "yes", 0), # keine Übereinstimmungen
    ("catcat cat catdog", "cat", 1), # nur eigenständiges cat zählt
    ("a a a", "a", 3)
])

def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected


print("hello patrick")