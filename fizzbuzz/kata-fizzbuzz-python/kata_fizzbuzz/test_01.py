from fizzbuzz_01 import FizzBuzz

def test_fizzbuzz_1():
    fizzbuzz = FizzBuzz()
    assert "1" == fizzbuzz.fizzbuzz(1)

def test_fizzbuzz_2():
    fizzbuzz = FizzBuzz()
    assert "2" == fizzbuzz.fizzbuzz(2)

def test_fizzbuzz_3():
    fizzbuzz = FizzBuzz()
    assert "Fizz" == fizzbuzz.fizzbuzz(3)

def test_fizzbuzz_5():
    fizzbuzz = FizzBuzz()
    assert "Buzz" == fizzbuzz.fizzbuzz(5)

def test_fizzbuzz_15():
    fizzbuzz = FizzBuzz()
    assert "FizzBuzz" == fizzbuzz.fizzbuzz(15)
