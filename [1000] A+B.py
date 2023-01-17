## a에 대해 설정하기
#while True : 
#    a = int(input("첫 번째 수를 0보다 크게 입력하세요. : "))
#    
#    # a의 조건에 맞는 수를 받기
#    if a>0 :
#        print(a,"를 입력받았습니다.")
#        break
#    # 조건에 맞는 수가 아닐 경우 다시 입력하라는 메세지 출력
#    else :
#        print("조건에 맞는 수를 입력해주세요.")
#
## b에 대해 설정하기
#while True :   
#    b = int(input("두 번째 수를 10보다 작게 입력하세요. : "))
#    
#    # b의 조건에 맞는 수를 받기
#    if b<10 :
#        print(b,"를 입력받았습니다.")
#        break
#    # 조건에 맞는 수가 아닐 경우 다시 입력하라는 메세지 출력
#    else :
#        print("조건에 맞는 수를 입력해주세요.")
#    
## a+b의 결과값 출력
#print("결과값은 ", a+b, "입니다.")

a, b = map(int, input().split())
print(a+b)