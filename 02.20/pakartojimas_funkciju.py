# Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
# Print first Name with age;
# And then print all arguments with key arguments.


def print_age_name_arguments(age: int , name: str ="Antanas", *args , **kwargs) -> None:
    print(name , age)
    print(age , name , args if args  else "" , kwargs if kwargs else "")


print_age_name_arguments(1 , "da", "asd", "adsad" , vardas="Danielius", tsg="mldc")

print_age_name_arguments(1 , "da")


