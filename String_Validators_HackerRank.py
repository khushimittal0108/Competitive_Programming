if __name__ == '__main__':
    s = input()
    a,b,c,d,e=0,0,0,0,0;
    for i in s:
        if i.isalnum():
            a=1
            break
    for i in s:
        if i.isalpha():
            b=1
            break
    for i in s:
        if i.isdigit():
            c=1
            break
    for i in s:
        if i.islower():
            d=1
            break
    for i in s:
        if i.isupper():
            e=1
            break
    for j in [a,b,c,d,e]:    
        if j==0:
            print(False)
        else:
            print(True)
