num  = 10
life = 3


while life > 0:
    guess = int(input('Enter an integer : '))
    if guess == num:
        print('You Win!')
        break
    life -= 1
    if life == 0:
        print('Sorry you failed!')
        break
  