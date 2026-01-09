

class pro_manage():
    def __init__(self):
        self.menu = {}
    
    # 물건 채우기
    def product_plus(self):
        box = range(5)
        for i in box:
            product = input("제품 명을 입력: ")
            self.menu[i+1] = product
        
        return self.menu



    # 물건 교체하기
    def product_change(self):
        number = int(input("교체 제품 번호 입력: "))
        new_product = input("새로운 제품 명을 입력: ")
        self.menu[number] = new_product
        

    def show_menu(self):
        print(self.menu)