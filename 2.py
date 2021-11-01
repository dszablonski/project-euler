class Fibonacci:
    def __iter__(self):
        self.a = 1
        self.previous_number = 0

        return self

    def __next__(self):
        if self.a < 4000000:
            if self.a == 1:
                result = self.a + 1
            else:
                result = self.a + self.previous_number
            self.previous_number = self.a
            self.a = result

            return result
        else:
            raise StopIteration


fib = Fibonacci()
sequence = iter(fib)
ans = 0

for i in sequence:
    if not bool(i % 2):
        ans += i
    else:
        continue

print(ans)
