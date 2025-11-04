class Node:
    def __init__(self, elem, next = None):
        self.data = elem # 데이터 필드
        self.link = next # 다음 노드을 가리키는 주소값을 저장(링크) 필드
        
    def append(self, new): # 현재 노드(self) 뒤에 주어진 노드(new)를 연결 연산
        if new is not None:
            new.link = self.link # new의 다음 노드는 현재 노드(self)의 다음 노드로 수정
            self.link = new  # 현재 노드(self)의 다음 노드를 new로 수정

    def popNext(self): # 현재 노드 (self)의 다음 노드를 삭제하고, 그 노드를 반환
        deleted_node = self.link # 삭제할 노드를 현재노드(self)의 다음 노드
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node
    
class LinkedList:
    def __init__(self):
        self.head = None # 비어 있는 리스트의 초기 상태

    # 주요 기본 연산
    def isEmpty(self): # 리스트의 빈 상태 검사
        return self.head is None
    
    def find_by_title(self, title):
        recent = self.head
        if recent == None: # 리스트가 빈 상태
            return None
        while recent:
            if recent.data.title == title:
                return recent.data
            recent = recent.link
        return None

    def ind_pos_by_title(self, title):
        pos = 0
        recent = self.head
        if recent == None: # 리스트가 빈 상태
            return None
        while recent:
            if recent.data.title == title:
                return pos
            recent = recent.next
            pos +=1
            return None

class Book:
    def __init__ (self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def play(self):
        return f"{self.book_id} , {self.title} , {self.author} , {self.year}"


class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        new_book = Book(book_id, title, author, year)
        new_node = Node(new_book)

        if self.books.head is None:
             self.books.head = new_node
        else:
             recent = self.books.head
             while recent.link:
                  recent = recent.link
             recent.link = new_node

        print("도서가 추가되었습니다.")
        
    def remove_book(self, title):
        recent = self.books.head
        pos = None

        while recent:
             if recent.data.title == title:
                  if pos is None:
                       self.books.head = recent.link
                  else:
                       pos.link = recent.link
                  print("도서가 삭제 되었습니다.")
                  return
             pos = recent
             recent = recent.link
                   
    def search_book(self, title):
        recent = self.books.find_by_title(title)
        if recent:
            print(f"Id: {recent.book_id}, 제목:{recent.title}, 저자:{recent.author}, 출판년도: {recent.year}")
        else:
            print("도서를 찾을 수 없습니다.")



    def display_books(self):
        recent = self.books.head
        print("전제 도서종류: ")
        while recent:
            book = recent.data
            print(f"Id: {book.book_id} , 제목: {book.title} , 저자: {book.author} , 출판년도: {book.year}")
            recent = recent.link

    def run(self):
       print("== 도서 관리 프로그램 ==")
       print("1. 도서 추가")
       print("2. 도서 삭제(책 제목으로 삭제)")
       print("3. 도서 조회(책 제목으로 조회)")
       print("4. 전체 도서 목록 출력")
       print("5. 종료") 

       while True:
            choice = input("메뉴를 선택하세요: ")
            if choice == "1":
                book_id = input("도서 ID: ")
                title = input("제목: ")
                author = input("저자: ")
                year = input("출판년도: ")
                self.add_book(book_id, title, author, year)
            elif choice == "2":
                    title = input("삭제할 도서 제목: ")
                    self.remove_book(title)
            elif choice == "3":
                title = input("조회할 도서 제목: ")
                self.search_book(title)
            elif choice == "4":
                    self.display_books()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break



if __name__ == "__main__":
    BookManagement().run()
