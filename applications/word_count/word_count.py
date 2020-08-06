

cache = {}



def word_count(s):
    # Your code here
    # create cache
    
    # loop through each letter add it to the current
    current = ''
    for i in range(len(s)) :
        
        if s[i].isalpha():
            current+=s[i]
        
        
                
            
        if s[i].isspace():
            x = current.lower()
            if x in cache:
                cache[x] += 1
            else:
                
                cache[x] = 1
            current = ''
        elif i + 2 > len(s):
            if current.lower() not in cache:
                cache[current.lower()] = 1
            else:
                cache[current]+=1
                
            
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only '))