def pemecahKode(kode, n):
    if n == len(kode):
        return 1
    if kode[n] != '0':
        if kode[n] == '1':
            if n + 1 == len(kode):
                return pemecahKode(kode, n + 1)
            else:
                return pemecahKode(kode, n + 1) + pemecahKode(kode, n + 2)
        if kode[n] == '2':
            if (cekKode(kode, n + 1) and (n + 1 < len(kode))):
                return pemecahKode(kode, n + 1) + pemecahKode(kode, n + 2)
            else:
                return pemecahKode(kode, n + 1)
        else:
            return pemecahKode(kode, n + 1)
    else:
        return 0

def cekKode(kode, index):
    if index >= len(kode):
        return False
    else:
        return (kode[index] == '0' or kode[index] == '1' or kode[index] == '2' or 
            kode[index] == '3' or kode[index] == '4' or kode[index] == '5' or kode[index] == '6')

print(pemecahKode(input(), 0))