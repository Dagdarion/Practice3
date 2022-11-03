x = 7

print("Fizz Buzz" if (x % 5 == 0) and (x % 3 == 0) else
       "Buzz" if x % 5 == 0 else
       "Fizz" if x % 3 == 0 else
       str(x))
