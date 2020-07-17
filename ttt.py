env={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
continue_game = True
global player
def display_init_board():
    print(' TIC TAC TOE')
    print(' -----------')
    print('   |1|2|3|')
    print('   -------')
    print('   |4|5|6|')
    print('   -------')
    print('   |7|8|9|\n')

def display_board():
  print('   '+'|'+env[1]+'|'+env[2]+'|'+env[3]+'|')
  print('   -------')
  print('   '+'|'+env[4]+'|'+env[5]+'|'+env[6]+'|')
  print('   -------')
  print('   '+'|'+env[7]+'|'+env[8]+'|'+env[9]+'|''\n')

def move(a):
    #check moves
    if a == 1:
        a="TWO"
    else:
        a="ONE"
    if env[1]==env[2]==env[3]=='X' or env[4]==env[5]==env[6]=='X' or env[7]==env[8]==env[9]=='X' or env[1]==env[5]==env[9]=='X' or env[3]==env[5]==env[7]=='X' or env[1]==env[4]==env[7]=='X' or env[2]==env[5]==env[8]=='X' or env[3]==env[6]==env[9]=='X' or env[1]==env[2]==env[3]=='O' or env[4]==env[5]==env[6]=='O' or env[7]==env[8]==env[9]=='O' or env[1]==env[5]==env[9]=='O' or env[3]==env[5]==env[7]=='O' or env[1]==env[4]==env[7]=='O' or env[2]==env[5]==env[8]=='O' or env[3]==env[6]==env[9]=='O':
        print(f'PLAYER {a} WON')
        return 1
    return 0

def play_game():
  # set / reset global variables
    player=1
    moves=0
    check=2

    display_init_board()
    
    while True:
        display_board()
        print('value must be in "1-9"')
        check=move(player)
        if check == 0 and moves == 9:
            print("match draw")
            break
        if moves == 9 or check == 1:
            break
        while True:
            if player == 1:
                input1=input('player one(X):')
                if input1.isnumeric():
                    player1=int(input1)
                else:
                    print('Invalid value,please give correct value "1-9"')
                    continue 
                if player1 in env and env[player1] == " ":
                    env[player1]='X'
                    player=2
                    break
                else:
                    print('Invalid value,please give correct value "1-9"')
                    continue
            else:
                input2=input('player two(O):')
                if input2.isnumeric():
                    player2=int(input1)
                else:
                    print('Invalid value,please give correct value "1-9"')
                    continue 
                player2=int(input2)
                if player2 in env and env[player2]==" ":
                    env[player2]='O'
                    player=1
                    break
                else:
                    print('Invalid value,please give correct value "1-9"')
                    continue
        moves += 1
        print()

def play_again():

    play_again = False
    want_to_continue = input("Do u want to continue/restart game ? (Y/N) : ")

    # check confirmation
    while True:
        if (not want_to_continue.isalpha()):
            want_to_continue = input("Enter 'Y' to confirm, 'N' to exit")
            continue
        elif (want_to_continue.lower() == 'y'):
            play_again = True
            break
        elif (want_to_continue.lower() == 'n'):
            print("Thanks for playing!!!")
            break
        else:
            want_to_continue = input("Enter 'Y' to confirm, 'N' to exit")
            continue
    return play_again

while continue_game:
  
    # call play_game function
    play_game()

    # continue game?
    continue_game = play_again()
    if continue_game:
        env={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
