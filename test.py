from script import sum_num, div

def test_sum():
    a, b = 1, 2
    result = 3
    assert sum_num(a,b) == result

def test_div():
    a, b = 6, 2
    result = 3
    assert div(a,b) == result


if __name__ == "__main__":
    test_div()
    test_sum()