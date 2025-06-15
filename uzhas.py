import random

words_to_guess = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']

def formal_guess(guess, result):
    display = []
    for j in range(len(guess)):
        s = guess[j]
        res = result[j]
        if res == 'correct':
            display.append("[" + s + ']')
        elif res == 'present':
            display.append( '(' + s + ')')
        else:
            display.append(' ' + s + ' ')
    return display


def guesscheck(guess: str, secret_word: str):
    results = []
    for i in range(len(secret_word)):
        g = guess[i]
        s = secret_word[i]
        if g == s:
            results.append("correct")
        elif g in secret_word:
            results.append("present")
        else:
            results.append("absent")
    return results


def gameplay():
    tries = 6
    secret_word = random.choice(words_to_guess)

    print("Welcome to Wordle!")
    print("Guess the", len(secret_word), "-letter word. You have", tries, "tries.")

    while tries > 0:
        try:
            guess = input("Напишіть вашу здогадку: ").lower()

            if len(guess) != len(secret_word):
                print("wrong length :(", "true length:", len(secret_word))
                continue
            result = guesscheck(guess, secret_word)
            display = formal_guess(guess, result)
            print("resultat:", ' '.join(display))

            if guess == secret_word:
                print("vy molodtsi!!! yes!!!", secret_word.upper())
                return

            tries -= 1
            print("sprob left:", tries)
        except Exception as e:
            print("pomylka appeared(((", str(e))

    print("u lost! the word was:", secret_word.upper())

while True:
    gameplay()
    retry = str(input("hochete sche raz? vvedit 'tak', yakshcho tak, i 'ni', yakshcho ni"))
    if retry != 'tak':
        print('byeee')
        break