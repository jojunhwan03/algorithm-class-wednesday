import time
import sys

sys.setrecursionlimit(2000)

def factorial_iter(n): # 반복문

    result = 1
    for k in range(2,n+1):
        result *=k
    return result

def factorial_rec(n): # 재귀

    if n ==1:
        return 1
    else:
        return n *  factorial_rec(n-1)



def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = 1000

if __name__ == "__main__":
    # n = int(input("\n정수를 입력하세요: ").strip())
    # print(f"반복문 기반: {factorial_iter(n)}")
    # try:
    #     print(f"재귀 기반: {factorial_rec(n)}")
    # except RecursionError:
    #     print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
    
    print("1) 반복법으로 n! 계산\n"
    "2) 재귀로 n! 계산\n" \
    "3) 두 방식 모두 계산 후 결과 시간 비교\n" \
    "4) 준비된 테스트 데이터 일괄 시행\n" \
    "5) 종료")

    list =[0,1,2,3,5,10,15,20,30,50,100]

    s = int(input("\n선택: "))
    # n = int(input("\n정수n 을 입력해주세요: "))   
    # if n <= 0:
    #         print("\n정수 (0이상의 숫자)만 입력하세요.")
    #         exit()
    if s== 1:
        n = int(input("\n정수n 을 입력해주세요: "))   
        if n <= 0:
            print("\n정수 (0이상의 숫자)만 입력하세요.")
            exit()
        print(f"반복문 기반: {factorial_iter(n)}")
    elif s == 2: 
        n = int(input("\n정수n 을 입력해주세요: "))   
        if n <= 0:
            print("\n정수 (0이상의 숫자)만 입력하세요.")
            exit()
        try:
            print(f"재귀 기반: {factorial_rec(n)}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
    elif s == 3:
        start = time.perf_counter()
        n = int(input("\n정수n 을 입력해주세요: "))   
        if n <= 0:
            print("\n정수 (0이상의 숫자)만 입력하세요.")
            exit()
        print(f"반복문 기반: {factorial_iter(n)}")
        result = sum(range(1000000))
        end = time.perf_counter()
        print(f"반복문 실행 시간: {end - start:.6f}초")
        start = time.perf_counter()
        try:
            print(f"재귀 기반: {factorial_rec(n)}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
        result = sum(range(1000000))
        end = time.perf_counter()
        print(f"재귀문 실행 시간: {end - start:.6f}초")
        if factorial_iter(n) == factorial_rec(n):
            print("결과 일치 여부:일치")

    elif s== 4:
        for i in range(len(list)):
            try:
                sum = factorial_rec(list[i])
            except RecursionError:
                print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

            if factorial_iter(list[i]) == sum:
                same = "True"
            else:
                same = "False"

            start = time.time() 
            ter_result = factorial_iterative(n)
            end = time.time()

            start = time.time()
            try:
                recur_result = factorial_recursive(n)
            except RecursionError:
                print("[재귀] RecursionError 발생!")
            recur_end = time.time()

            print(f"n = {list[i]} | same = {same} | " 
                f"iter ={end - start:.6f} | rec = {recur_end - start:.6f} | "
                  f"{i}! = {factorial_iter(list[i])}")

    elif s == 5:
        exit()