import re

class PasswordStrengthMeter:
    def __init__(self, password):
        self.password = password
        self.strength = self.calculate_strength()

    def calculate_strength(self):
        strength = 0

        # 1-8 harflar
        if re.search(r"[a-zA-Z]", self.password):
            strength += 1

        # 1-8 raqamlar
        if re.search(r"\d", self.password):
            strength += 1

        # 1-8 maxsus belgilar
        if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", self.password):
            strength += 1

        # 8 dan uzun
        if len(self.password) >= 8:
            strength += 1

        return strength

    def get_strength(self):
        if self.strength == 4:
            return "Zarur"
        elif self.strength == 3:
            return "Kamyaqin"
        elif self.strength == 2:
            return "O'rta"
        else:
            return "Kam"

password = input("Parolni kiriting: ")
meter = PasswordStrengthMeter(password)
print("Parol kuchi:", meter.get_strength())
