A = input("Введіть рядок: ")
B = input("Введіть символ: ")
count = 0
for char in A:
    if char == B:
        count += 1
print("Кількість входжень символу", B, "в рядок:", count)
