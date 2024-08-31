user_input = input("Enter a word: ")
alphabet = input("Enter an alphabet you want to replace: ")
replacement = input("Enter the alphabet you want to replace it with: ")

def main(user_input, alphabet, replacement):
    new_word = user_input.replace(alphabet, replacement)
    print(new_word)

main(user_input, alphabet, replacement)