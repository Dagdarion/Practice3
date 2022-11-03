x = 24

print("Плохо" if x % 2 == 1 else
      "Неплохо" if (2 <= x <= 5) and (x % 2 == 0) else
      "Так себе" if (6 <= x <= 20) and (x % 2 == 0) else
      "Отлично")