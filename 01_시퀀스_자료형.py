#리스트, 튜플, 문자열, 레인지 등드 -> 값이 연속적(시퀀스)
#이와 같이 어떠한 값이 연속적으로 이어진 자료형을 시퀀스 자료형이라고 부른다.
#"파이썬"이라는 문자열은 "파", "이", "썬"이 합쳐진 것이다.

#시퀀스 자료형의 공통 기능(특징)

#1. 특정한 값(element)이 그 안에 있는지 확인할 수 있다.
# 값 in 객체(시퀀스 자료형)

# shoes = ["adidas", "nike", "nebalance"]
# print('adidas' in shoes)
# print(input('브랜드이름 : ') in shoes)
# print(input('브랜드이름 : ') not in shoes)

#시퀀스 자료형(타입)에는 문자열, 리스트, 튜플, range 등등이 해당됨.

t=("쌀국수", "기")

a=range(500, 100, -25)
print(list(a))

print(200 in a)
print((200,350) in a)

#문자열 검색
ph_n = "010 5555 9999"
print('555' in ph_n)
#문자열은 연속된 부분집합의 형태로 단어들을 검색할 수 있다. (다른 시퀀스들은 안됨)

##연결
#시퀀스 객체는 + 연산자로 서로 연결해서 새로운 시퀀스를 만들 수 있다.(웬만하면 동일 타입끼리)
#시퀀스 객체1 + 시퀀스 객체2 = 시퀀스 객체3

# a=[0,1,2,3]
# a=range(4)
a=list(range(4))
# b=[2,3,4,5,6]
# b=range(2,7) #타입 지정을 안해줬음
b=list(range(2,7))
c=a+b
print(c)

a=('a','b','c')
b=tuple('abc')

print(a==b) #true

#range는 시작점, 끝점, 증가폭이라는 조건이 있기 때문에 range끼리 서로 연결할 수 없음.
#range(0,10,1) 과 range(10,20,1)은 논리적으로 문제 없다고 여겨지지만 프로그래밍에서는 더할 수 없음.
#리스트나 튜플 등의 다른 시퀀스로 만들어주면 연결할 수 있음.

#문자열 연결
greeting = "안녕하세요! "
# my_name = input("당신의 이름 : ")
# N=greeting+my_name
# print(N)

#문자열과 숫자 연결
# money = input('받고 싶은 돈')
# print('상신의 계좌에 ' + money + "원이 입금 되었습니다.")
#
# money = int(input('받고 싶은 돈'))
# print('상신의 계좌에 ' + str(money) + "원이 입금 되었습니다.")

##반복 (*연산자)
# *는 시퀀스 객체를 특정 횟수만큼 반복하여 새로운 시퀀스 객체를 만듬
'''
시퀀스 객체 * 정수
정수* 시퀀스 객체
'''
k = [0, 10, 20, 30]
print("k를 3번 반복한다", k + k + k)
print("k를 3번 반복한다", k * 3)
print("k를 0번 반복한다", k * 0) # 음수는 빈 시퀀스.
# 튜플도 유사...
k *= 3
print(k) # 산술할당연산자 됨 (연결도 똑같이 됨)
# range는 안 됨 -> list 또는 tuple로 변환해서...
# print(range(10) * 3)
print(tuple(range(10)) * 3)

hello = "안녕"
print(hello * 50) # 문자열도 *을 통해서 반복 가능

#길이 구하기
#길이란 시퀀스의 요소의 개수를 말한다.
#파이썬에서는 len()이라는 함수로 구함. 다른 언어에서는 .length 같은걸 쓴다고 함
a=[5,3,15,43,83]
print(len(a))
b='안녕하세요' #-> '안',(+) '녕',(+) '하',(+) '세',(+) '요'
print(len(b))
