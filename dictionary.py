x = dict()
y = {}

print(x)
print(y)

#dictionary 는 java의 Map처럼 key와 value로 구성
#key는 immutable

x = {
    "name" : "성재",
    "age" : 30,
    5 : "Hello"
}

print(x["name"])
print(x["age"])
print(x[5])

#in 은 key를 찾음 -> return : true/false
print("age" in x)

#dict의 모든 key 출력
print(x.keys())

#dict의 모든 val 출력
print(x.values())


#loop + dict
for key in x:
    print("key : " + str(key))
    print("value : " + str(x[key]))

#key put
x["school"] = "한빛"
print(x)