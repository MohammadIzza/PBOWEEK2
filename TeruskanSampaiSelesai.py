def cariAngka(arr,n, index):
    if(len(arr) == 0):
        return '"Tidak ditemukan"'
    else :
        if(arr[0] == n):
            return index 
        else:
            return cariAngka(arr[1:],n, index+1)


# input
arr = [1,2,3]
n = 2
index = 0
hasil = cariAngka(arr,n,index)
print(hasil)


