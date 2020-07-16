env={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
player=1
moves=0
check=2
def move():
    if env[1]=='X' and env[2]=='X' and env[3]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[4]=='X' and env[5]=='X' and env[6]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[7]=='X' and env[8]=='X' and env[9]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[1]=='X' and env[5]=='X' and env[9]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[3]=='X' and env[5]=='X' and env[7]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[1]=='X' and env[4]=='X' and env[7]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[2]=='X' and env[5]=='X' and env[8]=='X':
        print("PLAYER ONE WON")
        return 1
    if env[3]=='X' and env[6]=='X' and env[9]=='X':
        print("PLAYER ONE WON")
        return 1
    #player one over
    if env[1]=='O' and env[2]=='O' and env[3]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[4]=='O' and env[5]=='O' and env[6]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[7]=='O' and env[8]=='O' and env[9]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[1]=='O' and env[5]=='O' and env[9]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[3]=='O' and env[5]=='O' and env[7]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[1]=='O' and env[4]=='O' and env[7]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[2]=='O' and env[5]=='O' and env[8]=='O':
        print("PLAYER TWO WON")
        return 1
    if env[3]=='O' and env[6]=='O' and env[9]=='O':
        print("PLAYER TWO WON")
        return 1
    return 0
print(' TIC TAC TOE')
print(' -----------')
print('   |1|2|3|')
print('   -------')
print('   |4|5|6|')
print('   -------')
print('   |7|8|9|\n')
while True:
    print('   '+'|'+env[1]+'|'+env[2]+'|'+env[3]+'|')
    print('   -------')
    print('   '+'|'+env[4]+'|'+env[5]+'|'+env[6]+'|')
    print('   -------')
    print('   '+'|'+env[7]+'|'+env[8]+'|'+env[9]+'|''\n')
    print('value must be in "1-9"')
    check=move()
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
            
