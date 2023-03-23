import os


USER = os.environ.get("USER", "Not Set")
TOKEN = os.getenv("TOKEN")



print(USER)
print(TOKEN)
print(type(USER))
print(type(TOKEN))



os.environ["password"] = "326"

print(os.getenv("password"))

