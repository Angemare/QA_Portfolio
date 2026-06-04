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


"""### Übung 2: Testen von Randfällen (Edge Case Testing)

Erstelle ein Fixture, das häufige Randfall-Eingaben bereitstellt, und teste die Funktion mit parametrisierten Tests.

Fokussiere auf leere Eingaben, Leerzeichen und Interpunktion.

"""


#@pytest.fixture
#def count_word_matches():
  # return

@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello world", "world", 1), # zusätzliche leerzeichen ignoriert
    (" cat ", "cat", 1),
    ("cat,dog cat","cat", 1),
    ("x y z", "x", 1)
 ])

def test_count_word_matches_target(text, target, expected):
    assert count_word_matches(text, target) == expected