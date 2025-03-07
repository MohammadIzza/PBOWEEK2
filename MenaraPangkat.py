def f(x,y,m):
    if(y == 0):
        return 1
    else:
        return x**(f(x, y-1, m)%m)

def menaraPangkat(a,b,m):
    return (f(a,b,m) % m)

# inp = list(map(int, input().split()))

inp=[7,3,7]
print(menaraPangkat(inp[0], inp[1], inp[2]))
