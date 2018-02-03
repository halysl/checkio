def checkio(data):

    #replace this for solution
    a = 0
    b = 0
    c = 0
    if data.__len__() > 10:
        for i in data:
            if i.isupper():
                a = 1
            elif i.islower():
                b = 1
            elif i.isdigit():
                c = 1

    if a == 1 and b == 1 and c == 1:
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
