line = input("Введите элементы списка через пробел: ").split()
positive = 0
negative = 0
zero = 0

for element in line:
    try:
        # Приводим к int для математического сравнения
        if int(element) < 0:
            negative += 1
        elif int(element) > 0:
            positive += 1
        else:
            zero += 1
    except ValueError:
        # Если в введенном списке есть элемент с ошибкой,
        # даем пользователю ввести этот элемент повторно
        print(f"Элемент списка: {element} некорректен, введите его повторно")
        line.append(input("Введите элемент списка: "))

print(f"Число положительных чисел в списке: {positive}")
print(f"Число отрицательных в списке: {negative}")
print(f"Число нулей в списке: {zero}")

#Код писал сам, проверял на соответствие PEP 8 через Deepseek