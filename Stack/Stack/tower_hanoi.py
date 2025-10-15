
#하노이 탑 문제: 재귀적으로 문제 해결

def tower_hanoi(n,start,tmp,target):
    if n == 1:
    # 1. 재귀 호출 종료(base case)
        print(f"원판 {n} : {start} -> {target}")
#재귀 분할
    else:
    # 위의 n-1개 원판을 start -> tmp로 옮김 (C 막대를 보조 막대)
        tower_hanoi(n-1,start,target,tmp) # 왼쪽 서브 트리 재귀 순회

    # 가장 큰 1개 원판을 start -> target으로 이동 출력 # 부모 노드 출력
        print(f"원판 {n} : {start} -> {target}")

    # tmp 에 있는 n-1개 원판을 tmp-> target 으로 옮김(start를 보조 막대)
        tower_hanoi(n-1,tmp,start,target) # 오른쪽 서브 트리 재귀 순회

    if __name__ == "__main__":
        n = 4
        tower_hanoi(n,'A','B','C')

        total = ( 1 << n ) -1
        3
        print(f"\n 총 이동 횟수: {total} {2^{n} - 1}")
