def min(a,b):
    if a < b:
        return a
    else:
        return b
    
def selisih(n, listBerat, b1, b2):
    if(n == 0):
        return abs(b1-b2)
    else:
        return min(selisih(n-1,listBerat, b1+listBerat[n-1], b2), selisih(n-1, listBerat, b1, b2+listBerat[n-1]))
                                                                                    
    
# 2 min(
#       1
#           
#       1
    # )
# n = int(input())
# arr = list(map(int, input().split()))

n = 2
arr = [1,2]
print(selisih(n, arr , 0, 0))
