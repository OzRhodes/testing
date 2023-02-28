'''
print 100 numbers each on a new line
if multiple of 3 print fizz instead of the number
if multiple of 5 print buzz instead of the number
if multiple of both 3 and 5 print fizzbuss instread of the number
'''

def process(number):
    if number %3 == 0 and number %5 == 0 :
        return "FizzBuzz"
    if number %3 == 0:
        return "Fizz"
    if number %5 == 0:
        return "Buzz"
    return number

for number in range(101):
    print(process(number))