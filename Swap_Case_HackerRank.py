def swap_case(s):
    S=""
    for i in s:
        if i.isupper():
            S=S+i.lower()
        else:
            S=S+i.upper()
    return S

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
