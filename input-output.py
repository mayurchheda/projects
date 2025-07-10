name = input("please enter your name:")
print("Hello, " + name + "!")
age_str = input("How old are you? ")
age = int(age_str)
age = 100+age
print(f"What! You are {age} years old!!! I can't believe it")
print("I am just kidding, you are not that old!")

friends = []
n = input("How many friends do you have? (max 10): ")
n = int(n)
if n > 10:
    print("You can only enter up to 10 friends.")
    n = 10
elif n < 1:
    print("I am sure you have at least one friend.")
    n = 1
m=n
while n>0:
   
    friend_name = input(f"Enter the name of your friend and Press Enter to continue ({m-n+1}/{m}): ")
    friends.append(friend_name)
    if n == round(m/2 +0.5):
        print("You are halfway there!")
    elif n == 1:
        print("You made it to the end!")
    n -= 1
print("Your friends are:")
print(", ".join(friends))
best_friend_name = input("Who is your best friend? Type Name and press Enter to continue:")
print(f"Your best friend is {best_friend_name}!")
print("Your remaining friends are:")
for friend in friends:
    if friend != best_friend_name:
        print(friend)
print("Thank you for sharing your friends with me!")
print("Have a great day, " + name + "!")
print("Goodbye!")