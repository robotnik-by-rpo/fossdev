def sum(a: int, b: int):
    return a+b

def div(a: int, b: int):
    if b != 0:
        raise ValueError("Denom is zero")
    return a/b