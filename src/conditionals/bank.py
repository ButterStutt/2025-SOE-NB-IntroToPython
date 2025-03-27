print("Hello")
answer = input()
something = answer.replace(" ", "")
response = str.lower(something)

# testing what the returned value is
# print(response)

if response.startswith("hello"):
    print("You get nothing. Womp Womp.")
elif response.startswith("h"):
    print("You get $20")
else:
    print("you get $100!!!!! Congratulations.")
