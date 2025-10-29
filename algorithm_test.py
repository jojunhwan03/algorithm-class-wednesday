###############################
# 예제: 리스트에서 최대값 찾는 문제
# 성능 분석 비교연산과 이동연산 기준
###############################

def find_max(A):
    n = len(A) # 입력 크기
    move = 0 # 이동 연산 횟수
    cmp = 0 # 비교 연산 횟수
    
    max_value = A[0] # 최대값 초기화
    move +=1

    for i in range(n): # 1 ~ n-1 까지 반복
        cmp +=1 # 비교연산 횟수
        if A[i] > max_value:
            max_value = A[i]
            move +=1
    return max_value , cmp , move

#=======================================================
# 정렬알고리즘
#=======================================================
def selection_sort(arr): # 선택 정렬
     a = arr[:] # 원복복사
     n = len(arr) # 입력배열 크기
     for i in range(n-1): # i 번째 위치에 최소값 선택 배치
        min_idx = i # 최소값 인덱스
        for j in range(i+1,n): # 미정렬 구간 탐색
            if a[j] < a[min_idx]: # 더 적은값을 발견
                min_idx = j
        a[i] , a[min_idx] = a[min_idx] , a[i] # i번쨰 위치와 최소값 위치 교환
     return a

def insertion_sort(arr): # 삽입 정렬
    a = arr[:] # 원복복사
    n = len(arr) # 입력배열 크기
    for i in range(1,n): # 두번쨰 요소부터 시작
        key = a[i] # 삽입할 요소
        # 삽입할 요소의 삽입 위치 찾기
        j = i - 1
        while  j >=0 and a[j] > key:
            a[j+1]  = a[j] # 뒤쪽으로 한칸 이동
            j -=1 # 왼쪽으로 한칸 이동
        a[j + 1] = key
    return a

######################
# 테스트 실행
######################

if __name__ == "__main__":
    data = [3,9,2,7,5,10,4]
    #result , cmp_count, move_count = find_max(data)
    #print(f"최대값:{result} , 비교연산 횟수:{cmp_count} , 이동연산 횟수: {move_count}")
    sorted_array = selection_sort(data)
    print(f"최대값 : {sorted_array}")

    sorted_array = insertion_sort(data)
    print(f"최대값 : {sorted_array}")