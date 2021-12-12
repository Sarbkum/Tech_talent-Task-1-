import random

jokes = ("How does the ocen say hi?It waves","What do birds give out on Halloween?Tweets","Where did the music teacher leave her keys?In the piano")
user = random.choices(jokes, k=1)
num = input("Enter number between 1 and 100")

if(num):
 print(user)

