name = input("What is your name? ")
home = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fact = input("Tell me a fun fact: ")
yob = int(input("What year were you born? "))

age = 2026 - yob

print("")
print("****** PROFILE CARD ******")
print(f"Name     : {name}")
print(f"Hometown : {home}")
print(f"Hobby    : {hobby}")
print(f"Fun fact : {fact}")
print(f"Age      : {age}")
print("**************************")
