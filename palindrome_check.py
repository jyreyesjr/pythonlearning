def palindrome_check():
    word = input("check if a word is a palindrome: ")
    rev_word = word[::-1]
    if rev_word == word:
        print("It's a palindrome")
    else:
        print("Not a palindrome")

palindrome_check()