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

# test fixture
@pytest.fixture
def text():
    return ""

@pytest.fixture
def target():
    return "word"

def test_fixture(text, target):
    assert count_word_matches(text, target) == 0
    assert count_word_matches(text, target) != 1


@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello world", "world", 1), # zusätzliche leerzeichen ignoriert
    (" cat ", "cat", 1),
    ("cat,dog cat","cat", 1),
    ("x y z", "x", 1)
 ])

def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected


""" ### Übung 3: Negativtests (Negative Testing)

Teste die Funktion auf ungültige Eingaben wie `None`, Ganzzahlen oder Listen, um sicherzustellen,
 dass sie die entsprechenden Ausnahmen (Exceptions) auslöst.

Verwende ein Fixture, um Testfälle für ungültige Eingaben bereitzustellen.

"""

@pytest.fixture
def invalid_info():
    return [
        ("None", "word", 0),
        ("hello world", "None", 0),
        (123, "word", AttributeError),
        ("hello world", 456, AttributeError),
        (["hello", "world"], "world", AttributeError),
        ("hello world", ["world"], AttributeError)
    ]

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






# testing parametrize (para sa akin lang parang exercise)
@pytest.mark.parametrize("text, target, expected", [
    ("None", "word", 0),
    ("hello world", "None", 0),
])


def test_negative_testing(text, target, expected):
    assert count_word_matches(text, target) == expected


@pytest.mark.parametrize("text, target, exception", [
    (123, "word", AttributeError),
    ("hello world", 456, AttributeError),
    (["hello", "world"], "world", AttributeError),
    ("hello world", ["world"], AttributeError)
])
def test_exception(text, target, exception):
    with pytest.raises(AttributeError):
        count_word_matches(text, target)
