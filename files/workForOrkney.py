import random
min=1
max=10

def start(x, y) :
  number=random.randint(x, y)
  global number
  lives=3
  min=x
  max=y
  global lives
  main()
  
def main() :
  print "Im thinking of a number from",(min),"to",(max),"\nYou have",(lives),"trys to guess the number im thinking of...\n"
  answer=raw_input()
  int(answer)
  if (answer == number) :
    print "Correct!! The number I was thinking of was",(number),"\n\nType 'y' to play agein, and type n to end game...\n\n"
    answer=raw_input()
    if (answer == "y" or answer == "Y"):
      start(1, 10)
    else:
      print "Thank you for playing!!!"
  else :
    print "Sorry, but",(answer),"is not the number im thinking of...\n"
    global lives 
    lives = (lives - 1)
    if (lives <= 0) :
      print "Game Over!!! Im sorry but the number I was thinking of was",(number),"\n\nType 'y' to play agein, and type n to end game...\n\n"
      answer=raw_input()
      if (answer == "y" or answer == "Y"):
        start(1, 10)
      else:
        print "Thank you for playing!!!"
    elif (lives > 0) :
      main()
  

start(1, 10)