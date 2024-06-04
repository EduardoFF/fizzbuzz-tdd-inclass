from fizzbuzz import process, get_fizzbuzz_list

def test_number_one():
    assert process(1) == 1

def test_number_simple_numbers():
    assert process(2) == 2
    assert process(44) == 44

def test_multiple_of_three():
    assert process(3) == 'Fizz'
    assert process(6) == 'Fizz'
    assert process(9) == 'Fizz'


def test_multiple_of_five_just_buzz():
    assert process(5) == 'Buzz'
    assert process(10) == 'Buzz'

def test_multiple_of_15():
    assert process(15) == "FizzBuzz"
    assert process(30) == "FizzBuzz"

def test_fizzbuzz_islist():
    assert isinstance(get_fizzbuzz_list(),list)

def test_fizzbuzz_list_has_len_100():
    assert len(get_fizzbuzz_list()) == 100

def test_fizzbuzz_list_first_15():
    L = get_fizzbuzz_list()
    assert L[:15] == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz','Fizz',14,'FizzBuzz']
