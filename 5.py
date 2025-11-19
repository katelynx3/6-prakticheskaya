x1, y1 = map(int, input("Введите координаты ладьи через пробел ").split())
x2, y2 = map(int, input("Введите координаты хода ладьи через пробел ").split())
if (abs(x2-x1) == abs(y2-y1) or (x1 == x2) or (y1 == y2)):
    print('yes')
else:
    print('no')
неанлеарпапрлп
