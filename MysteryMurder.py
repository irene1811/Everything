start = '''
You wake up in a room with Sorya, your awesome personal chef dead on the floor
\nYou don't remember how you got there,
\nbut if someone finds you like this they'll blame you!
\nFind the real murderer or you will be charged of murder!!!
'''

print (start)
print('''
You hear someone walking towards the room! What do you do with the body?
\nType '1' if you want to leave it there.
\nType '2' if you want to put Sorya's body in the closet ''')
user_input = input()
if user_input == "1":
    print ('''You leave the body there.
    \nIrene walks into the room and is shocked by what she sees.
    \nDo you want to kill her or explain the situation?
    \nType '1' if you want to kill her
    \nType '2' if you want to explain the situation''')
    user_input = input()
    if user_input == "1":
        print (''' You stab Irene and Irene passes out and dies.
        \nYou run away from the crime scene and as you are running
        \nyou bump into Sophie! You notice that Sophie has bloody bandages on her hand
        \nType '1' if you want to distract Sophie so she doesn't go to the room or
        \nType '2' if you want to tell Sophie that Laura killed Irene''')
        user_input = input()
        if user_input == '1':
            print ('''You distract Sophie with an awesome dance to distract her.
            \nHowever, Sophie is suspicious of you awesome dance moves
            \nShe walks past you and she finds Irene's body!
            \nYou get charged with first degree murder of Irene. Game Over.
            ''')
        elif user_input == '2':
            print ('''You tell Sophie that Laura killed Irene. Sophie calls the police
            \nLaura comes out of the break room with Sorya's food!
            \nYou get away with murder. Laura is charged with first degree murder
            \nHowever, you did not solve the murder mystery of Sorya. Game Over
            ''')
        else:
            print ('Well I guess game over?')
    elif user_input == "2":
        print ('''You explain to Irene that you found Sorya's body in the coding room!
        \nYou ask Irene what she was doing on the night Sorya died.
        \nIrene says that she was playing Call of Duty
        \nYou've hit a dead end! Game Over''')
    else:
        print ('Well I guess game over?')
elif user_input == '2': #turn if to else
    print('''Shove the body in the closet...
    \nBody is now hidden.
    \nNo one saw
    \nYou start to run.
    \nyou run into irene
    \nwhat do you do next
    \n1= Question her, 2= Run past her''')
    ...
    user_input = input()
    if user_input =="2":
        print('''you contine to run
        \nas you do you reamber she previuosly had a argument with Sorya...
        \nyou trip on her shoe!!!
        \n you bump your head
        \nthen like a flash
        \nyou reamber
        \n......
        \nyou killed Sorya''')
    elif user_input=="1":
        print('''Question Irene
        \nIrean:I was only playing Call of Duty,
        \nwhat were you up to?
        \nYou freeze, realizing...
        \n you have no memory
        \n Game over''')
    else:
        print ('Well I guess game over?')

else:
    print ('Well I guess game over?')
