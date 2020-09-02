# Your code here
table={}
def expensive_seq(x, y, z,cache = None ):
    
    # Your code here
    if cache is None:
        cache = {}
    if (x,y,z) not in cache: 
        count = 0
        if x <= 0:
            count = y+z
        else:
            count += expensive_seq(x-1,y+1,z,cache)
             
        cache[(x,y,z)] = count
    
    return cache[(x,y,z)]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(250,500,900))
