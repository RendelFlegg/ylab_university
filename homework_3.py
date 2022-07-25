import time


def cashing_decorator(func):
    """Decorator function to store results in cash."""
    def wrapper(*args, **kwargs):
        key = tuple(arg for arg in args)  # Use tuple of *args as key to increase versatility
        if key in result_dict:
            # print('Достаем значение из словаря')
            return result_dict[key]
        result = func(*args, **kwargs)
        # print('Записываем значение в словарь')
        result_dict[key] = result
        return result
    return wrapper


@cashing_decorator
def multiplier(number: int):
    return number * 2


def param_decorator(call_count: int = 1, start_sleep_time: int = 0, factor: int = 1, border_sleep_time: int = 0):
    """Decorator function to manage function calling and repeating."""
    def repeater(func):
        def wrapper(*args, **kwargs):
            waiting_time = start_sleep_time
            print(f'Количество запусков = {call_count}')
            print('Начало работы')
            for n in range(1, call_count + 1):
                if waiting_time >= border_sleep_time:
                    waiting_time = border_sleep_time
                time.sleep(waiting_time)
                result = func(*args, **kwargs)
                print(f'Запуск номер {n}. Ожидание: {waiting_time} секунд. Результат декорируемой функции = {result}')
                waiting_time *= factor
            print('Конец работы')
        return wrapper
    return repeater


@param_decorator(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=5)
def new_multiplier(number: int):
    return number * 2


result_dict = {}

if __name__ == '__main__':
    print(multiplier(2))
    print(multiplier(5))
    print(multiplier(3))
    print(multiplier(2))
    print('-' * 10)
    new_multiplier(3)
