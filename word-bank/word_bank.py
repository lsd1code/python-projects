from random import choice

def main():
    misplaced_letters: set[str] = set()
    incorrect_letters: set[str] = set()
    num_chances = 5    
    
    CHOSEN_WORD = choice(get_words())

    while True:
        player_word = input('Guess the word (5 letters): ')
        
        if len(player_word) != 5:
            continue
        
        result = check_words(CHOSEN_WORD, player_word, misplaced_letters, incorrect_letters)

        num_chances -= 1
        
        display_stats(result, num_chances, misplaced_letters, incorrect_letters)
        
        if CHOSEN_WORD == result:
            print(f'Congratulations!!!! You guessed the correct word: {result}. 😎✔ \n')
            play_again()
                    
        if num_chances < 1:
            print(f'Sorry, you lost. The correct word is {CHOSEN_WORD}. 😢😢 \n')
            play_again()
        

def get_words(filepath: str='words.txt') -> str:
    with open(filepath) as words:
        return [w.strip() for w in words]

        
def check_words(
    chosen_word: str, 
    player_word: str,
    misplaced_letters: set,
    incorrect_letters: set
):
    result = ''
    
    for idx, letter in enumerate(player_word):
        if chosen_word[idx] == letter:
            result += letter
        elif letter in chosen_word and chosen_word[idx] != letter:
            misplaced_letters.add(letter) 
            result += '_'
        else:
            incorrect_letters.add(letter) 
            result += '_'
                
    return result

def play_again():
    answer = input('Do you want to play again?(Y/N): ').lower()    
    return main() if answer == 'y' else exit()

def display_stats(
    player_word: str, 
    num_chances: int,
    misplaced_letters: set,
    incorrect_letters: set
) -> None:
	print(f'Current result: {player_word}')
	print(f'Misplaced letters: {list(misplaced_letters)}')
	print(f'Incorrect letters: {list(incorrect_letters)}')
	print(f'Chances remaining: {num_chances}\n')
    

if __name__ == "__main__":
    main()

"""
- The word guessing game will prompt the player to guess a 5-letter word.
- As the player submits their word guess, the game will give feedback as to whether the letters within their guess are in the word to guess

- If the player guesses the correct letter in the correct position, that letter will be filled in on the console. 
- If they guess a correct word that belongs to in the word, but it is in the wrong position, that letter will be added to a list of misplaced letters, and an underscore will be shown in that position on the console. 
- If they guess an incorrect letter that does not belong in the word, that letter will be added to a list of incorrect letters, and an underscore will be shown in that position in the console.

- The user will have a maximum of 5 tries to guess the word
"""