# coffee.py 여러가지 기능 추가할 수 있음
coffee = 10
while True:
    print('Python Coffee machine\n나가기:1004입력\n')
    try:
        money = int(input('요청:돈을 넣어라: '))
    except ValueError:
        print('응답:돈만 넣어라\n')
        continue
    if money == 300:
        print('응답:커피준다')
        coffee -= 1
        print(f'남은커피 {coffee}잔 남았다\n')
    elif money == 1004:
        print('종료:잘가')
        break
    elif money > 300:
        print(f'응답:잔돈 {money - 300}준다 커피도 준다')
        coffee -= 1
        print(f'남은커피 {coffee}잔 남았다\n')
    else:
        print('응답:돈 부족하다. 커피 안준다')
        print(f'남은커피 {coffee}잔 남았다\n')
    if coffee == 0:
        print('종료:남은커피 없다. 커피 안판다')
        break