from ._fizzbuzz import fizzbuzz

def check_fizzbuzz(value, exp_out):
    ret_val = fizzbuzz(value)
    assert ret_val == exp_out

class TestFizzBuzz:
    def test_call_fizzbuzz(self):
        fizzbuzz(1)

    def test_1_with_1_passed_in(self):
        check_fizzbuzz(1, "1")

    def test_2_with_2_passed_in(self):
        check_fizzbuzz(2, "2")

    def test_fizz_with_3_passed_in(self):
        check_fizzbuzz(3, "fizz")

    def test_buzz_with_5_passed_in(self):
        check_fizzbuzz(5, "buzz")

    def test_fizz_with_multiple_3(self):
        check_fizzbuzz(6, "fizz")

    def test_buzz_with_multiple_5(self):
        check_fizzbuzz(10, "buzz")

    def test_fizzbuzz_with_multiple_3_5(self):
        check_fizzbuzz(15, "fizzbuzz")
