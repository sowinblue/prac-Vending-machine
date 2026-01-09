

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
        new_price = int(input("가격 입력: "))
        self.menu[number] = {
            "name": new_product,
            "price": new_price
        }
        

    #확인 전용
    def show_menu(self):
        print(self.menu)


    # 조회 전용
    def get_menu(self):
        return self.menu


    # 물건 고르기
    def pro_select(self):
        number = int(input("구매하실 물건을 선택하세요"))
        if number in self.menu:
            item = self.menu[number] 
            return item
        print(item)


if __name__ == "__main__":
    machine = pro_manage()

    print("=== 자판기 채우기 ===")
    machine.product_plus()

    print("\n=== 현재 자판기 상태 ===")
    machine.show_menu()

    print("\n=== 상품 교체 ===")
    machine.product_change()

    print("\n=== 교체 후 상태 ===")
    machine.show_menu()

    print("\n=== 상품 선택 ===")
    item = machine.pro_select()
    print("선택된 상품:", item)

    print("\n===물건 고르기===")
    machine.pro_select(self)

    print("\n===머니슬록===")
    machine.money_slot(money)


    
