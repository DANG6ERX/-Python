print ('Приветствуем вас в калькуляторе Python')
q1 = int (ввод ('Введите число 1:'))
q2 = int (ввод ('Введите число 2:'))

v = int (input ('Какую операцию вы хотите выполнить? \ n 1 Сложение \ n 2 Вычитание \ n 3 Деление \ n 4 Умножение \ n'))

If v == 1:
    r = q1 + q2
    p = 'сложения'
    t = p
If v == 2:
    r = q1 - q2
    l = 'вычитания'
    t = l
If v == 3:
    r = float (q1 / q2)
    m = 'деления'
    t = m
If v == 4:
    r = q1 * q2
    n = 'умножения'
    t = n
print ('Результат', t, '=', r)
