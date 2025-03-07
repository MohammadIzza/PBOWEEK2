def solve(n, stat, s, ans):
    if n == 0:
        ans.append(s)
    else:
        if stat == '0':
            solve(n-1, '0', s + "0", ans)  # Menambahkan '0' setelah '0' atau '1'
            solve(n-1, '1', s + "1", ans)  # Menambahkan '1' setelah '0'
        elif stat == '1':
            solve(n-1, '0', s + "0", ans)  # Hanya bisa menambah '0' setelah '1'

# 0 
# 0 1      
# 00 01 10 
# 000 001 010 100 101

# Membaca input panjang string
# n = int(input())
    
n = 3
ans = []
stat = '0' # 
s = ""
# 000 001 010 100 101

# Memulai rekursi dari string kosong dan status awal '0'
solve(n,stat,s, ans)
    
# Menampilkan hasil
print(" ".join(ans))

