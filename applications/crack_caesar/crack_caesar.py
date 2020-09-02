# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
text = open('ciphertext.txt','r')
lines = text.read()
def cipher(s):
    
    cache = {}
    holder =[]
    cracker=['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
            'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    crackList={}
    letter = ''
    def cipherCount(s):
        for i in s:
            if i.isalpha():
                if i not in cache:
                    cache[i] = [i,1]
                cache[i][1] +=1
        return cache

    def getCipher():
        x = cache
        for i  in x.values():
            holder.append(i)

    cipherCount(s)
    getCipher()
    holder.sort(key=lambda e:e[1], reverse=True)
        
    for i in range(len(holder)-1):
        x = holder[i][0]
        crackList[holder[i][0]] = cracker[i]
        

    # print(crackList)g
    for i in lines:
        if i in crackList:
            letter +=crackList[i]
        letter += i
        
    return letter


# x = cipher(lines)

# for i in range(2000):
#     t = cipher(x)
#     x = t 

print(cipher(lines))