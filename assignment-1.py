#SECTION 1

name = "Francisco"
age = 44
height = 5.10
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#SECTION 2

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year

print(f"Hi, {name}! You are approximately {age} years old.")


#SECTION 3

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

product = n1 * n2

print(f"{n1} × {n2} = {product}")


#SECTION 4

item = "Python textbook"
price = 27
quantity = 3

total = price * quantity

print("***************************")
print("        RECEIPT")
print("***************************")
print(f"Item:      {item}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("***************************")


#SECTION 5

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
