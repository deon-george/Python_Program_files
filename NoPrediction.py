import random
import time
import sys


def loading(text):
    for i in range(3):
        sys.stdout.write(text + "." * (i + 1) + "\r")
        sys.stdout.flush()
        time.sleep(0.2)
    print(" " * 30)


def success_animation():
    print("Checking answer", end="")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.1)

    print("\n")
    print("🎉🥳🥳 Correct!!! 🎉🥳🥳")

    for i in range(3):
        print("★ " * (i))
        time.sleep(0.1)

  #  print("You win!\n")


def wrong_animation():
    print("Checking", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print()


print("=== Number Guessing Game ===")
loading("Starting game")

secret = random.randint(1, 30)
attempts = 0

while True:
    guess = int(input("Enter number (1-30): "))
    attempts += 1

    wrong_animation()

    if guess < secret:
        print("Too small!\n")

    elif guess > secret:
        print("Too big!\n")

    else:
        success_animation()
        print("Attempts:", attempts)
        break
if attempts <3:
    print ('🔥🔥your are Legend 🔥🔥')
elif 3<=attempts<=5:
    print ('your are Hero 😎😎') 
else: 
    print (' your are Noob🤣🤣 ')