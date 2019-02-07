class FizzBuzz:

    def __init__(self):
        pass

    def fizzbuzz(self, integer: int) -> str:
        if integer % 15 == 0: return "FizzBuzz"
        if integer %  3 == 0: return "Fizz"
        if integer %  5 == 0: return "Buzz"
        return str(integer)

    def print_it(self) -> None:
        for i in range(1, 101):
            print(self.fizzbuzz(i))


if __name__ == '__main__':

    f = FizzBuzz()
    f.print_it()
