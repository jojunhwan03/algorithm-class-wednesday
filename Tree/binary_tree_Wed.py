# binary_tree.py
#=========================================================================
# 이진 트리를 위한 노드 클래스
# - 연결된 구조로 표현

class BTNode:
	def __init__(self,elem,left =None,right =None):
		self.data = elem # 노드의 데이터
		self.left = left # 노드의 왼쪽 자식노드 링크
		self.right = right # 노드의 오른쪽 자식노드 링크

	def __repr__(self): # 노드 객체 -> 문자열 표현 ; print 함수 호출 -> 자동으로 호출
		return f"BTNode({self.data!r}, {self.left!r}. {self.right!r})"

#============================================================================
# 예시 트리 구조:
#     A
#    /   \
#   B   C

if __name__ == "__main__":
	left_c = BTNode("B",None,None)
	right_c = BTNode("C")
	root = BTNode("A",left_c,right_c)

	print(root)
	print(root.data) # "A"
	print(root.left.data) # "B"
	print(root.right.data) # "C"

#========================================================================
# BTNode 클래스 외부에서 사용할 이진 트리의 연산 함수
# - root: 현재 노드를 나타냄. 보통 트리의 루트(root) 노드부터 시작.
# - root는 이진 트리의 노드 객체이며, .left, .right 속성을 통해 왼쪽과 오른쪽 자식 노드에 접근
#=======================================================================

def print_data(data): # 노드의 데이터를 출력하기
	if data is None: # None인 경우
		return False
	print(data, end =' ')

def is_leaf(node): # 단말노드 확인하기 
	if node is None:
		return False
	return node.left is None and node.right is None

def print_leaf_nodes(node): #  이진트리의 단말노드만 출력하기
	# 재귀적 정의: 노드가 None이면 종료, 리프노드이면  출력, 아니면 왼쪽과 오른쪽 서브트리의 단말노드 출력
	if node is None: # 재귀호출의 종료
		return
	if is_leaf(node): # 리프노드이면
		print(f"{node.data}: 단말노드")
		return
	# 리프노드가 아니면 재귀호출
	print_leaf_nodes(node.left) # 현재 노드의 왼쪽 서브트리의 단말노드 출력
	print_leaf_nodes(node.right)# 현재 노드의 오른쪽 서브트리의 단말노드 출력

def preorder(node): # 전위순회
	# 재귀적 정의: 노드가 None이면 종료, 아니면 현재 노드 방문 -> 왼쪽 서브트리 순회 -> 오른쪽 서브트리
	if node is None:
		return
	print_data(node.data) # 현재 노드의 데이터 출력
	preorder(node.left)
	preorder(node.right)

def inorder(node): # 중위순회
	# 재귀적 정의: 노드가 None이면 종료, 아니면 왼쪽 서브트리 순회 -> 현재 노드 방문 -> 오른쪽 서브트리
	if node is None:
		return
	inorder(node.left)
	print_data(node.data) # 현재 노드의 데이터 출력
	inorder(node.right)

def postorder(node): # 후위순회
	# 재귀적 정의: 노드가 None이면 종료, 아니면 왼쪽 서브트리 순회 -> 오른쪽 서브트리 순회 -> 현재 노드 방문 
	# 예 : 폴더 용량 계산, 수식트리 종료
	if node is None:
		return
	postorder(node.left)
	postorder(node.right)
	print_data(node.data) # 현재 노드의 데이터 출력

def levelorder(root): # 레벨순회
	# 예 : 너비우선탐색, 최단경로 탐색
	from collections import deque
	if	root is None:
		return
	q = deque() # 큐 생성
	q.append(root)
	while q : # 큐가 공백이 될때까지 반복 처리
		node = q.popleft() # 큐에서도 노드 추출
		print_data(node) # 방문노드 출력 : 큐에서 노드가 나오는 순서가 방문순서
		if node.left: # 현재 노드의 왼쪽 자식노드가 존재하는 경우
			q.append(node.left)
		if node.right: # 현재 노드의 오른쪽 자식노드가 존재하는 경우
			q.append(node.right)

def count_nodes(root): # 이진트리의 노드 수 = 왼쪽 서브트이의 노드 수 + 오른쪽 서브트리의 노드 수 + 1
# 재귀적 정의 : 트리가 비어있는 경우 0, 아니면 왼쪽과 오른쪽 서브트리의 노드 수 합 + 1
	if root is None:
		return 0
	return count_nodes(root.left) + count_nodes(root.right) +1

def count_leaves(node): # 이진트리의 단말노드 수 = 왼쪽 서브트이의 단말노드 수 + 오른쪽 서브트리의 단말노드 수 합산
# 재귀적 정의 : 트리가 비어있는 경우 0, 단말노드이면 1, 아니면 왼쪽과 오른쪽 서브트리의 단말노드 수 합 
	if node is None: # 재귀호출 종료
		return 0
	if is_leaf(node):
		return 1
	return count_leaves(node.left) + count_leaves(node.right)

def tree_height(root): # 이진트리의 높이
	# 재귀적 정의 : 트리가 빈 경우 0, 아니면 왼쪽 서브트리의 높이와 오른쪽 서브트리의 최대값 +1
	if root is None:
		return 0
	left_h = tree_height(root.left)
	right_h = tree_height(root.right)
	return max(left_h,right_h) + 1

def count_edges(root): # 이진트리의 간선(연결된 링크)의 수
	# 트리에 간선의 수 = 트리의 노드 수 -1
	nodes = count_nodes(root) # 트리의 노드 수
	return max(0,nodes -1) # 노드 개수가 0인 경우 음수가 나오지 않도록

def min_nodes_bitree(k): # 높이가 k인 이진트리의 최소 노드의 수
	# 최소 노드는 경사이진트리의 노드의 수와 동일
	if k >= 1:
		return k
	else:
		return 0
	
def max_nodes_bitree(k): # 높이가 k인 이진트리의 최대 노드의 수
	# 최대 노드의 수는 포화이진트리의 노드의 수와 동일
	return 2**k - 1

def count_none_links(root): # 이진트리에서 노드 수가 N이면 연결되지않은 링크 수 계산
	# N = count_nodes(root)
	# 연결되지 않은 링크 수 = 전체 링크 수 - 간선 수 = N - (N-1) = N +1
	if root is None:
		return 1 # None 링크 1개
	# return count_nodes(root) + 1
	return count_none_links(root.left) + count_none_links(root.right)

#========================================================================
# 테스트 프로그램 : QUIZ (p.127)
#============================================================================
if __name__ == "__main__":
# 예시 트리 생성
	#       A
	#      / \
	#     B   C
	#    /   / 
	#   D   E 
	#  / \
	# F  G

 F = BTNode('F')
 G = BTNode('G')
 E = BTNode ('E')
 D = BTNode('D',F,G)
 B = BTNode('B',D)
 C = BTNode	('C',E)
 root = BTNode('A',B,C)

 print("노드의 개수:", count_nodes(root))
 print("트리의 높이:", tree_height(root))
 print("간선의 수:", count_edges(root))
 print_leaf_nodes(root)
 print("높이 5인 이진트리의 최소 노드 수:", min_nodes_bitree(5))
 print("높이 5인 이진트리의 최대 노드 수:", max_nodes_bitree(5))	
 print("연결되지않은 링크 수:", count_none_links(root))
#========================================================================
# 테스트 프로그램 : 코드 4.8 p.136
#============================================================================
# if __name__ == "__main__":
#  	예시 트리 생성
#  	      A
#  	     /  \
#  	    B     C
#  	   / \   / 
#  	  D   E  F
#  	링크 표현법으로 이진트리 생성 : 단말 노드 -> 루트
# 	D = BTNode('D')
# 	E = BTNode('E')
# 	B = BTNode('B',D, E)
# 	F = BTNode('F')
# 	C = BTNode('C', F, None)
# 	root = BTNode('A', B, C)

# 	print("\n전위순회:", end=" ")
# 	preorder(root)
# 	print("\n후위순회:", end=" ")
# 	postorder(root)
# 	print("\n중위순회:", end=" ")
# 	inorder(root)
# 	print("\n레벨순회:", end=" ")
# 	levelorder(root)
# 	print()
# 	print("노드의 개수:", count_nodes(root))
# 	print("\n트리의 높이:", tree_height(root))
# 	print("\n단말노드의 개수:", count_leaves(root))
# 	print("\n간선의 수:", count_edges(root))

