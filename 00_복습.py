# 불과 비교, 논리 연산자
## 불과 비교 연산자 사용하기
"""
* 프로그래밍을 하다 보면 참, 거짓을 판단해야 할 때가 많습니다. 참은 무엇인가가 맞다, 거짓은 틀리다(아니다)를 표현합니다.
* 이번에는 참(True), 거짓(False)을 나타내는 불(boolean)을 알아보겠습니다. 그리고 두 값의 관계를 판단하는 비교 연산자와 두 값의 논릿값을 판단하는 논리 연산자도 함께 알아보겠습니다.
* 여기서 비교, 논리 연산자는 프로그래밍에서 매우 광범위하게 쓰입니다. 특히 앞으로 배울 if, while 구문을 작성할 때 비교, 논리 연산자를 자주 사용합니다.
"""
# 불은 True, False로 표현하며 1, 3.6, 'Python'처럼 값의 일종
can_smoke = True
print("can_smoke", can_smoke)
can_drink_beer = False
print("can_drink_beer", can_drink_beer)
"""### 비교 연산자의 판단 결과
* 파이썬에서는 비교 연산자와 논리 연산자의 판단 결과로 True, False를 사용합니다. 즉, 비교 결과가 맞으면 True, 아니면 False입니다.
"""
# my_age = int(input("나이는?"))
# can_bootcamp = my_age >20

# print(can_bootcamp)


"""### 숫자가 같은지 다른지 비교하기
* 이제 두 숫자가 같은지 또는 다른지 비교해보겠습니다. 두 숫자가 같은지 비교할 때는 ==(equal), 다른지 비교할 때는 !=(not equal)을 사용합니다.
"""
"""* 10과 10은 같으므로 True, 10과 5는 다르므로 True가 나옵니다. 파이썬에서 두 값이 같은지 비교할 때는 =이 아닌 ==을 사용합니다. 왜냐하면 =은 할당 연산자로 이미 사용되고 있기 때문입니다.
### 문자열이 같은지 다른지 비교하기
숫자뿐만 아니라 문자열도 ==와 != 연산자로 비교할 수 있습니다. 이때 문자열은 비교할 때 대소문자를 구분합니다. 다음과 같이 단어가 같아도 대소문자가 다르면 다른 문자열로 판단합니다.
"""
"""### 부등호 사용하기
* 부등호는 수학 시간에 배운 내용과 같습니다. 큰지, 작은지, 크거나 같은지, 작거나 같은지를 판단해봅니다.
"""
"""* 여기서 비교 기준은 첫 번째 값입니다. 따라서 첫 번째 값보다 큰지, 작은지처럼 읽습니다. 항상 이점을 기억해두세요.
* 특히 부등호를 말로 설명할 때 >은 초과, <은 미만, >=은 이상, <=은 이하라고도 합니다. 그리고 >, <은 비교할 값과 같으면 무조건 거짓입니다. 하지만 >=, <=은 비교할 값과 같으면 참입니다. 따라서 이상, 이하는 비교할 값도 포함된다는 점이 중요합니다.
### 객체가 같은지 다른지 비교하기
* 이번에는 is와 is not입니다. 같다는 ==, 다르다는 !=이 이미 있는데 왜 is, is not을 만들었을까요? is, is not도 같다, 다르다지만 ==, !=는 값 자체를 비교하고, is, is not은 객체(object)를 비교합니다.
"""
"""* 1과 1.0은 정수와 실수라는 차이점이 있지만 값은 같습니다. 따라서 ==로 비교해보면 True가 나옵니다. 하지만 1과 1.0을 is로 비교해보면 False가 나옵니다. 왜냐하면 1은 정수 객체, 1.0은 실수 객체이므로 두 객체는 서로 다르기 때문입니다. 물론 1과 1.0을 is not으로 비교하면 True가 나오겠죠?


## 논리 연산자 사용하기
* 이번에는 논리 연산자를 사용해보겠습니다. 논리 연산자는 and, or, not이 있는데 먼저 and입니다.
* `a and b`
"""

n1, n2 = input("숫자두개입력 ".split())
print(n1)
print(n2)

"""* and는 두 값이 모두 True라야 True입니다. 하나라도 False이면 False가 나옵니다.
* 이번에는 or입니다.
* `a or b`
"""
"""* or는 두 값 중 하나라도 True이면 True입니다. 두 값이 모두 False라야 False가 되죠.
* 마지막으로 not입니다.
* `not x`
"""
"""* not은 논릿값을 뒤집습니다. 그래서 not True는 False가 되고, not False는 True가 됩니다.
* 여기서 and, or, not 논리 연산자가 식 하나에 들어있으면 not, and, or 순으로 판단합니다.
"""
"""* 식이 꼬여 있어서 상당히 헷갈리죠? 가장 먼저 not True와 not False를 판단하여 False and False or True가 됩니다.
* 그다음에 False and False를 판단하여 False가 나와서 False or True가 되므로 최종 결과는 True가 됩니다.
"""
# 이 식을 괄호로 표현하면 다음과 같은 모양이 됩니다.
"""* 순서가 헷갈릴 때는 괄호로 판단 순서를 명확히 나타내 주는 것이 좋습니다.
### 논리 연산자와 비교 연산자를 함께 사용하기
"""
"""* 비교 연산자로 비교한 결과를 논리 연산자로 다시 판단했습니다. 이때는 비교 연산자(is, is not, ==, !=, <, >, <=, >=)를 먼저 판단하고 논리 연산자(not, and, or)를 판단하게 됩니다
### 정수, 실수, 문자열을 불로 만들기
* 정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 됩니다. 이때 정수 1은 True, 0은 False입니다. 만약 문자열의 내용이 'False'라도 불로 만들면 True입니다. 문자열의 내용 자체는 판단하지 않으며 값이 있으면 True입니다.
"""
# 문자열
## 문자열 사용하기
"""
# 문자열 'Hello, world!'를 출력
# 한글 문자열
#  " "(큰따옴표)로 묶기
# '''(작은따옴표 3개)로 묶거나 \"""(큰따옴표 3개)로 묶기
"""### 여러 줄로 된 문자열 사용하기
"""
* 이번에는 여러 줄로 된 문자열(multiline string)을 사용해보겠습니다. 다음과 같이 '''(작은따옴표 3개)로 시작하고 Hello, world!를 입력한 다음에 엔터 키를 누르면 다음 줄로 이동합니다. 이런 방식으로 문자열을 계속 입력하고 마지막 줄에서 '''로 닫습니다.
"""
"""* 이처럼 여러 줄로 된 문자열은 '''(작은따옴표 3개)로 시작하여 '''로 끝납니다. 물론 '''(큰따옴표 3개)로 시작하여 '''로 끝내도 됩니다.
### 문자열 안에 작은따옴표나 큰따옴표 포함하기
* 그런데 문자열을 표현할 때 작은따옴표와 큰따옴표 중 한 가지로 통일하지 않고 여러 가지 방식을 사용할까요?
* 문자열을 사용하다 보면 문자열 안에 작은따옴표나 큰따옴표를 넣어야 할 경우가 생깁니다. 이때는 작은따옴표와 큰따옴표를 사용하는 규칙이 달라집니다.
"""
# 먼저 문자열 안에 '(작은따옴표)를 넣고 싶다면 문자열을 "(큰따옴표)로 묶어줍니다. 이렇게 하면 문자열 안에 '를 그대로 사용할 수 있습니다.
# 반대로 문자열 안에 "(큰따옴표)를 넣고 싶다면 문자열을 '(작은따옴표)로 묶어줍니다.
# 하지만 작은따옴표 안에 작은따옴표를 넣거나 큰따옴표 안에 큰따옴표를 넣을 수는 없습니다.
# 하지만 여러 줄로 된 문자열은 작은따옴표 안에 작은따옴표와 큰따옴표를 둘 다 넣을 수 있습니다.
# 또한, 큰따옴표 안에도 작은따옴표와 큰따옴표를 넣을 수 있습니다.
"""### 문자열에 따옴표를 포함하는 다른 방법
* 작은따옴표 안에 작은따옴표를 넣을 수는 없을까요? 방법이 있습니다. 다음과 같이 작은따옴표 앞에 \(역슬래시)를 붙이면 됩니다.
"""
"""* 물론 큰따옴표도 "He said \"Python is easy\""처럼 큰따옴표 앞에 \를 붙이면 됩니다.
* 이처럼 문자열 안에 ', " 등의 특수 문자를 포함하기 위해 앞에 \를 붙이는 방법을 이스케이프(escape)라고 부릅니다.
"""
# 리스트와 튜플
## 리스트
# 지금까지 변수에는 값을 한 개씩만 저장했습니다.
"""* 그럼 값을 30개 저장하려면 어떻게 해야 할까요? 다음과 같이 변수 30개에 값 30개를 저장하면 됩니다.
```
a1 = 10
a2 = 20
# ... (생략)
a29 = 60
a30 = 40
```
* 변수 30개를 일일이 타이핑하기는 쉽지 않습니다. 만약 저장할 값이 3,000개라면 정말 끔찍하죠? 이때는 리스트를 사용하면 편리합니다. 리스트는 말 그대로 목록이라는 뜻이며 값을 일렬로 늘어놓은 형태입니다(보통 리스트의 값은 코드로 생성하는 경우가 많아서 타이핑할 일이 거의 없습니다).
### 리스트 만들기
* 변수에 값을 저장할 때 `[ ](대괄호)`로 묶어주면 리스트가 되며 각 값은 ,(콤마)로 구분해줍니다.
* `리스트 = [값, 값, 값]`
"""
"""* 변수에 [ ]로 값을 저장하여 리스트를 만들었습니다. 특히 리스트에 저장된 각 값 요소(element)라고 부릅니다.
### 리스트에 여러 가지 자료형 저장하기
* 리스트는 문자열, 정수, 실수, 불 등 모든 자료형을 저장할 수 있으며 자료형을 섞어서 저장해도 됩니다
"""
"""* 이처럼 리스트에 여러 가지 자료형을 사용하면 관련 정보를 하나로 묶기 좋습니다.
### 빈 리스트 만들기
* 빈 리스트를 만들 때는 [ ]만 지정하거나 list를 사용하면 됩니다.
* `리스트 = []`
* `리스트 = list()`
"""
"""* 빈 리스트는 쓸모가 없을 것 같지만, 보통 빈 리스트를 만들어 놓은 뒤에 새 값을 추가하는 방식으로 사용합니다.
### range를 사용하여 리스트 만들기
* 이번에는 range를 사용하여 리스트를 만들어보겠습니다. range는 연속된 숫자를 생성하는데 range에 10을 지정하면 0부터 9까지 숫자를 생성합니다. 즉, 지정한 횟수 숫자는 생성되는 숫자에 포함되지 않습니다.
* `range(횟수)`
"""
"""* range(0, 10)이라고 나와서 10까지 생성될 것 같지만 10은 포함되지 않습니다. 다음과 같이 list에 range(10)을 넣어보면 0부터 9까지 들어있는 리스트가 생성됩니다.
* `리스트 = list(range(횟수))`
"""
"""* range는 시작하는 숫자와 끝나는 숫자를 지정할 수도 있습니다. 이때도 끝나는 숫자는 생성되는 숫자에 포함되지 않습니다. 즉, list에 range(5, 12)를 넣으면 5부터 11까지 들어있는 리스트가 생성됩니다.
* `리스트 = list(range(시작, 끝))`
"""
"""* 이번에는 증가폭을 사용하는 방법입니다. range에 증가폭을 지정하면 해당 값만큼 증가하면서 숫자를 생성합니다.
* `리스트 = list(range(시작, 끝, 증가폭))`
"""
"""* range(-4, 10, 2)는 -4부터 8까지 2씩 증가합니다. 여기서 끝나는 값은 10이므로 10까지 증가하지 않고 8까지 생성됩니다.
* 만약 증가폭을 음수로 지정하면 해당 값만큼 숫자가 감소합니다.
"""
"""## 튜플
지금까지 리스트를 사용해보았는데 파이썬에서는 튜플이라는 자료형도 제공합니다. 튜플은 리스트처럼 요소를 일렬로 저장하지만, 안에 저장된 요소를 변경, 추가, 삭제를 할 수 없습니다. 간단하게 읽기 전용 리스트라고 할 수 있죠
변수에 값을 저장할 때 ( )(괄호)로 묶어주면 튜플이 되며 각 값은 ,(콤마)로 구분해줍니다. 또는, 괄호로 묶지 않고 값만 콤마로 구분해도 튜플이 됩니다.
* `튜플 = (값, 값, 값)`
* `튜플 = 값, 값, 값`
"""
# 숫자가 5개 들어있는 튜플
# 괄호를 사용하지 않고 튜플 만들기
# 튜플도 리스트처럼 여러 자료형을 섞어서 저장해도 됩니다.
"""그런데 저장된 요소를 변경, 추가, 삭제할 수도 없는 튜플을 왜 만들어 놓았을까요? 이유는 간단합니다. 파이썬 프로그래밍에서 튜플을 사용하는 쪽이 더 유리한 경우도 있기 때문입니다. 보통 튜플은 요소가 절대 변경되지 않고 유지되어야 할 때 사용합니다.
튜플을 만든 상태에서 요소를 변경하게 되면 에러가 발생하게 됩니다. 따라서 요소를 실수로 변경하는 상황을 방지할 수 있습니다.
반면 요소를 자주 변경해야 할 때는 리스트를 사용합니다. 보통 실무에서는 요소를 변경하는 경우가 많기 때문에 튜플보다 리스트를 더 자주 사용하는 편입니다.
### range를 사용하여 튜플 만들기
"""
# 다음과 같이 tuple 안에 range를 넣으면 튜플이 생성됩니다.
"""range에 시작하는 숫자와 끝나는 숫자를 지정해서 튜플을 만들 수도 있겠죠? 다음은 5부터 11까지 들어있는 튜플을 만듭니다.
* `튜플 = tuple(range(시작, 끝))`
"""
"""range에 증가폭을 지정하는 방법도 가능합니다.
* `튜플 = tuple(range(시작, 끝, 증가폭))`
"""
"""### 튜플을 리스트로 만들고 리스트를 튜플로 만들기
튜플과 리스트는 요소를 변경, 추가, 삭제할 수 있는지 없는지만 다를 뿐 기능과 형태는 같습니다. 따라서 튜플을 리스트로 만들거나 리스트를 튜플로 만들 수도 있습니다.
"""
"""반대로 list 안에 튜플을 넣으면 새 리스트가 생성됩니다."""
"""## 리스트와 튜플로 변수 만들기"""
# 리스트와 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있습니다.
# 이때 변수의 개수와 리스트(튜플)의 요소 개수는 같아야 합니다.
# 리스트와 튜플 변수로도 변수 여러 개를 만들 수 있습니다.
# 다음과 같이 리스트와 튜플의 요소를 변수 여러 개에 할당하는 것을
# 리스트 언패킹(list unpacking), 튜플 언패킹(tuple unpacking)이라고 합니다.
# 리스트 패킹(list packing)과 튜플 패킹(tuple packing)은
# 변수에 리스트 또는 튜플을 할당하는 과정을 뜻합니다.