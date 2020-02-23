a=['chair','height','racket','touch','tunic']
s=[]
for i in a:
    if i.startswith('c'):
        s.append(i)
    elif i.startswith('r'):
        s.insert(1,i)
    elif i.startswith('to'):
        s.insert(2,i)
    elif i.startswith('h'):
        s.insert(3,i)
    elif i.startswith('tu'):
        s.insert(4,i)
print('input ',a)        
print('output ',s)
        
        
    


    
