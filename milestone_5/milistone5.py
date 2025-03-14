from functools import wraps
import inspect
import time
from collections import defaultdict

def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get("user_type") != "admin":
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper

def catch_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__} {e}")
    return wrapper

def check_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        for param, value in bound_args.arguments.items():
            expected_type = sig.parameters[param].annotation
            if expected_type is not inspect.Parameter.empty and not isinstance(value, expected_type):
                raise TypeError(f"Argument {param} must be {expected_type.__name__}, not {type(value).__name__}")
        result = func(*args, **kwargs)
        return_type = sig.return_annotation
        if return_type is not inspect.Signature.empty and not isinstance(result, return_type):
            raise TypeError(f"Return value must be {return_type.__name__}, not {type(result).__name__}")
        return result
    return wrapper

def cache_results(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

def rate_limiter(calls_per_minute):
    interval = 60.0 / calls_per_minute
    call_times = defaultdict(list)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            call_list = call_times[func]
            call_list = [t for t in call_list if now - t < 60]
            if len(call_list) >= calls_per_minute:
                raise RuntimeError("Rate limit exceeded. Try again later.")
            call_list.append(now)
            call_times[func] = call_list
            return func(*args, **kwargs)
        return wrapper
    return decorator

@is_admin
def show_customer_receipt(user_type: str):
    return "Showing customer receipt"

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

@check_types
def add(a: int, b: int) -> int:
    return a + b

@cache_results
def slow_function(x):
    print("Executing slow function...")
    return x * x

@rate_limiter(5)
def limited_function():
    print("Function executed")

try:
    print(show_customer_receipt(user_type='user'))
except ValueError as e:
    print(e)

print(show_customer_receipt(user_type='admin'))

some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})

try:
    print(add(1, 2))
    print(add("1", "2"))
except TypeError as e:
    print(e)

print(slow_function(4))
print(slow_function(4))

for _ in range(7):
    try:
        limited_function()
    except RuntimeError as e:
        print(e)