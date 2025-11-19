x1, y1 = map(int, input("Введите координаты слона через пробел ").split())
x2, y2 = map(int, input("Введите координаты хода слона через пробел ").split())
if abs(x2-x1) == abs(y2-y1):
    print('yes')
else:
    print('no')
