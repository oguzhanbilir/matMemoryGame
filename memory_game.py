import tkinter as tk
from tkinter import messagebox
import random
import operator

class MathMemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Matematik Hafıza Oyunu")
        self.root.resizable(False, False)
        
        # Renk tanımlamaları
        self.DEFAULT_COLOR = "lightgray"
        self.OPENED_COLOR = "lightblue"
        self.MATCHED_COLOR = "lightgreen"
        
        self.buttons = []
        self.first_click = None
        self.matches_found = 0
        self.can_click = True  # Yeni: tıklama kontrolü için flag
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '//': operator.floordiv
        }
        
        self.create_cards()
        self.create_board()
    
    def create_cards(self):
        numbers = list(range(1, 13))
        self.cards = []
        self.card_values = {}
        
        while len(self.cards) < 16:
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            op = random.choice(list(self.operations.keys()))
            
            if op == '//' and (num2 == 0 or num1 % num2 != 0):
                continue
                
            result = self.operations[op](num1, num2)
            
            if result > 100 or result < -100:
                continue
                
            expression = f"{num1} {op} {num2}"
            if expression not in self.cards and str(result) not in self.cards:
                self.cards.append(expression)
                self.cards.append(str(result))
                self.card_values[expression] = result
                self.card_values[str(result)] = result
    
    def create_board(self):
        random.shuffle(self.cards)
        
        for i in range(4):
            for j in range(4):
                button = tk.Button(self.root, text="?", width=10, height=4,
                                command=lambda row=i, col=j: self.button_click(row, col),
                                bg=self.DEFAULT_COLOR,
                                font=('Arial', 10, 'bold'))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
    
    def button_click(self, row, col):
        if not self.can_click:  # Yeni: tıklama kontrolü
            return
            
        index = 4 * row + col
        button = self.buttons[index]
        
        if button["text"] == "?" and button["state"] != "disabled":
            button["text"] = self.cards[index]
            button["bg"] = self.OPENED_COLOR
            
            if self.first_click is None:
                self.first_click = button
            else:
                # İkinci kart açıldığında kontrol et
                self.can_click = False  # Yeni: tıklamayı geçici olarak devre dışı bırak
                self.root.after(1000, lambda: self.check_match(button))
    
    def check_match(self, second_button):
        if self.first_click and second_button:  # Yeni: None kontrolü
            first_value = self.card_values[self.first_click["text"]]
            second_value = self.card_values[second_button["text"]]
            
            if first_value == second_value:
                self.first_click["state"] = "disabled"
                second_button["state"] = "disabled"
                self.first_click["bg"] = self.MATCHED_COLOR
                second_button["bg"] = self.MATCHED_COLOR
                self.matches_found += 1
                
                if self.matches_found == 8:
                    messagebox.showinfo("Tebrikler!", "Oyunu kazandınız!")
                    self.reset_game()
            else:
                self.first_click["text"] = "?"
                second_button["text"] = "?"
                self.first_click["bg"] = self.DEFAULT_COLOR
                second_button["bg"] = self.DEFAULT_COLOR
            
            self.first_click = None
            self.can_click = True  # Yeni: tıklamayı tekrar etkinleştir
    
    def reset_game(self):
        self.matches_found = 0
        self.first_click = None
        self.can_click = True
        for button in self.buttons:
            button["text"] = "?"
            button["state"] = "normal"
            button["bg"] = self.DEFAULT_COLOR
        self.create_cards()
        random.shuffle(self.cards)

if __name__ == "__main__":
    root = tk.Tk()
    game = MathMemoryGame(root)
    root.mainloop()
