import calc
import echo


a = 5
b = 20
c = 10


# print(f"__name__ is {__name__}")

print(calc.add(a, b))
print(calc.div(a, b))
print(calc.prod(a, b))
print(calc.sub(a, b))
print(calc.add_sub_last(a, b, c))

if __name__=='__main__':
    print(f"call from main {__name__}")


print(echo.echo("Stringas DIDELIS", 5))