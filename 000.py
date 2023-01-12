# num = 단수, until9 = 9단까지 곱하는 수들
num = int(input("단수를 입력하세요."))
until9 = range(1, 10)

# 구구단 형식에 맞추어 출력
for i in until9 :
    print(num,"*",i,"=",num*i)