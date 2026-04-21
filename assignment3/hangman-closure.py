def make_hangman(secret_word):
    guessed_word = []
    def hangman_closure(letter):
        guessed_word.append(letter.lower())
        result_word = ""
        for c in secret_word:
            if c.lower() in guessed_word:
                result_word = result_word + c
            else:
                result_word=result_word + "_"
        print(result_word)
        
        if (result_word != secret_word):
            return False
        else:
            return True
    return hangman_closure


if __name__ == "__main__":
    secret = input("Enter the secrte word ")
    game = make_hangman(secret)
    check = False
    while not check:
        guess = input("Enter a letter: ")
        check = game(guess)
    print("Congrats you guessed the correct word.")

