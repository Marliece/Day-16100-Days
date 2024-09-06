print("Name the Lyrics Game")
print()
print("Fill in the blank lyrics!")
print()
counter = 1
while True:
  lyrics = input("Never going to ______ you up. ")
  if lyrics == "give" or lyrics == "Give":
    print("You got it! Well done! It only took you", counter, "attempts.")
    break
  else:
    print("Nope! Try again!")
    counter +=1
  