# 괄호 검사 프로그램

from stack_class import Arraystack

def checkBrackets(statement):
    #  여는 괄호는 push, 닫는 괄호가 나오면 스택의 맨 위와 짝이 맞는지 확인 후 pop -> lifo

    pairs = {')' : '(', ']':'[', '}':'{'}
    openings = set(pairs.values())
    stack = Arraystack(len(statement))

    for ch in statement: # 입력 문자열 순회
        if ch in openings: # 괄호이면 스텍에 push 한다
            stack.push(ch)
        elif ch in pairs: # 닫힌 괄호이면 
            if stack.isEmpty() : # 조건2 위반(짝이 맞지 않으면)
                return False
            if stack.peek() != pairs[ch] : # 조건3 위반(짝이 맞지 않으면)
                return False
            stack.pop()
        else:
            pass # 괄호가 아니면 무시해라
        
    return stack.isEmpty() # 만약에 True이면 검사 성공, False이면 조건1 위반(수가 맞지 않음)

# 테스트 하기
def test_Brackets():
    tests = [
        "{A[(i+1)]=0;}" # True
        "if ((x<0) && (y<3)" # False
        " while (n<8)) {n++;}" # False
        "arr[(i+1]) = 0;" # False 

    ]
    for t in tests:
        print(t,"->",checkBrackets(t))

if __name__ == "__main__":
    test_Brackets

