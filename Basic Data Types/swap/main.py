def swap_case(s):
    n = ''
    for i in range(len(s)):
        if s[i].islower():
            n += (s[i].upper())
        else:
            n += (s[i].lower())
    return n


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



