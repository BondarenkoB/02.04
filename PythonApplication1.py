s = input("Введіть рядок: ")
letters = 0
digits = 0
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("Кількість літер:", letters)
print("Кількість цифр:", digits)

