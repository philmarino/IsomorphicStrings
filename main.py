def isIsomorphic(s, t):
    con = dict() #conversionDictionary
    for i in range(len(s)):
        if s[i] in con.keys():
            if con.get(s[i]) != t[i]:
                return False
        else:
            con.update({s[i]: t[i]})

    #print(con)
    return True


# Example 1:
# Input: 
s = "egg"
t = "add"
print(isIsomorphic(s, t))
# Output: true

# Example 2:
# Input: 
s = "foo"
t = "bar"
print(isIsomorphic(s, t))
# Output: false

# Example 3:
# Input: 
s = "paper"
t = "title"
print(isIsomorphic(s, t))
# Output: true
 
