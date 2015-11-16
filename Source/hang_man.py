import random

words_to_guess_from = ['chicken', 'dog', 'cat', 'mouse', 'frog', 'baboon' ]
lives_remaining = 3

def play(lives_remaining):
    guessed_letters = ''
    word_to_guess = pick_a_word(words_to_guess_from)
    while True:
        print ('Lives remaining: ' + str(lives_remaining) )
        print ( get_word_to_guess_with_blanks( word_to_guess, guessed_letters ) )
        guess = get_guess(word_to_guess)
        if len( guess ) > 1:
            if is_whole_word_guess_correct(guess, word_to_guess):
                print('You win! Well done! Good whole-word guess!')
                break
        else:
            if is_single_letter_guess_correct(guess, word_to_guess):
                guessed_letters = guessed_letters + guess
            if word_to_guess == get_word_to_guess_with_blanks( word_to_guess, guessed_letters ):                
                print('You win! Well done! That last letter clinched it!')
                break
        lives_remaining = lives_remaining - 1
        if lives_remaining == 0:
            print( 'You are hung!')
            break
        print ('Incorrect guess; try again' )
        
def pick_a_word(words_go_guess_from):
    word_index = random.randint( 0, len(words_to_guess_from) - 1 )
    return words_to_guess_from[word_index]

def get_guess(word_to_guess):
    guess = input( 'Guess a letter or whole word: ' )
    return guess

def get_word_to_guess_with_blanks( word_to_guess, guessed_letters ):
    word_to_guess_with_blanks = ''
    for letter in word_to_guess:
        if guessed_letters.find( letter ) > -1:
            # this letter has been guessed
            word_to_guess_with_blanks = word_to_guess_with_blanks + letter
        else:
            word_to_guess_with_blanks = word_to_guess_with_blanks + '*'
    return word_to_guess_with_blanks

def is_whole_word_guess_correct(guess, word_to_guess):
    return guess == word_to_guess

def is_single_letter_guess_correct(guess, word_to_guess):
    return word_to_guess.find( guess ) > -1

play(lives_remaining)
       
