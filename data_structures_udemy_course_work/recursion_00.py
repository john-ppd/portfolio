# Recursion is a function that calls itself until it doesn't
# 2 rules for recursion, 1 must be making problem smaller (ie breaking lists in half) 2 must do same thing over and over
ir = 19


def count_down(val):
    # stack overflow is when it becomes an infinite loop
    val -= 1
    if val > 0:
        # this is recursive case
        print(f'val {val} calling function again')
        count_down(val)
    else:
        # this is base case (satisfies recursion)
        print('done recursion ')


def count_better_have_return(val):
    val -= 1
    if val == 0:
        return True
    count_better_have_return(val)


# the way these get called is called a call stack, function in function will complete be4 printing
def funcThree():
    print('func 3')


def funcTwo():
    funcThree()
    # runs after funcThree finishes running
    print('func 2')


def funcOne():
    funcTwo()
    print('func 1')

def factorial(n):
    if n == 1:
        return 1
    # this works because each time it runs it adds it to the call stack and then the return is part of prev return
    return n * factorial(n-1)

print(factorial(6))





# count_down(ir)
# count_better_have_return(ir)
funcOne()
