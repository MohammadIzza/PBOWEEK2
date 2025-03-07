def kromosom(arr):
    if len(arr) == 1:
        return False 
    if(len(arr) >= 2):
        if(arr[0] == 'X' and arr[1] == 'Y'):
            return 1 + kromosom(arr[1:])
        else:
            return 0 + kromosom(arr[1:])
    else:
        return 0 + kromosom(arr[1:])
    
def boolenKromosom(arr):
    if (kromosom(arr) % 2) == 0:
        return True
    else:
        return False


arr = ['A','X','X','Y','X','Y','X','Y']

print(boolenKromosom(arr))