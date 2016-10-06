def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


n=1
while 1:
    for p in range(2, n+1):
        print(n)
        n = n + 1
        if is_prime(p):
            print (p)

print("Done")
