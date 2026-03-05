# import sys
# sys.path.append("../src")
#TODO make it with pip install math_demmo

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не их отствие
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты не должны дублировать логику тестируемого кода
# тесты должны покрывать "класстеры" входных параметров
# Тесты должны обнаруживать новые ошибки, использование одних и тех же типов данных может препятствовать этому
# Тестовые функции должны тестировать логические блоки
# тесты покрывают как успешные так и ошибочные кейсы

from math_demo import add, add_with_bug, calculate_tax_bugged, calculate_tax

def test_addition():
    assert add(2,2)==4
    print("Test ADDITION PASSED")

def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их отсутстиве 
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    print("Test ADDITION PASSED")
    # finally we found error 
    # assert add_with_bug(7,6) == 13

def test_addition_duplicate():
    assert add(6,7) == 6 + 7
    print("Test DUPLICATION ADDITION PASSED")

def test_addition_overkill():
    for i in range(0,2**32):
        for j in range(0, 2**32):
            assert add(i,j) == i +j
            assert add(-i,j) == -i + j
            assert add(-i, -j) == -i-j
            assert add(i, -j) == i -j

def test_addition_clussters():
    assert add(7,6) == 13
    assert add(0,6) == 6
    assert add(7,0) == 7
    assert add(10,-11) == -1
    assert add(-10,-11) == -21
    assert add(-5,0) == -5
    assert add(0, -2) == -2
    assert add(9,5) == 14
    assert add(5,5) == 14 
    print("test CLUSTERS PASSED")

def test_tax_calculator_pasticide():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("Test TAX CALCULATOR PASSED")
    assert calculate_tax_bugged(2.340) == 0.35

def test_tax_calculate():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("Test UNGUDDED TAX CALCULATOR PASSED")
    assert calculate_tax_bugged(2.340) == 0.35

def test_addition_commutative():
    assert add(9,5) == 14
    assert add(5.9) == 14
    print("Test COMMUTATIVE PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    test_addition_overkill()
    test_addition_commutative()
    test_tax_calculator_pasticide()