#input() : 키보드로 부터 입력받는 명령어

a=int(input('첫 번째 수를 입력하세요. : '))
b=int(input('두 번째 수를 입력하세요. : '))

add=a+b
sub=a-b
mul=a*b
div=a/b

'''print('첫 번째 수를 입력하세요. : ')
a=input()
print('두 번째 수를 입력하세요. : ')
b=input()

add=int(a)+int(b)
sub=int(a)-int(b)
mul=int(a)*int(b)
div=int(a)/int(b)'''

print(a,'+',b,'=',add)
print(a,'-',b,'=',sub)
print(a,'*',b,'=',mul)
print(a,'/',b,'=',div)
print(a,'/',b,'=','%7.1f'div)
