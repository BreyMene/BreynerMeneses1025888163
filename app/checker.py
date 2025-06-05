import re

class PasswordChecker:
    """
    Clase que evalúa la fortaleza de una contraseña con base en reglas definidas.
    """

    def __init__(self, password: str):
        self.password = password
        self.requirements_met = 0

    def has_min_length(self, min_length: int = 8) -> bool:
        return len(self.password) >= min_length

    def check_uppercase(self) -> bool:
        return bool(re.search(r'[A-Z]', self.password))

    def check_lowercase(self) -> bool:
        return bool(re.search(r'[a-z]', self.password))

    def check_digit(self) -> bool:
        return bool(re.search(r'\d', self.password))

    def check_symbol(self) -> bool:
        return bool(re.search(r'[@!$#*]', self.password))

    def evaluate_strength(self) -> str:
        """
        Evalúa y clasifica la fortaleza de la contraseña:
        - 'Débil'  : menos de 8 caracteres o muy pocos requisitos cumplidos.
        - 'Media'  : cumple longitud mínima y 2 requisitos.
        - 'Fuerte' : cumple longitud mínima y al menos 3 requisitos.
        """

        self.requirements_met = sum([
            self.check_uppercase(),
            self.check_lowercase(),
            self.check_digit(),
            self.check_symbol()
        ])
        # Penaliza si la longitud es menor al mínimo
        if not self.has_min_length():
            self.requirements_met = max(0, self.requirements_met - 1)

        if self.requirements_met >= 3:
            return 'Fuerte'
        elif self.requirements_met == 2:
            return 'Media'
        else:
            return 'Débil'


def main():
    """Función principal para ejecutar el verificador desde la terminal."""
    password = input("🔐 Ingrese su contraseña: ")
    checker = PasswordChecker(password)
    strength = checker.evaluate_strength()
    print(f"\n✅ Su Contraseña es: {strength}")


if __name__ == "__main__":
    main()
