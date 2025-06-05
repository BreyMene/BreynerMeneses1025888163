import pytest
from app.checker import PasswordChecker

@pytest.mark.parametrize("password,expected", [
    ("ab1", "Débil"),             # Muy corta
    ("abcdefgh", "Débil"),         # Solo minúsculas
    ("abcde123", "Media"),         # Minúsculas + dígitos
    ("Abcd1234", "Fuerte"),        # Mayúsculas + minúsculas + dígitos
    ("Abc1@def", "Fuerte"),        # Todos los criterios
    ("ABCD@#$%", "Media"),         # Mayúsculas + símbolos
    ("Ab1@5678", "Fuerte"),        # Justo 8 caracteres, cumple todo
    ("        ", "Débil"),         # Solo espacios
    ("123456", "Débil"),           # Solo dígitos
    ("a@a222fJdska", "Media")     # Largo y cumple todos los criterios
])
def test_password_strength(password, expected):
    checker = PasswordChecker(password)
    assert checker.evaluate_strength() == expected
