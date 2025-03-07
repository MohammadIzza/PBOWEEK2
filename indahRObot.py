def solution(s, index = 0) :
    if index == len(s):
        return 1
    
    if s[index] == "0" :
        return 0
    
    count = solution(s, index+1)
    
    if index+1 < len(s) and int(s[index]+s[index+1]) >= 10 and int(s[index]+s[index+1]) <= 26:
        count += solution(s, index+2)
        
    return count
        
s = input().strip()
print(solution(s))