# 2

# logging input and output type
def function_logging(func):
    def inner_log(*args, **kwar):
        result = func(*args, **kwar)
        if args and kwar:
            print(f"Function {func.__name__} is called with positional arguments: {args} and keyword argument:",
                  ", ".join(f'{key}={value}' for key, value in kwar.items()))
        elif args:
            print(f"Function {func.__name__} is called with positional arguments: {args}")
        elif kwar:
            print(f"Function {func.__name__} is called with keyword argument:",
                  ", ".join(f'{key}={value}' for key, value in kwar.items()))
        else:
            print(f"Function {func.__name__} is called with no arguments")
        print(f"Function {func.__name__} returns output of type {type(result).__name__}")
        return result

    return inner_log


@function_logging
def func1():
    return set()


@function_logging
def func2(a, b, c):
    return (a + b) / c


@function_logging
def func3(a, b, c, d=4):
    return [a + b * c] * d


@function_logging
def func4(a=None, b=None):
    return {a: b}


print(func1(), end="\n\n")
print(func2(1, 2, 3), end="\n\n")
print(func3(1, 2, c=3, d=2), end="\n\n")
print(func4(a=None, b=float("-inf")), end="\n\n")
