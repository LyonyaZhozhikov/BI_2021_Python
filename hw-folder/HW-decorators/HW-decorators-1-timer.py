# 1

# substitute return on time of its process
import time


def measure_time(func):
    def inner_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} has finished in {end - start} second")
        return result

    return inner_time


@measure_time
def some_func(a, b, c, d, e=8, f=2, g='3'):
    time.sleep(a)
    time.sleep(b)
    time.sleep(c)
    time.sleep(d)
    time.sleep(e)
    time.sleep(f)
    return g


if __name__ == "__main__":
    some_func(1, 2, 3, 4, e=5, f=6, g='99999')  # check, 21 sec indeed
