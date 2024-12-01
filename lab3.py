import matplotlib.pyplot as plt
import numpy as np

# Функція для зчитування координат
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

# Функція для обчислення векторного добутку, що визначає орієнтацію трьох точок
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Алгоритм Ендрю для обчислення опуклої оболонки
def andrew_algorithm(points):
    points = sorted(points)
    # Створюємо нижню оболонку
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    # Створюємо верхню оболонку
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Відкидаємо останні точки з кожної оболонки, оскільки вони дублюються
    return lower[:-1] + upper[:-1]

# Функція для малювання точок та опуклої оболонки
def plot_points(points, convex_hull_points):
    plt.figure(figsize=(9.6, 5.4))
    plt.xlim(0,960)
    plt.ylim(0,540)
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, color='orange')
    # Малюємо опуклу оболонку
    convex_hull_points = np.array(convex_hull_points)
    plt.plot(np.append(convex_hull_points[:, 0], convex_hull_points[0, 0]), 
            np.append(convex_hull_points[:, 1], convex_hull_points[0, 1]), 
            color='blue', linewidth=2)
    plt.savefig("convex_hull_output_image.png")

# Виклик програми
if __name__ == "__main__":
    dataset_file = 'DS5.txt'  
    points = read_dataset(dataset_file)
    convex_hull_points = andrew_algorithm(points)
    plot_points(points,convex_hull_points)
