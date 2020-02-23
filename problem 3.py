# number is 12 and  its binary is '0b1100'
def maxConsecutiveones(a):
    c=0
    while (a!=0):
        a =(a & (a << 1))
        c=c+1
    return c  
print('the maximum length of one is',maxConsecutiveones(12))
