secret_word = "chupacabra"

while True:
    input_word = input("Enter the secret word: ")
    if input_word == secret_word:
        print("You've successfully left the loop.")
        break
        