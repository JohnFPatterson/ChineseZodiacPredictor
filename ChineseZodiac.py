import time
while True:
    YearTarget = int(input("What year do you want to know the lucky Chinese Zodiac for? "))
    YearCurrent = 2020
    X = YearTarget
    Y = 12
    Z = 'Zodiac Animal'
    if X % Y == 0:
        Z = 'Monkey'
    elif X % Y == 1:
        Z = 'Rooster'
    elif X % Y == 2:
        Z = 'Dog'
    elif X % Y == 3:
        Z = 'Pig'
    elif X % Y == 4:
        Z = 'Rat'
    elif X % Y == 5:
        Z = 'Ox'
    elif X % Y == 6:
        Z = 'Tiger'
    elif X % Y == 7:
        Z = 'Rabbit'
    elif X % Y == 8:
        Z = 'Dragon'
    elif X % Y == 9:
        Z = 'Snake'
    elif X % Y == 10:
        Z = 'Horse'
    elif X % Y == 11:
        Z = 'Goat'
    else:
        print('Enter numbers only')
    if YearTarget < YearCurrent:
        print(str(X) + ' was the Year of the ' + Z)
    elif YearTarget == YearCurrent:
        print(str(X) + ' is the Year of the ' + Z)
    elif YearTarget > YearCurrent:
        print(str(X) + ' will be the Year of the ' + Z)
    time.sleep(0.5)
    print(" ")

