print("Give me Math")
math = input()
x, y, z = math.split(" ")

# Testing outputs
# print(math.split(" "))
# print(x)
# print(y)
# print(z)

if y == "+":
    answer = int(x) + int(z)
elif y == "-":
    answer = int(x) - int(z)
elif y == "*":
    answer = int(x) * int(z)
elif y == "/":
    if z == "0":
        answer = "n/a"
    else:
        answer = int(x) // int(z)
else:
    answer = "n/a"
print(answer)
