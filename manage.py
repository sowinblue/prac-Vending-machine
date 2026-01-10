



class ProManage():
    def __init__(self):
        self.menu = {}
    
    # 물건 채우기
    def product_plus(self):
        box = range(5)
        for i in box:
            product = input("제품 명을 입력: ")
            price = int(input("가격 입력: "))
            count = int(input("재고 수"))
            self.menu[i+1] = {
            "name": product,
            "price": price,
            "counts": count 
        }



    # 물건 교체하기
    def product_change(self):
        number = int(input("교체 제품 번호 입력: "))
        new_product = input("새로운 제품 명을 입력: ")
        price = int(input("교체하는 제품의 가격 입력"))
        count = int(input("재고 수"))
        self.menu[number] = {
            "name": new_product,
            "price": price,
            "counts": count
        }


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

            # 번호 존재 여부
            if number not in self.menu:
                print("존재하지 않는 번호입니다. 다시 선택하세요.")
                continue

            item = self.menu[number]

            # 재고 확인
            if item["counts"] <= 0:
                print(f"{item['name']}은(는) 품절입니다. 다른 상품을 선택해주세요.")
                continue

            # 선택 확인
            print(f"선택하신 물품은 {item['name']}, 가격은 ({item['price']}원) 입니다.")


            confirm = input("맞으면 Y, 정정하려면 N 입력: ").lower()
            
            valid_yes = {"y", "yes"} 
            valid_no = {"n", "no"} 

            if confirm in valid_yes:
                # 결제 진행 전 재고 감소
                item["counts"] -= 1
                return item
            elif confirm in valid_no:
                print("다시 선택해주세요.")
            else:
                print("Yes(Y) 또는 NO(N) 중에서만 선택해 주세요")


    # 돈 결제 합산
    def insert_money(self,money):
        money_allowed = {100, 500, 1000}
        total= 0
        
        for m in money:
            if m in money_allowed:
                total = total + m
        return total 

    # 카드 결제
    def insert_card(self, card):
        card_allowed = {"visa","master","kakao","naver"}

        card = card.lower()

        if card in card_allowed:
            print(f"{card} 결제가 승인 되었습니다.")
            return True
        else:
            print("사용할 수 없는 카드 입니다.")
            return False