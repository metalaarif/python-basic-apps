# a = int(input("Enter a number: "))  # any error which prevents code execution is error
# print(a)    # errors triggred at runtime is knowns as exception

def square(n):
    try:
        assert isinstance(n, int), "Invalid type encountered"   # if the condition in assert is true move ahead else tigger the assertion exception
        assert n < 10, "Number must be less than 10"        # assert used for validation
        print((n) ** 2)
    except ValueError as V:
        print("Invalid value provided to function")
    except TypeError as T:
        print("Exception Triggred due to Invalid Operands")
    except AssertionError as e:
        print(e.args)
    except Exception as e:
        print("Exception Triggred " + str(e.args))
    else:   # this block will be executed if no exception is triggered
        print("Program executed Successfully")
    finally:    # this would be executed irrespective of the exception
        print("Exception Triggered, please check the inputs properly")

square(19)