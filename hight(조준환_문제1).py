n = int(input("계단의 개수를 입력하시오: "))

hight = [0] * (n + 1)
hight[0] = 1
hight[1] = 1

for i in range(2, n + 1):
    hight[i] = hight[i-1] + hight[i-2]

print(f"{n}개의 계단을 오르는 방법의 수는 {hight[n]}가지입니다.")