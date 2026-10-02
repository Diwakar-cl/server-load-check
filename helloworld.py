name = "DIwakar"
age = 20
grade = 13

print(name)
print(age)
print(grade)

print("My name is ", name, "My age is ", age, "I am in grade ",grade)

a = 2
b = 3
print(a  + b)
total = a+b
print(total)

print(f"MY name is {name}")
servers =["WEB", "FORM"]
print(servers)

i=10

if i>10:
    print("Hello")
else:
    print("NO")


try:
    iso_num = float(input("Enter you iso number:"))

except ValueError:
    print("This is not a number.Try again.")
    exit()
print(iso_num)

if iso_num>10:
    print("High")
elif iso_num < 10:
    print("Low")
else:
    print("Balanced")