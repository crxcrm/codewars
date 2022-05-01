# I love Fibonacci numbers in general, but I must admit I love some more than others.

# I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]
    
def nth_fib(n):
    fibonacci_of = Fibonacci()
    return fibonacci_of(n-1)
