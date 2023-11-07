def divide(a, b):
    try:
        return (int(a)**2)/int(b)
    except ValueError:
        print("Error: Input numbers")
    except ZeroDivisionError:
        print("Error: division by 0")


num_1 = input("Input a:\n")
num_2 = input("Input b:\n")
print(divide(num_1, num_2))
