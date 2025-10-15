# stack_class.py
#################################

# array로 구성된 stack 클래스

# 메소드: isEmpty, isFull, push, pop, peek, top

class Arraystack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self) :
        return self.top == self.capacity

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
            print(f"push: {item!r} -> stack = {self.array[:self.top+1]} ")
        else :
            raise OverflowError("stack overflow") # pass , exit(1)
        
    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print(f"pop: {item!r} -> stack = {self.array[:self.top+1]} ")
            return item
        else:
            raise IndexError("stack underflow")


    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        return None
    
    def size(self):
        return self.top+1
    

# 스택 클래스를 이용한 문자열을 반대로 출력하는 프로그램

def reverse_string(statement):
    print("\n[1] push단계 -----------------------")
    st = Arraystack(len(statement))
    for ch in statement :
        st.push(ch)
    
    print("\n[1] pop단계 -----------------------")
    out = []
    while not st.isEmpty():
        out.append(st.pop())
    result = ''.join(out)
    print(f"\n[3] 최종결과: {result}")
    return result

#테스트하기
def test_reverse():
    tests = ["토마토","안녕하세요","반갑습니다","1234567890"]
    
    for s in tests:
        got = reverse_string(s)
    
if __name__ == "__main__":
    test_reverse()



    
            

    
