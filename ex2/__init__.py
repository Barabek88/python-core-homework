from ex2 import fetcher
import time

CALL_COUNT = 20


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def decorator(func):
        def wrapper(url):
            total_time = 0
            i = 0
            while i < num:
                start = time.time()
                func(url)
                end = time.time()
                total_time += end - start
                print(f'Время выполнения вызова к {url}: {end - start} ')
                i += 1
            print(f'Среднее время выполнения: {0 if num == 0 else total_time / num} ')

        return wrapper

    return decorator


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
