def gcd(a, b):
    a = int(a)
    b = int(b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)



while True:
    input_str = input("请输入两个值，中间用空格隔开:")
    a,b = input_str.split(' ')
    print("{}和{}的最大公约数是:{}".format(a,b,gcd(a,b)))
    print('-------------------------------\n')
