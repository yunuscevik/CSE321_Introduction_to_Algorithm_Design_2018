import random

def winner(n, m, player1, player2, playerNo=None):
    
    if playerNo is None:
        playerNo = player1
    if(n <= m):
        if playerNo == player1:
            return player1
        else:
            return player2
    
    if(playerNo == player1):
        if(n <= 2*m):
            modRes = n % (m+1)
            return winner((n - modRes), m, player1, player2, player2)
        else:
            return winner((n - (random.randint(1, m))), m, player1, player2, player2)
    else:
        return winner((n - (random.randint(1, m))), m, player1, player2, player1)


def inputValues():
    player1 = str(input("Enter a player1 Name >>> "))
    player2 = str(input("Enter a player2 Name >>> "))
    n = int(input("Enter an integer for n chips in the pile        >>> "))
    m = int(input("Enter an integer for most m chips from the pile >>> "))
    while(n % (m+1) == 0 or n <= m):
        print("\n\"n % (m+1)\" must be not equal to 0\n\t\tOR\nThe n value must be bigger than m value")
        n = int(input("Enter an integer for n chips in the pile        >>> "))
        m = int(input("Enter an integer for most m chips from the pile >>> "))
    return n,m,player1,player2


def main():
    n,m,player1,player2 = inputValues()
    print("Winner is Player " + str(winner(n, m, player1, player2)))

if __name__ == "__main__":
    main()