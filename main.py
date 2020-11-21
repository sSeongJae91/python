#package = 라이브러리, module들의 합

#module = 코드가 들어가있는 파일

#animal package
#dog, cat module

from animal import dog #animal 패키지에서 dog라는 모듈을 import
from animal import cat

from animal import * #모든 모듈을 import

d = dog.Dog() #instance
d.hi()

c = cat.Cat()
c.hi()


# *로 전체 import 했을 시
e = Dog()
e.hi()

f = Cat()
f.hi()