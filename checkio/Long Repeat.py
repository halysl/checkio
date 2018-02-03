def long_repeat(string):
    count_max = [0,0,0,0,0,0,0,0,0,0]
    j = 0
    while string:
        for i in string:
            temp = string[0]
            if i==temp:
                count_max[j] += 1
            else:
                break
        string = string[count_max[j]:]
        j += 1
    maxnum = 0
    for i in range(10):
        print(count_max[i])
        if count_max[i]>=maxnum:
            maxnum = count_max[i]
    return maxnum

def main():
    str = "ddvvrwwwrggg"
    print(long_repeat(str))
if __name__ == "__main__":
    main()