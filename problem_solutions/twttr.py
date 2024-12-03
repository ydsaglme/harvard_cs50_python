def main():
    tweet = input("Input: ")
    output = shorten(tweet)
    print("Output:", output)

def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    residuals = []
    for letter in word:
        if letter not in vowels:
            residuals.append(letter)
    output = str("".join(residuals))
    return output

if __name__ == "__main__":
    main()
