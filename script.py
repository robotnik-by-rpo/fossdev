def sum_num(a: int, b: int)->int:
    return a+b

def div(a: int, b: int)->int:
    if b == 0:
        raise ValueError("Denom is zero")
    if isinstance(a,str) or isinstance(b,str):
        raise ValueError("Wrong type")
    if isinstance(a,list) or isinstance(b,list):
        raise ValueError("Could not divide lists")
    return a/b