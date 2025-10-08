
class TemplateClass:
    '''
    __init__(self, *args, **kwargs): Constructor method called when an instance is created.
    __str__(self): Defines the string representation of an object for print and str.
    __repr__(self): Defines the official string representation of an object, typically used for debugging.
    __del__(self): Destructor method called when an object is about to be destroyed.
    __len__(self): Called by the len() function to determine the length of an object.
    __getitem__(self, key): Defines behavior for accessing an item, e.g., obj[key].
    __setitem__(self, key, value): Defines behavior for setting an item, e.g., obj[key] = value.
    __delitem__(self, key): Defines behavior for deleting an item, e.g., del obj[key].
    __iter__(self): Returns an iterator object, used in for loops.
    __next__(self): Returns the next item from an iterator.
    __contains__(self, item): Called by the in operator to check membership.
    __call__(self, *args, **kwargs): Makes an instance callable like a function.
    __enter__(self): Called when entering a context (with statement).
    __exit__(self, exc_type, exc_val, exc_tb): Called when exiting a context (with statement).
    __add__(self, other): Defines behavior for the + operator.
    __sub__(self, other): Defines behavior for the - operator.
    __mul__(self, other): Defines behavior for the * operator.
    __truediv__(self, other): Defines behavior for the / operator.
    __floordiv__(self, other): Defines behavior for the // operator.
    __mod__(self, other): Defines behavior for the % operator.
    __pow__(self, other, modulo=None): Defines behavior for the ** operator.
    __eq__(self, other): Defines behavior for the == operator.
    __ne__(self, other): Defines behavior for the != operator.
    __lt__(self, other): Defines behavior for the < operator.
    __le__(self, other): Defines behavior for the <= operator.
    __gt__(self, other): Defines behavior for the > operator.
    __ge__(self, other): Defines behavior for the >= operator.
    __hash__(self): Defines the hash value for the object, used in hash tables and by the hash() function.
    __bool__(self): Defines the boolean value of the object, used by the bool() function and in conditional expressions.
    '''
    def __init__(self, *args, **kwargs):
        # Constructor
        pass

    def __str__(self):
        # String representation
        pass

    def __repr__(self):
        # Official string representation
        pass

    def __del__(self):
        # Destructor
        pass

    def __len__(self):
        # Length
        pass

    def __getitem__(self, key):
        # Get item
        pass

    def __setitem__(self, key, value):
        # Set item
        pass

    def __delitem__(self, key):
        # Delete item
        pass

    def __iter__(self):
        # Iterator
        pass

    def __next__(self):
        # Next item in iteration
        pass

    def __contains__(self, item):
        # Contains
        pass

    def __call__(self, *args, **kwargs):
        # Callable
        pass

    def __enter__(self):
        # Entering a context
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Exiting a context
        pass

    def __add__(self, other):
        # Addition
        pass

    def __sub__(self, other):
        # Subtraction
        pass

    def __mul__(self, other):
        # Multiplication
        pass

    def __truediv__(self, other):
        # True division
        pass

    def __floordiv__(self, other):
        # Floor division
        pass

    def __mod__(self, other):
        # Modulus
        pass

    def __pow__(self, other, modulo=None):
        # Exponentiation
        pass

    def __eq__(self, other):
        # Equality
        pass

    def __ne__(self, other):
        # Not equal
        pass

    def __lt__(self, other):
        # Less than
        pass

    def __le__(self, other):
        # Less than or equal
        pass

    def __gt__(self, other):
        # Greater than
        pass

    def __ge__(self, other):
        # Greater than or equal
        pass

    def __hash__(self):
        # Hash value
        pass

    def __bool__(self):
        # Boolean value
        pass

def setParams(instance, local_vars, exclude=('self',)):
    for name, value in local_vars.items():
        if name not in exclude: setattr(instance, name, value)

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

def swap(a,b):
    return b,a

def slice(a, start=0, stop=None, step=1) -> list:
    stop = stop or len(a)
    return a[start:stop:step]

def linspace(a, b, num):
    if num < 2:
        return [a]
    step = (b - a) / (num - 1)
    return [a + i * step for i in range(num)]

def main(argc: int, *argv: str) -> int:
    
    return 0

if __name__ == '__main__':
    argv = __import__("sys").argv
    exit(main(len(argv), *argv))
