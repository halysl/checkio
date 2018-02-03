def correct_sentence(text):
    text = text[0].upper()+text[1:]
    if(text[-1]!="."):
        text = text+"."
    return text

text = "greeting ,friend"
correct_sentence(text)