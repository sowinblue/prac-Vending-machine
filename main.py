from manage import ProManage
from crud import SuggestionBoard



def main():
    pm = ProManage()
    board = SuggestionBoard()

    pm.product_plus()

    while True:
        print("\n1. 상품 보기  2. 구매  3. 건의사항 관리  0. 종료")
        menu = input("선택: ")

        if menu == "1":
            pm.show_menu()

        elif menu == "2":
            item = pm.pro_select()
            print(f"{item['name']} 구매 완료")


        elif menu == "3":
            while True:
                print("\n[건의사항]")
                print("1. 등록  2. 조회  3. 수정  4. 삭제  0. 뒤로")
                sub = input("선택: ")

                if sub == "1":
                    board.b_create()
                elif sub == "2":
                    board.b_read()
                elif sub == "3":
                    board.b_update()
                elif sub == "4":
                    board.b_delete()
                elif sub == "0":
                    break
                else:
                    print("잘못된 입력")

        elif menu == "0":
            print("종료")
            break

        else:
            print("잘못된 입력")


if __name__ == "__main__":
    main()
