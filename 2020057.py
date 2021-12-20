


def Caesar_Cypher(word,shift):
    
    r = ''
    for x in word:
        y = (ord(x)+shift)%90
        r = r + chr(y)
    return r
 

def decrypt_Caesar_cypher(word,shift):
    r =''
    
    for x in word:
        
        y = (ord(x)-shift)%90
        if y <65:
            y = (y + 65)%90
            
            if y == 33 :
                y =  84
        
        
        r = r + chr(int(y))
    return r
print(Caesar_Cypher('DEFENDTHEFORT',7 ))
print(decrypt_Caesar_cypher('KLMLUKAOLMVYA', 7))