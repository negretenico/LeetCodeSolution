import re


def isPalindrome( s: str) -> bool:
    if len(s)==1:
        return True
    t = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    i, j = 0, len(t)-1
    while i <j:
        if not t[i] == t[j]:
            return False
        i +=1
        j-=1
    return True
