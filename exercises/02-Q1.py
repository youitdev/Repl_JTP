# 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

# 과목	점수
# 국어	80
# 영어	75
# 수학	55

## 방법0: 그냥 계산
print((80+75+55)/3)

## 방법1: 변수 이용
a = 80
b = 75
c = 55

e = (a+b+c)/3

print(e)


## 함수 이용
a, b, c = 80, 75, 55
def average(a, b, c):
    """
    a: 국어 점수
    b: 영어 점수
    c: 수학 점수
    """
    return (a+b+c)/3

print(average(a, b, c))


## 과목 수가 정해지지 않은 경우는?
# def average(**kwargs):
#   ....
#     return ....