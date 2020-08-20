def print_formatted(number):
    # your code goes here
    s=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(s),end=' ')
        print(str(oct(i)[2:]).rjust(s),end=' ')
        print(str(hex(i)[2:]).upper().rjust(s),end=' ')
        print(str(bin(i)[2:]).rjust(s))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
