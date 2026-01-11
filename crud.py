

class SuggestionBoard():
    def __init__(self):
        self.comments = []

    
    def b_create(self):
        comment = input("건의 사항")
        self.comments.append(comment)
        print("건의 사항이 등록되었습니다.")


    def b_read(self):
        if not self.comments:
            print("등록된 건의 사항이 없습니다.")
            return

        print("등록된 건의 사항")
        for i, comment in enumerate(self.comments, start=1):
            print(f"{i}. {comment}")
    

    def b_update(self):
        number = int(input("수정하고 싶은 건의 사항 번호"))
        index = number - 1

        if index < 0 or index >= len(self.comments):
            print("존재하지 않는 건의 사항 입니다.")
            return

    
        new_comment = input("건의사항 수정 내용")
        self.comments[index] = new_comment
        print("수정 완료")
    

    def b_delete(self):
        number = int(input("지우고 싶은 건의 사항 번호"))
        index = number -1

        if index < 0 or index >= len(self.comments):
            print("존재하지 않는 건의 사항 입니다.")
            return
        
        del self.comments[index]
        print("삭제 되었습니다.")
        return
    



if __name__ == "__main__":
    board = SuggestionBoard()

    while True:
        print("\n1. 등록  2. 조회  3. 수정  4. 삭제  0. 종료")
        menu = input("메뉴 선택: ")

        if menu == "1":
            board.b_create()
        elif menu == "2":
            board.b_read()
        elif menu == "3":
            board.b_update()
        elif menu == "4":
            board.b_delete()
        elif menu == "0":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")


