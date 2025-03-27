print("hello")
answer = input()
while answer.startswith(" "):
    newanswer = answer.removeprefix(" ")
    answer = newanswer
response = answerwer

if response.startswith("h") or response.startswith("H"):
    print("You get $20")
elif response.__contains__("hello") or response.__contains__("Hello"):
    print("You get nothing. Womp Womp.")
else:
    print("you get $100!!!!! Congratulations.")
