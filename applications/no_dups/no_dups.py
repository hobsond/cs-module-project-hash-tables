def no_dups(s):
    # Your code here
    
    # create a cache variable
    cache = {}
    current = ''
    # Will loop through each character of the string
    # for i in s:
    #     if i.isalpha():
    #         current +=i
            
    # if it is an alpha i will concatnate it to the current word
    # if the word is a space i will create a variable for that word
        # if i.isspace():
        #     x = current 
            # current = ''
    # if that word is in cache i will continue the looop else
            # if x not in cache:
            #     cache[x] = x
                
    # else i will add a that word and set the current to empty
    for i in range(len(s)):
        if s[i].isalpha():
            current +=s[i]
            
        
        if s[i].isspace():
            x = current.strip() 
            current = ''
            if x not in cache:
                cache[x] = x
        if i+1 >= len(s):
            if current not in cache:
                
                cache[current] = current
                current = ''
    x = ''
    for i in cache:
        x+= f" {i}"
    return x



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))