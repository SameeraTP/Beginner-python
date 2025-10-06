import random
print("Welcome to hangman game")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
''')
stages = ['''
  _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / \\
  |
 _|___''',
 '''
  _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / 
  |
 _|___''',
 '''
  _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      
  |
 _|___''',
 '''
  _______
  |/      |
  |      (_)
  |      \|/
  |       
  |     
  |
 _|___''',
 '''
  _______
  |/      |
  |      (_)
  |      \|
  |       
  |      
  |
 _|___''',
 '''
  _______
  |/      |
  |      (_)
  |      \\
  |       
  |      
  |
 _|___''',
 '''
  _______
  |/      |
  |      (_)
  |      
  |       
  |      
  |
 _|___''',
 '''
  _______
  |/      |
  |      
  |      
  |       
  |      
  |
 _|___'''
]

lives = 7
word_list = ["Tree", "Apple", "Summer"]
word = random.choice(word_list).lower()
print(word)

placeholder = "_" * len(word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    letter = input("Guess a letter:\n").lower()

    if letter in correct_letters:
        print("You already guessed that letter.")
        continue

    display = ""
    for i in word:
        if letter == i:
            correct_letters.append(i)
            display += i
        elif i in correct_letters:
            display += i
        else:
            display += "_"

    print(display)

    if letter not in word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("YOU LOSE. The word was:", word)

    if "_" not in display:
        game_over = True
        print("YOU WIN!")

    print(stages[lives])
