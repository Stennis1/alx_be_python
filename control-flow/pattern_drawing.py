
user_prompt = int(input("Enter the size of the pattern: "))

row = 0
while row < user_prompt:
    for i in range(user_prompt):
        print("*", end="")
    print()
    row += 1
    