# The variables:
vowels = {"A", "E", "I", "O", "U"}

# The script 
user_word = input("Enter the word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in vowels:
        continue
    else:
        print(letter)
        
        