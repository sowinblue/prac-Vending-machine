import tkinter as tk
from tkinter import messagebox

class ProManage:
    def __init__(self):
        self.menu = {}
    
    def product_plus(self):
        # 예제용 기본 메뉴
        self.menu = {
            1: {"name": "콜라", "price": 1200, "counts": 5},
            2: {"name": "사이다", "price": 1000, "counts": 3},
            3: {"name": "커피", "price": 1500, "counts": 2},
            4: {"name": "초코바", "price": 800, "counts": 4},
            5: {"name": "과자", "price": 900, "counts": 0},
        }

    def pro_select(self, number):
        if number not in self.menu:
            return None, "존재하지 않는 번호입니다."
        
        item = self.menu[number]
        if item["counts"] <= 0:
            return None, f"{item['name']}은(는) 품절입니다."
        
        # 재고 감소
        item["counts"] -= 1
        return item, f"{item['name']} 선택 완료! 가격: {item['price']}원"

# --------------------- GUI ---------------------
class VendingGUI:
    def __init__(self, master, machine):
        self.master = master
        self.machine = machine
        self.machine.product_plus()  # 기본 메뉴 세팅

        master.title("자판기")

        self.label = tk.Label(master, text="상품 선택 (1~5)")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.select_button = tk.Button(master, text="선택", command=self.select_item)
        self.select_button.pack()

        self.menu_button = tk.Button(master, text="메뉴 보기", command=self.show_menu)
        self.menu_button.pack()

    def select_item(self):
        try:
            number = int(self.entry.get())
        except ValueError:
            messagebox.showerror("오류", "번호를 입력하세요!")
            return
        
        item, msg = self.machine.pro_select(number)
        messagebox.showinfo("결과", msg)

    def show_menu(self):
        menu_text = ""
        for num, info in self.machine.menu.items():
            menu_text += f"{num}. {info['name']} - {info['price']}원, 재고: {info['counts']}개\n"
        messagebox.showinfo("현재 메뉴", menu_text)

# --------------------- 실행 ---------------------
if __name__ == "__main__":
    root = tk.Tk()
    machine = ProManage()
    gui = VendingGUI(root, machine)
    root.mainloop()
