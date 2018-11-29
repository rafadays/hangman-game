from os import system, name

  
# define our clear function 
def clear(): 
  
    if name == 'nt': 
        _ = system('cls')


print("Player 1 please insert a word:")
word = list(input(""))
disp = []
for i in range(len(word)):
    disp.append('*')

clear()

def Disp(word):
    strdisp = ""
    for i in range(len(word)):
        strdisp += disp[i]
    strdisp += '\n'
    print(strdisp)

Disp(word)

lives = 10
used = []


print("You can quit at any time by inserting the word QUIT.")

while lives > 0:
    #print(drawing[lives])
    print(lives)
    lettercount = 0
    valid1 = False
    valid2 = False
    letter = str(input("\nTry a character: "))
    
    if letter == "QUIT":
        lives = 0
        
    if len(list(letter)) == 1 and lives != 0:
        valid1 = True
    else:
        print("This is not a single character\n")
        lives -= 1
        
    if used.count(letter) == 0 and valid1 and lives != 0:
        valid2 = True
        used.append(letter)
    elif valid1 and lives != 0:
        print("This word was used already\n")
        lives -= 1
        
    if valid1 and valid2 and lives != 0:
        for i in range(len(word)):
            if word[i] == letter:
                disp[i] = letter
                lettercount += 1
    if lettercount == 0 and valid1 and valid2 and lives != 0:
        print("\nThe letter" , letter , "is not in the word.")
        lives -= 1
        
    
    Disp(disp)
    
    if lives == 0:
        print("You lost")
        
    if disp == word:
        lives = 0
        print("You won")

        
    

        
