
def var_input():
    some_var = float(input("Первое число >>> "))
    oper = input("Знак?(+,-,*,/) >>> ")
    any_var= float(input("Второе число >>> "))
    oper = oper.replace(" ", "")
    print()
    return {
    "first_var": some_var,
    "operation": oper,
    "second_var": any_var
    }
