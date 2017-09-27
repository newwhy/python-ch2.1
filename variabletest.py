import keyword
# 변수 이름은 문자. 순자 . _로 구성해야한다

friend = 1
a = 10
my_name = '위효연'
_yourName = '둘리'
member1 = '도우넛'

# 에러
# $friend = 2\
# a! = 1
# 1abc = 10


# 에러: 예약어는 사용할 수 없다
# def = 10
#예시 kw=> keyword
print(keyword.kwlist)

# 한글이름의 변수도 가능
가격1 = 2000
print(가격1 - 200)

print(len(keyword.kwlist))


