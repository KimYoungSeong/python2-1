# if... elif ... else
print('수를 입력하세요:')
a = int(input())

if a > 10 and a % 2 == 0:
    print('10보다 큰 짝수')
elif a > 10 and a % 2 != 0:
    print('10보다 큰 홀수')
elif a < 10 and a % 2 == 0:
    print('10 이하의 짝수')
elif a < 10 and a % 2 != 0:
    print('10 이하의 홀수')

'''a = int(input())

if a > 10 :
    if a % 2 == 0:
        print('10보다 큰 홀수')
    else :
        print('10보다 큰 홀수')
if a < 10 :
    if a % 2 == 0:
        print('10보다 작은 홀수')
    else :
        print('10보다 작은 홀수')'''
