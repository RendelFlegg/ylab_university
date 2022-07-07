import math
import itertools
import re


def find_distance(first_point, second_point):
    """Return the distance between two points"""
    return math.sqrt((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)


def find_total_distance(list_of_points, best=False):
    """Return the distance total distance of consistent travel from one point to another from the list"""
    result = 0
    idx = 0
    route_render = [str(list_of_points[0])]
    while idx < len(list_of_points) - 1:
        result += find_distance(list_of_points[idx], list_of_points[idx + 1])
        if best:
            route_render.append(f'{list_of_points[idx + 1]}[{result}]')
        idx += 1
    if best:
        return ' -> '.join(route_render) + f' = {result}'
    return result


def get_combinations(list_of_points):
    """Return the list of all possible combinations of items of the given list"""
    list_of_combinations = []
    for combination in itertools.product(list_of_points, repeat=len(list_of_points)):
        if len(combination) == len(set(combination)):  # Get rid of combination with duplicates
            list_of_combinations.append(combination)
    return list_of_combinations


def get_routes(list_of_points):
    """Return list of points as route, ending in starting point"""
    list_of_routes = []
    post_office, *list_of_points = list_of_points
    for combination in get_combinations(list_of_points):
        list_of_routes.append([post_office, *combination, post_office])
    return list_of_routes


def find_best_route(list_of_points):
    """Return the route with minimal distance"""
    route_dictionary = {}
    for route in get_routes(list_of_points):
        route_dictionary[tuple(route)] = find_total_distance(route)
    route_dictionary = sorted(route_dictionary.items(), key=lambda item: item[1])
    return list(route_dictionary[0][0])


def check_input(user_input):
    """Return list of tuples if user input passes checks"""
    if user_input == 'test':
        return [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    pattern = r',* *(\d+\, \d+)+,* *'
    list_of_points = []
    for item in re.findall(pattern, user_input):
        x, y = item.split(', ')
        list_of_points.append((int(x), int(y)))
    if len(list_of_points) < 3:
        print('Для того, чтобы это имело смысл нужно минимум три адреса.')
    else:
        return list_of_points


def menu():
    """Main menu"""
    print('Добро пожаловать в программу для вычисления кратчайшего пути почтальона.')
    while True:
        list_of_points = None
        while not isinstance(list_of_points, list):
            print('Введите список адресов, разделенных запятой. '
                  'Первый адрес - почтовое отделение; формат адреса - (x, y).')
            print('Для тестового списка адресов ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3)) введите "test".')
            list_of_points = check_input(input())
        best_route = find_best_route(list_of_points)
        print(find_total_distance(best_route, best=True))
        user_input = None
        while user_input not in ('1', '2'):
            user_input = input('Хотите проверить другие адреса? 1 - "Да", 2 - "Нет".\n')
        if user_input == '2':
            break
    print('Всего хорошего!')


if __name__ == '__main__':
    menu()
