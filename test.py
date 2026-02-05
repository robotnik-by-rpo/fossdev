from script import sum_num, div

def test_sum():
    a, b = 1, 2
    result = 3
    assert sum_num(a,b) == result

def test_div():
    a, b = 6, 2
    result = 3
    assert div(a,b) == result

def test_div_zero():
    a, b = 2,0
    try: 
        div(a,b)
        assert("test didn't pass")
    except:
        print("test was passed")

if __name__ == "__main__":
    test_div()
    test_sum()
    test_div_zero()