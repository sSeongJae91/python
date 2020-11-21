#function, parameter
def chat(name1, name2, age):
    print("%s : 안녕? 넌 몇살이니?" % name1)
    print("%s : 나? 나는 %d" % (name2, age))

chat("알렉스", "윤하", 10)
chat("철수", "영희", 30)

#function, parameter, return
def dsum(a, b):
    result = a+b
    return result

d = dsum(2, 4)
print(d)

