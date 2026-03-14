import random

def randomNum():
    myNum = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20')
    for guessestaken in range(1, 7) :
      print('take a guess')
      yourNum = int(input())
      if yourNum < myNum :
        print('Your guess is to low')
      elif yourNum > myNum :
       print('Your guess is to high')
      else:
       break
    if yourNum == myNum :
      print('Good job! You guessed my number in ' + str(guessestaken) + ' guesses!') 
    else :
      print('Nope. The number i was thinking of was ' + str(myNum))
    
randomNum()