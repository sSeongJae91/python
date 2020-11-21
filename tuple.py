x = tuple()
y = ()

print(x)
print(y)

x = (1,2,3)
y=('a','b','c')
z=(1,"Hello","there")

print(x+y)
print('a' in y)
print(z.index(1))

##튜플은 상수처럼 값 할당이 안됨(immutable)
#ex)
#x[0] = 10 #Error발생