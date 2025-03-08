def hitung_permutasi(S, M, constraints):
    def permutasi(n):
        if n == 1:
            return 1
        return n * permutasi(n - 1)
    
    def mark_fixed(S, constraints, idx=0, fixed_post=None):
        if fixed_post is None:
            fixed_post = []
        
        if idx == len(S):
            return fixed_post
        
        if idx >= len(fixed_post):
            fixed_post.append(False)
        
        if idx < len(constraints):
            c, p = constraints[idx]
            while len(fixed_post) < p:
                fixed_post.append(False)
            fixed_post[p - 1] = True
        
        return mark_fixed(S, constraints, idx + 1, fixed_post)

    def collect_unmark(S, fixed_post, idx=0, karakter_bebas=None):
        if karakter_bebas is None:
            karakter_bebas = []
        
        if idx == len(S):
            return karakter_bebas
        
        if not fixed_post[idx]:
            karakter_bebas.append(S[idx])
        
        return collect_unmark(S, fixed_post, idx + 1, karakter_bebas)

    def all_same(lst):
        if len(lst) <= 1:
            return True
        return lst[0] == lst[1] and all_same(lst[1:])

    fixed_post = mark_fixed(S, constraints)
    karakter_bebas = collect_unmark(S, fixed_post)
    
    if all_same(karakter_bebas):
        return 1
    
    permutasi_bebas = permutasi(len(karakter_bebas))
    
    return permutasi_bebas

S = input().strip()
M = int(input().strip())
constraints = []
for _ in range(M):
    C, P = input().strip().split()
    constraints.append((C, int(P)))

print(hitung_permutasi(S, M, constraints))