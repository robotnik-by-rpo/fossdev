def sum(a: int, b: int)->int:
    return a+b

def div(a: int, b: int)->int:
    if b != 0:
        raise ValueError("Denom is zero")
    return a/b