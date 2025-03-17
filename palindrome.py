string = input("enter the string you want to check")
isPalindrome = False
for i in range(len(string)):
    if string[i] == string[len(string) - i - 1]:
        isPalindrome = True
    else:
        isPalindrome = False