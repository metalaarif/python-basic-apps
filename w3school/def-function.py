def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)
main()