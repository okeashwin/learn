def mypower(x,n):
    if n==0:
        return 1
    temp = mypower(x,n/2)
    if n%2==1:
        return temp*temp*x
    else:
        return temp*temp

def power(x,n):
    if n==0:
        return 1
    neg = False
    if x<0:
        neg = True
        x *= float(-1)
    if n<0:
        x = float(1)/x
        n *= (-1)
    result = mypower(x,n)
    if neg and n%2==1:
        return (-1)*result
    return result

def main():
    print "Base : %s , Exponent : %s ::::: Result : %s" %(2, 3, power(2, 3))
    print "Base : %s , Exponent : %s ::::: Result : %s" % (2, -3, power(2, -3))
    print "Base : %s , Exponent : %s ::::: Result : %s" % (-2, 3, power(-2, 3))
    print "Base : %s , Exponent : %s ::::: Result : %s" % (-2, -3, power(-2, -3))

if __name__=='__main__':
    main()


