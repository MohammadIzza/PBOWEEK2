# fungsi print array
def untukPrint(arr):
    if len(arr) == 0:
        return 
    print(arr[0], end=" ")
    return untukPrint(arr[1:])

# fungsi jumlah 2 angka
def jumlah2angka(arr):
    if len(arr) == 1:
        return []
    else :
        total = arr[0] + arr[1]
        return [total] + jumlah2angka(arr[1:])

# fungsi piramida
def piramida(arr):
    if(len(arr) == 1):
        print(arr[0])
        return
    # agar direkursif dulu sampai ujung atas
    next_level = jumlah2angka(arr)
    piramida(next_level)

    # baru diprint 
    untukPrint(arr)
    print()  
        
    

# input  
n = 5
awal = 5
arr = [1,2,3,4,5]
# arr.insert(len(arr),5)
# arr.insert(len(arr),6)
# arr.insert(len(arr),7)
# arr.insert(len(arr),8)

piramida(arr)

# output
# piramida(arr)

# untukPrint(arr)
# print()
# jumlah2angka(arr)
# print()
# untukPrint(arr[1:])
# print()
# jumlah2angka(arr[1:])
# print()