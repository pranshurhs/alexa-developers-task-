import random

player_score = 0
computer_score = 0

while True:
    print("\n     play stone paper scissors     ")
    print("1. stone")
    print("2. paper")
    print("3. scissors")
    print("4. exit from game")

    try:
        player_choice = int(input("enter your pick from the three options: "))
    except ValueError:
        print("invalid option, please select a valid number")
        continue

    if player_choice == 4:
        print("\n    final score     ")
        print("player:", player_score)
        print("computer:", computer_score)
        print("game over")
        break

    if player_choice < 1 or player_choice > 3:
        print("invalid option, please select a valid number")
        continue

    computer_choice = random.randint(1, 3)

    choices = {
        1: "stone",
        2: "paper",
        3: "scissors"
    }

    print("\nyour choice:", choices[player_choice])
    print("computer's choice:", choices[computer_choice])

    if player_choice == computer_choice:
        print("result: draw")

    elif ((player_choice == 1 and computer_choice == 3) or
          (player_choice == 2 and computer_choice == 1) or
          (player_choice == 3 and computer_choice == 2)):

        print("result: you won")
        player_score += 1

    else:
        print("result: you lost")
        computer_score += 1

    print("\n     score right now       ")
    print("player:", player_score)
    print("computer:", computer_score)

    play_again = input("\nplay again? yes/no: ").lower()

    if play_again == "no":
        print("good game")
        break

    elif play_again == "yes":
        continue

    else:
        print("invalid option")
        break