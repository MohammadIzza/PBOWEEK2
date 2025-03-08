def hitung_karakter(string, index=0, count=None):
    if count is None:
        count = {}
    
    if index == len(string):
        return count
    else:
        char = string[index]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        return hitung_karakter(string, index + 1, count)


def cek_palindrom(count):
    count_copy = dict(count)
    def helper(count_dict, odd_count):
        if not count_dict:
            return odd_count <= 1
        char, cnt = count_dict.popitem()
        if cnt % 2 != 0:
            odd_count += 1
        return helper(count_dict, odd_count)
    return helper(count_copy, 0)


def buat_half_string(count, half_str="", middle_char=""):
    if not count:
        return half_str, middle_char
    char, cnt = count.popitem()
    if cnt % 2 != 0:
        middle_char = char
    half_str += char * (cnt // 2)
    return buat_half_string(count, half_str, middle_char)


def swap_char(s, i, j):
    if i == j:
        return s
    if i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]


def is_duplicate(s, start, current, pos):
    if pos >= start and pos < current:
        if s[pos] == s[current]:
            return True
        return is_duplicate(s, start, current, pos + 1)
    return False


def rekursi_permutasi(half_str, middle_char, start, palindromes, i=None):
    if i is None:
        i = start
    if start == len(half_str):
        palindrom = half_str + middle_char + half_str[::-1]
        if palindrom not in palindromes:
            palindromes.append(palindrom)
        return palindromes
    if i >= len(half_str):
        return palindromes
    if is_duplicate(half_str, start, i, start):
        return rekursi_permutasi(half_str, middle_char, start, palindromes, i + 1)
    new_str = swap_char(half_str, start, i)
    rekursi_permutasi(new_str, middle_char, start + 1, palindromes, start + 1)
    rekursi_permutasi(half_str, middle_char, start, palindromes, i + 1)
    return palindromes


def cari_palindrom(half_str, middle_char):
    palindromes = []
    return rekursi_permutasi(half_str, middle_char, 0, palindromes)


def find_min_index(arr, current, min_idx, start):
    if current >= len(arr):
        return min_idx
    if arr[current] < arr[min_idx]:
        min_idx = current
    return find_min_index(arr, current + 1, min_idx, start)


def urutkan_palindrom(palindromes, index=0):
    if index >= len(palindromes) - 1:
        return palindromes
    min_idx = find_min_index(palindromes, index + 1, index, index)
    palindromes[index], palindromes[min_idx] = palindromes[min_idx], palindromes[index]
    return urutkan_palindrom(palindromes, index + 1)


def palindoria(string):
    count = hitung_karakter(string)
    
    if not cek_palindrom(count):
        return "Kabur!"
    
    half_str, middle_char = buat_half_string(count)
    
    palindromes = cari_palindrom(half_str, middle_char)
    
    if palindromes:
        palindromes = urutkan_palindrom(palindromes)
    
    return " ".join(palindromes)


# string = str(input())
string = "racecar"
print(palindoria(string))