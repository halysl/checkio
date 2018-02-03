import re

def checkio(text):
    text = re.sub('[^a-zA-Z]',"",text)
    text = text.lower()
    arr = [[]*26]*26
    max_len = 0
    for i in range(26):
        temp = chr(ord('a')+i)
        arr[i] = re.findall(temp,text)
    for i in range(26):
        if len(arr[i])>max_len:
            max_len = len(arr[i])
            tt = arr[i][0]
    return tt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")