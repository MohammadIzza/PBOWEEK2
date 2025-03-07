def angkaMax(arr):
    if arr[0] > arr[-1]:
        return arr[0]  
    else:
        return arr[-1] 
    
def angkaMax2(arr):
    if arr[0] < arr[-1]:
        return arr[0]  
    else:
        return arr[-1] 
    
def arrMax(arr):
    if arr[0] > arr[-1]:
        return arr[1:]  
    else:
        return arr[:-1] 

def arrMax2(arr):
    if arr[0] < arr[-1]:
        return arr[1:]  
    else:
        return arr[:-1] 


def aukutagwa(urutan, chuya, akutagawa, arr):
    if len(arr) == 0:
        return chuya > akutagawa  # True jika Chuuya menang atau seri, False jika kalah
    
    p = angkaMax(arr)
    p2 = angkaMax2(arr)

    new_arr = arrMax(arr)
    new_arr2 = arrMax2(arr)

    if urutan == 'C':
        return aukutagwa('A', chuya + p, akutagawa, new_arr) or aukutagwa('A', chuya + p2, akutagawa, new_arr2)
    else:  # urutan == 'A'
        return aukutagwa('C', chuya, akutagawa + p, new_arr) and aukutagwa('C', chuya, akutagawa + p2, new_arr2)

# Contoh penggunaan
arr = [1,5,233,7]
arr2 = [1,5,2]
hasil = aukutagwa('C', 0, 0, arr)
hasil2 = aukutagwa('C', 0, 0, arr2)
print(hasil)  
print(hasil2) 

