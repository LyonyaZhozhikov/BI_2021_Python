# 3

# randomly changes the output of function
import random
import requests


def rus_roul(probability=None, return_value=None):
    def decorator(func):
        def inner_rus(*args,  **kwargs):
            if random.random() < probability:
                return return_value
            else:
                return func(*args,  **kwargs)
        return inner_rus
    return decorator


@rus_roul(probability=0.5, return_value="Oops, I did it again")
def make_request(url):
    return requests.get(url)


for _ in range(10):
    print(make_request("https://google.com"))
