#
# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\__|''')
#
#
# print('''         ,r'"7
# r`-_   ,'  ,/
#  \\. ". L_r'
#    `~\\/
#       |
#       |''')
#

k = [0, 10, 20, 30]
k *= 3
print(k)


a=3
a+=6
print(a)

t=(3,4)
t*=3
print(t)
'''
chatgpt

t=(3,4)
t*=3
print(t)
의 결과값이 (3, 4, 3, 4, 3, 4)로 나왔어.
튜플은 요소를 변경할 수 없다고 배웠는데 왜 이게 가능한거야?

ChatGPT
맞습니다, 일반적으로 튜플은 변경이 불가능한(immutable) 시퀀스 타입으로 알려져 있습니다. 그러나 튜플이 가변(mutable)이 아니라는 의미는 튜플의 요소를 직접적으로 수정할 수 없다는 것을 의미합니다.

하지만 t*=3와 같은 코드는 튜플을 변경하는 것이 아니라, 기존의 튜플을 가지고 새로운 튜플을 생성한 후에 변수 t가 이 새로운 튜플을 참조하도록 만드는 것입니다. 이러한 동작은 산술 할당 연산자인 *=가 수행하는 것으로, t *= 3은 t = t * 3과 동일한 의미입니다.

따라서 t *= 3은 원래의 튜플 (3, 4)를 3번 반복한 (3, 4, 3, 4, 3, 4)를 새로운 튜플로 생성하고, t가 이 새로운 튜플을 참조하게 됩니다. 이 과정에서 기존의 튜플은 변경되지 않습니다.

흔히 사용되는 이러한 산술 할당 연산자는 변경 불가능한 객체의 참조를 업데이트하는 데 사용됩니다.'''




