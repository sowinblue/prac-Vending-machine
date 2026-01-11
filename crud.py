

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
    

    def b_delete(self):
        number = int(input("지우고 싶은 건의 사항 번호"))
        index = number -1
        del self.comments[index]
        return
    

    
