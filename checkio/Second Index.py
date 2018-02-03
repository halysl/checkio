import re
def second_index(text: str, symbol: str):
    try:
        a = re.search(symbol,text).span()
        a = list(a)
        a = text[:a[0]]+text[a[1]:]
        a = re.search(symbol, a).span()
        a = list(a)
        print(a)
        return a[1]
    except:
        return None

second_index("find the river", "e")