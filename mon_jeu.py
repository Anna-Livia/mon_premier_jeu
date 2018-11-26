import random
target = random.randint(1, 100)


still_playing = True
while still_playing: 
  print("Voulez vous jouer ?")
  print ("Pressez A pour jouer, et Q pour quitter")
  game_status = input()
  if game_status in ["A", "a"]:
    still_guessing = True
    while still_guessing :
      guess = int(input("Devine un chiffre "))
      if guess < target : 
        print("Trop petit")
      elif guess > target : 
        print("Trop grand")
      else :
        still_guessing = False
        print("Bravo")
  if game_status in ["Q", "q"]:
    still_playing = False
