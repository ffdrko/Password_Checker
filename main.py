# Password checking program

user_name = input("Enter your name:").strip()
password = input("Enter your password:").strip()

if user_name == "Fahim" and password == "ffd":

    print(f"Welcome back,{user_name}")
else:
    print("Wrong password")