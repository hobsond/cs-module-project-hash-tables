# Your code here


def histo(file):
    # open the text
    cache = {}
    textFile = open(f"{file}.txt",'r')
    lineArray = textFile.read()
    current = ''
    for i in lineArray:
        if i.isalpha():
            current += i
            
        if i.isspace():
            current = current.lower()
            # x[current] = current
            x = current
            current=''
            
            if x in cache:
                cache[x] += '*'
            else:
                cache[x] = ""
                
        
    return cache          
            
    # print(x)
    
    
    
def sortPrint(item):
   j =  histo(item)
   
   item = list(j.items())
   item.sort(key=lambda e: e[1],reverse=False)
   for i in item:
       if len(i[1]) > 0:
           print(f"{i[0]} {i[1]} " ) 
           
        
   
    
    
sortPrint('robin')