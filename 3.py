x1,y1 = map(int, input('Введите координаты первой клетки через пробел ').split())
x2,y2 = map(int, input('Введите координаты второй клетки через пробел ').split())
def color_calc(x,y):
    if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
        color = 'черный'
    else:
        color = 'белый'
    return color
if color_calc(x1,y1) == color_calc(x2,y2):
    print('yes')
else:
    print('no')
