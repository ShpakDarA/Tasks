import numpy as np
def read_coordinates_from_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            # Разделяем строку на две части и преобразуем в float
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

file_path = 'file2.txt'
coordinates_list = read_coordinates_from_file(file_path)
#print(coordinates_list)
number_of_points = len(coordinates_list)
#print("num ", number_of_points)
center = []
# Открываем файл для чтения
with open('file1.txt', 'r') as file:
    # Считываем первую строку с координатами
    line1 = file.readline().strip()
    # Считываем вторую строку с радиусом
    line2 = file.readline().strip()
    # Разделяем первую строку на части и преобразуем в float
    x_center, y_center = map(float, line1.split())
    center.append((x_center, y_center))
    # Преобразуем радиус в float
    radius = float(line2)

#print("center ", center)
#print("radius ", radius)

res = np.zeros(number_of_points)
for i in range (number_of_points):
    x_c, y_c = center[0]
    x, y = coordinates_list[i]
    xtmp = abs(x_c - x)
    ytmp = abs(y_c - y)
    dist = np.sqrt(xtmp**2+ytmp**2)
    if (dist==radius):
        res[i]=0
    if (dist<radius):
        res[i] = 1
    if (dist>radius):
        res[i] = 2
    #print(dist)
print("result: ", res)