import random

def _isdigit(var): #올바른 입력인지 확인
    return 0 <= var <= 9

def _strike(arr1, arr2): #스트라이크(Bull) 판정
    s = 0
    for i in range(4):
        if arr1[i] == arr2[i]:
            s += 1
    return s

def _ball(arr1, arr2): #볼(Cow)판정
    b = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if i != j and arr1[i] == arr2[j]:
                b += 1
    return b

def make_answer(): #플레이어에게 입력받기 
    answer=[-1] * 4
    while -1 in answer:
        print("0~9까지의 숫자중 중복없이 4개를 입력해 주십시오:")
        answer[0] = int(input("첫번째: "))
        if  not _isdigit(answer[0]):
            print("잘못된 형식입니다. 다시입력해 주십시오")
            continue
        for i in range(1, len(answer)):
            while True:
                n = int(input(f"{i + 1}번째: "))
                if  not _isdigit(n):
                    print("잘못된 형식입니다. 다시입력해 주십시오")
                    continue
                if n in answer:
                    print("잘못된 형식입니다. 다시입력해 주십시오") 
                    continue
                answer[i] = n
                break           
    return answer

first, second, third, fourth = random.sample(range(10), 4)
answer = "%s, %s, %s, %s" % (first, second, third, fourth) #정답
count = 0 #턴수

# 판정 #

flag = True
while flag:
    # 초기화
    strike = 0
    ball = 0

    for i in range(10):
        # 판정
        cowboy=make_answer() #플레이어에게 입력받기
        strike = _strike(cowboy, list(map(int, answer.split(', '))))
        ball = _ball(cowboy, list(map(int, answer.split(', '))))
        count += 1
        print(f"판정: {strike}B{ball}C, 턴수: {count}")

        if strike == 4:
            print("정답입니다!!!")
            flag = False
            break

    print(f"정답은 {answer} 입니다. GAMEOVER")
    while True:
        choice = input("재시작을 원하면 1을 종료를 원하시면 0을 입력해주십시오: ")
        if not (choice == "1" or choice == "0"):
            continue
        else:
            flag = bool(int(choice))
            count = 0
            break
