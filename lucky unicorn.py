import random

#Integer checking function below
def intcheck(question, low, high):
  valid = False
  while not valid:
    error = "Whoops! Please enter an integer between {} and {}.".format(low, high)

    try:
      response = int(input("Enter an integer between {} and {}: ".format(low, high)))

      if low <= response <= high:
        return response
      else:
        print(error)
        print()

    except ValueError:
      print(error)

#main routine goes here



 #Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money do you want to play with? ",1, 10)

keep_going = ""
while keep_going == "":

  #Tokens list includes 10 items to prevent too many unicorns being chosen
  tokens = ["horse", "horse","horse",
  "zebra","zebra","zebra",
  "donkey","donkey","donkey",
  "lion", "lion","lion",
  "monkey", "monkey",
  "unicorn","unicorn"]

  #Randomly choose a token from list above
  token = random.choice(tokens)
  print()
  print("You got a {}".format(token))

  #Adjust balance based on the chosen token and generate feedback
  if token == "unicorn":
    balance += 4
    feedback = "Congratulations you won $5.00."
  elif token == "donkey":
    balance -= 1
    feedback = "Sorry, you did not win anything this round."
  elif token == "monkey":
    balance -= 2
    feedback = "sorry, you did not win anything this round XD"
  else:
    balance -= 0.5
    feedback = "Congratulation you won 50c."

  print()

  print(feedback)
  print("You have ${:.2f} to play with".format(balance))


  if balance <1:
    print("Sorry, you don't have enough money to continue. Gave over.")
    keep_going = "end"
  else:
    keep_going = input("Press <enter> to play again or any other key to quit.")

#Farewell user at end of game
print("have a nice day. Thank you for playing this game ")
