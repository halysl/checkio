import re
def first_word(text):
    text = re.sub('[^a-zA-Z\']',"?",text)
    print(text)
    a = text.split('?')
    totel = 0
    print(a)
    for i in a:
        try:
            while(i[0].isalpha()):
                print(i)
                break
            break
        except:
            continue


text = " word s4 wad"
first_word(text)