import os
os.system('clear')

tictactoe = (
"""
 1|2|3
 4|5|6
 7|8|9
"""
)





# t = input("Pick a number: ")
# location = tictactoe.find(str(t))

# print("Number location: " + str(location))





# xMove = str(input("X, Pick a spot on the board: "))
# oMove = str(input("O, Pick a spot on the board: "))

# tictactoe = tictactoe.replace(xMove,"d")

i = range(1,2)
sContinue = input("Would you like to play? (y/n): ")

if sContinue == n:
    pass

# if sContinue == n:
    

rules = input("would you like to see the rules? (y/n): ")
if rules == "y":
    print("""
        1. Decide who will be X, and who will be Y
        2. X goes first
        3. To pick a tile on the board, enter the number associated with it and press enter
        4. Whoever gets three in a row first wins

            """)
else:
    pass
print(tictactoe)


while sContinue == "y" :
    xMove = str(input("X, Pick a spot on the board: "))
    if xMove == 'r':
        sContinue = 'r'
    else:
        pass

    tictactoe = tictactoe.replace(xMove,"X")

    os.system('clear')
    print(tictactoe)
    

    oMove = str(input("O, Pick a spot on the board: "))
    if oMove == 'r':
        sContinue = 'r'
    else:
        pass

    tictactoe = tictactoe.replace(oMove,"O")
    os.system('clear')
    print(tictactoe)
    
    
x = 234234
x = "asdfd"
