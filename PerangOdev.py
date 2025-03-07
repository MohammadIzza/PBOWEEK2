# Oddlings: Ganjil. --> 1,3,5
# Evenly: Genap.    --> 2,4,6
# Penghianat : Negatif


# print pasukan
def printPasukan(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[0], end=" ")
        return printPasukan(arr[1:])


# Total pasukan
def totalPasukan(newArr, totalPAS):
    if len(newArr) == 0:
        return totalPAS
    else:
        totalPAS += newArr[0]
        return totalPasukan(newArr[1:], totalPAS)


# array pasukan
def arrPasukan(pasukan, arr, newArr):
    if len(arr) == 0:
        return newArr
    if pasukan == "Oddlings":
        if arr[0] % 2 == 1:
            newArr.append(arr[0])
            return arrPasukan("Oddlings", arr[1:], newArr)
        return arrPasukan("Oddlings", arr[1:], newArr)

    elif pasukan == "Evenly":
        if arr[0] % 2 == 0:
            newArr.append(arr[0])
            return arrPasukan("Evenly", arr[1:], newArr)
        return arrPasukan("Evenly", arr[1:], newArr)

# main fungsi
def perang(arr):
    # inisialisasi
    newArr = []
    newArr2 = []
    totalPAS = 0
    totalPAS2 = 0

    # menentukan array pasukan
    ArrOddlings = arrPasukan("Oddlings", arr, newArr)
    ArrEvenly = arrPasukan("Evenly", arr, newArr2)

    # menghitung total pasukan
    TotalOddlings = totalPasukan(ArrOddlings, totalPAS)
    TotalEvenly = totalPasukan(ArrEvenly, totalPAS2)

    if  TotalOddlings <= 0 and TotalEvenly <= 0:
        print("Kedua pasukan sudah musnah")
    elif TotalOddlings > TotalEvenly:
        print("Oddlings menang!")
        printPasukan(ArrOddlings)
        print()
        print(TotalOddlings)
    elif TotalOddlings < TotalEvenly:
        print("Evenly menang!")
        printPasukan(ArrEvenly)
        print()
        print(TotalEvenly)
    elif TotalOddlings == TotalEvenly:
        print("Kedua pasukan damai!")
        printPasukan(ArrEvenly)
        printPasukan(ArrOddlings)
        print()
        print(TotalOddlings + TotalEvenly)


# input
# n = 4
arr = [2, -3, 8, -7, 3, -10]
# Oddlings = 0
# Evenly = 0
# pasukan = "Oddlings"
# pasukan2 = "Evenly"
# newArr = []
# newArr2 = []
# totalPAS= 0
# totalPAS2= 0

# # FUNGSI UTAMA
perang(arr)


# # UNTUK MENGECEKAN
# print("mengelompokkan pasukan genap dan ganjil")
# o = arrPasukan(pasukan,arr, newArr)
# o1 = arrPasukan(pasukan2,arr, newArr2)
# print(o)
# print(o1)
# printPasukan(o)
# print()
# printPasukan(o1)
# print()
# # print(newArr)
# # print(newArr2)

# print("menghitung total pasukan genap dan ganjil ")
# p = totalPasukan(newArr,totalPAS)
# p2 =totalPasukan(newArr2,totalPAS2)
# print(p)
# print(p2)
