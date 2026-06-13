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


""" Testen von Randfällen (Edge Case Testing)

Erstelle ein Fixture, das häufige Randfall-Eingaben bereitstellt, und teste die Funktion mit parametrisierten Tests.

Fokussiere auf leere Eingaben, Leerzeichen und Interpunktion.

"""

# test mit fixture edge case
@pytest.fixture()
def edge_cases():
    # return gibt den wert an den test zurück
    return [
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello world", "world", 1),  # zusätzliche leerzeichen ignoriert
    (" cat ", "cat", 1),
    ("cat,dog cat", "cat", 1),
    ("x y z", "x", 1)
]

# testfunktion edge_cases - fixture test
def test_with_edge_cases():
    assert count_word_matches("", "word") == 0
    assert count_word_matches("hello world", "") == 0
    assert count_word_matches("", "") == 0
    assert count_word_matches("hello world", "world") == 1
    assert count_word_matches(" cat ", "cat") == 1
    assert count_word_matches("cat, dog cat", "cat") == 1
    assert count_word_matches("x y z", "x") == 1


# testing edge cases with parametrize
@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello world", "world", 1),  # zusätzliche leerzeichen ignoriert
    (" cat ", "cat", 1),
    ("cat,dog cat", "cat", 1),
    ("x y z", "x", 1)
])

# testfunktion mit edge cases und parametrize
def test_count_matches_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected



""" Negativtests (Negative Testing)

Teste die Funktion auf ungültige Eingaben wie `None`, Ganzzahlen oder Listen, um sicherzustellen,
 dass sie die entsprechenden Ausnahmen (Exceptions) auslöst.

Verwende ein Fixture, um Testfälle für ungültige Eingaben bereitzustellen.

"""

@pytest.fixture
def invalid_info():
    # return gibt den Wert an den Test zurück
    return [
        ("None", "word", 0),
        ("hello world", "None", 0),
        (123, "word", AttributeError),
        ("hello world", 456, AttributeError),
        (["hello", "world"], "world", AttributeError),
        ("hello world", ["world"], AttributeError)
    ]

# testfunktion mit invalid_info
def test_with_invalid_info():
    assert count_word_matches("None", "word") == 0
    assert count_word_matches("hello world", "None") == 0
    with pytest.raises(AttributeError):
        count_word_matches(123, "word")
    with pytest.raises(AttributeError):
        count_word_matches("hello world", 456)
    with pytest.raises(AttributeError):
        count_word_matches(["hello", "world"], "world")
    with pytest.raises(AttributeError):
        count_word_matches("hello world", ["world"])




# testing parametrize
@pytest.mark.parametrize("text, target, expected", [
    ("None", "word", 0),
    ("hello world", "None", 0),
])

# testfunction
def test_negative_testing(text, target, expected):
    assert count_word_matches(text, target) == expected


@pytest.mark.parametrize("text, target, exception", [
    (123, "word", AttributeError),
    ("hello world", 456, AttributeError),
    (["hello", "world"], "world", AttributeError),
    ("hello world", ["world"], AttributeError)
])

# testfunction
def test_exception(text, target, exception):
    with pytest.raises(AttributeError):
        count_word_matches(text, target)
