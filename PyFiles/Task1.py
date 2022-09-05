def find_ind(a, b):
    ans = []
    for i in range(len(b)):
        if i + len(a) <= len(b) and b[i:i + len(a)] == a:
            ans.append(i)
        
    return ans 