#Max McCalla
#Python Programming
#Starship Password Manager
#2/1/2022
#Version 4.0

#Imports
#Tries to import random and exits program if an error occurs
try:
    import random
    import pyclip
except:
    print("Your imports have not been added correctly. The program has stopped.")
    exit()
    
#Menu function
def menu():
    print('\nWhat would you like to do?\n(C)heck Password\n(G)enerate Password\n(Q)uit')
    inputAsk = input().lower()
    return(inputAsk)

#Check for uppercase letters
def checkUpper(password):
    for letters in password:
        if letters.isupper():
            return True
            break
    return False 

#Check for lowercase letters
def checkLower(password):
    for letters in password:
        if letters.islower():
            return True
            break
    return False

#Check For Numbers
def checkNumber(password):
    for letters in password:
        if letters.isdigit():
            return True
            break
    return False

#Check for Special Characters
def checkSpecial(password):
    specialChars = '.!@#$%&*'
    for letters in password:
        if letters in specialChars:
            return True
            break
    return False

def checkPassword():
    password = input('What is your Password? ') #initial ask
    length = len(password)
    #Check length and check for each type of character (I'll make a better implementation later)
    while length < passwordLength or checkUpper(password) == False or checkLower(password) == False or checkNumber(password) == False or checkSpecial(password) == False:
        print('That is not a valid password. Please check the rules again.') #failed check message
        password = input('What is your Password? ') #ask again
        length = len(password)
    
    print('That password is valid!') #confirms a passed check

    
def generatePassword():
    #Ask for a name in a blank string
    name = ''
    name = input('What is your name? ')
    #Creates a reversed letters list and a list of possible letters
    reversedLetters = []
    possibleLetters = "abcdefghijklmnopqrstuvwxyz1234567890.!@#$%&*"
    #Reverses your name
    for letters in name:
        reversedLetters.insert(0,letters)
    reversedName = ''.join(reversedLetters)
    #Creates a random string of 12 characters
    generatedPassword = ''
    randomString = ''
    while len(randomString) < 12:
        randomLetter = random.randint(0,len(possibleLetters)-1)
        randomString = randomString + possibleLetters[randomLetter]
    
    #Adds half of the random string before the reversed name
    for index in range(6):
        generatedPassword = generatedPassword + randomString[index]
    generatedPassword = generatedPassword + reversedName
    #And half of the random string afterwards
    for index in range(7,12):
        generatedPassword = generatedPassword + randomString[index]
    #Print the name, random and password data
    print(f'Your name reversed is {reversedName}')
    print(f'Your random digits are {randomString}')
    print(f'Your password is {generatedPassword}')
    pyclip.copy(generatedPassword)
    print('Your password has been copied to your clipboard!')

#----------------------------------------------Main Program-----------------------------------------------------

#these lines define the welcome message and logo (In separate variables to avoid making one really long line of code)
message ='''|------------------| _____ _                 _     _
|        /\        |/  ___| |               | |   (_)
|       /||\       |\ `--.| |_ __ _ _ __ ___| |__  _ _ __
|   || / || \ ||   | `--. \ __/ _` | \'__/ __| \'_ \| | \'_ \ 
|   ||/  ||  \||   |/\__/ / || (_| | |  \__ \ | | | | |_) |
|   |/   ||   \|   |\____/ \__\__,_|_|  |___/_| |_|_| .__/
|   /    ||    \   |                                | |
|  /=====||=====\  |                                |_|
|  \=====||=====/  |______                                   _
|   \    ||    /   || ___ \                                 | |                _  _    ___  
|    \   ||   /    || |_/ /_ _ ___ _____      _____  _ __ __| |___    /\   /\ | || |  / _ \ 
|     \  ||  /     ||  __/ _` / __/ __\ \ /\ / / _ \| \'__/ _` / __|   \ \ / / | || |_| | | |
|      [][][]      || | | (_| \__ \__ \\\ V  V / (_) | | | (_| \__ \    \ V /  |__   _| |_| |
|      ~~~~~~      |\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___/     \_/      |_|(_)___/ 
|------------------|\n
Welcome to the Starship Password Manager!
This password system will create and validate passwords automatically!\n'''

#These lines define the rules message
passwordLength = 12
rules = '''These are the rules for generating passwords. Passwords must:
\u2022Contain uppercase and lowercase letters.
\u2022Contain letters and numbers.
\u2022Contain special characters.
\u2022Contain at least ''' + str(passwordLength) + ' characters.'


#Print the set messages
print(message)
print(rules)
menuAnswer = ''
while menuAnswer != 'q':
    #While the menu doesn't return "q", run the menu loop
    try:
        menuAnswer = menu()
    except:
        print("Menu Error. The program has stopped.")
        exit()
    
    if menuAnswer == 'c':
    #Runs the password checker if the menu returns "c"
        try:
            checkPassword()
        except:
            print("Password Checker error. The program has stopped.")
            exit()
            
    if menuAnswer == 'g':
        #Runs the password generator if the menu returns "g"
        try:
            generatePassword()
        except:
            print("Password Generation error. The program has stopped.")
            exit()
            
print('Thanks for using Starship Password Manager!')