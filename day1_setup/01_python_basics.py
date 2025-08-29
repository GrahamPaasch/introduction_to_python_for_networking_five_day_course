from common.lib.logging_setup import setup_logging

log = setup_logging("day1")

# Simple examples for syntax, data types, flow control, functions

def add(a: int, b: int) -> int:
    return a + b


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


if __name__ == "__main__":
    log.info("add(2,3)=%s", add(2, 3))
    for i in range(1, 6):
        log.info("%s -> %s", i, fizzbuzz(i))
