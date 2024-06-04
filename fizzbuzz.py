
def process(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n

def get_fizzbuzz_list():
    return [process(i) for i in range(1, 101)]

def fizzbuzz():
    L = get_fizzbuzz_list()
    for number in range(1, 101):
        print(L[number])
