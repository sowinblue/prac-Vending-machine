

class pro_manage():
    def __init__(self):
        self.menu = {}
    
    # 물건 채우기
    def product_plus(self):
        box = range(5)
        for i in box:
            product = input("제품 명을 입력: ")
            price = int(input("가격 입력: "))
            self.menu[i+1] = {
            "name": product,
            "price": price
        }



    # 물건 교체하기
    def product_change(self):
        number = int(input("교체 제품 번호 입력: "))
        new_product = input("새로운 제품 명을 입력: ")
        self.menu[number] = new_product
        

    #확인 전용
    def show_menu(self):
        print(self.menu)


    # 조회 전용
    def get_menu(self):
        return self.menu


    def pro_select():
        print