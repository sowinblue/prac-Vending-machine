

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


    # 물건 고르기
    def pro_select(self):
        while True:
            number = int(input("구매하실 물건의 번호를 입력: "))

            if number not in self.menu:
                print("존재하지 않는 번호입니다. 다시 선택하세요.")
                continue    # while 처음으로 돌아감

            item = self.menu[number]
            print(f"선택하신 물품은 {item['name']}, 가격은 ({item['price']}원) 입니다.")

            confirm = input("맞으면 Y, 정정하려면 N 입력: ").lower() # 사용자가 무엇을 입력하든 문자열을 전부 소문자로 변환해서 받음


            valid_yes = {"y", "yes"} 
            valid_no = {"n", "no"} 

            if confirm in valid_yes: 
                return item 
            elif confirm in valid_no: 
                print("다시 선택해주세요.")



    def money_slot(money):
        coin_allowed = [100,500]
        paper_allowed = [1000,5000,10000]
        total= 0
        
        for m in money:
            if m in coin_allowed or m in paper_allowed:
                total = total + m
            else:
                print(f"{m}원은 사용할 수 없어")

        return total



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
