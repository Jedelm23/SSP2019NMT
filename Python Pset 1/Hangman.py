import random
with open("words.txt") as f:
    content = f.readlines()
wordList = [x.strip() for x in content]

#define variables
word = random.choice(wordList)
wordList = list(word)
hiddenWord = []
#Selecting Difficulty
level = str.lower(input("Select Difficulty: Easy, Normal, Hard, God: "))
if level == "easy":
    guesses = 12
    guessList = [0,1,2,3,4,5,6,7,8,9,10,11]
elif level == "hard":
    guesses = 6
    guessList = [0,1,2,3,4,5]
elif level == "god":
    guesses = 3
    guessList = [0,1,2]
else:
    guesses = 8
    guessList = [0,1,2,3,4,5,6,7]
    
guessed = []

for index in range(len(wordList)):
    hiddenWord.append("-")

hiddenWordV = ''.join(hiddenWord)
print("Guesses:", guesses)
print(hiddenWordV)

#Guessing stage
for guess in guessList:
    #Guessing
    letter = str.lower(input("Letter: "))
    
    for i in range(len(wordList)):
        counter = 0
        if letter == wordList[i]:
            counter += 1
            hiddenWord[i] = letter
            hiddenWordV = ''.join(hiddenWord) 
        if counter >= 1:
            guessList.append(0)
    #Guesses don't go away if a letter is guessed correctly
    if letter not in wordList and letter not in guessed:
        guesses -= 1

    #Displaying letters guessed
    guessed.append(letter)
    print("Already Guessed: ", ', '.join(guessed))
    
    print("Guesses:", guesses)
    print(hiddenWordV)
    
    if hiddenWordV == word:
        print("Winner Winner Chicken Dinner!")
        break
    elif guesses == 0:
        print("You must be illiterate. It was obviously ",word)
        break
