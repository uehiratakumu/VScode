# Libraries Import
import tkinter as tk
from tkinter import ttk
import math

# Define
BUTTON = [
    ["π",'mod', 'B', 'C', '/'],
    ["sin",'7', '8', '9', '*'],
    ["tan",'4', '5', '6', '-'],
    ["cos",'1', '2', '3', '+'],
    ["000",'00', '0', '.', '=']
]

SYMBOL = ['+', '-', '*', '/']

def flague_proc(fn,b_var):
    b_var = float(b_var)  
    if fn == 1:
        fn_var = math.sin(b_var)
    elif fn == 2:
        fn_var = math.cos(b_var)
    elif fn == 3:
        fn_var = math.tan(b_var)      
    return str(fn_var)

# 簡易的な電卓を作ってみた！
class CaluGui(object):
    def __init__(self, app=None):
        # Define
        self.calc_str = '' # 計算用の文字列
        self.dis_str = '' #表示用の文字列

        # Window Setting
        app.title('電卓') # Window のタイトル
        app.geometry('350x450') # Window のサイズ

        # Frame Setting
        calc_frame = ttk.Frame(app, width=300, height=100) # 計算式と結果用のFrame
        calc_frame.propagate(False) # サイズが固定される
        calc_frame.pack(side=tk.TOP, padx=10, pady=20) # 余白の設定
        button_frame = ttk.Frame(app, width=300, height=400) # 計算ボタン用のFrame
        button_frame.propagate(False) # サイズが固定される
        button_frame.pack(side=tk.BOTTOM) # 余白の設定

        # Parts Setting
        self.calc_var = tk.StringVar() # 計算式用の動的変数
        self.dis_var = tk.StringVar() # 表示用の動的変数
        self.flague_var = tk.StringVar() # 関数管理用の動的変数
        self.var_var =tk.StringVar() # 関数の引数用の動的変数
        self.ans_var = tk.StringVar() # 結果用の動的変数
        calc_label = tk.Label(calc_frame, textvariable=self.dis_var, font=("",20)) # 計算式用のLabel
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",15)) # 結果用のLabel
        calc_label.pack(anchor=tk.E) # 右揃えで配置
        ans_label.pack(anchor=tk.E) # 右揃えで配置

        for y, row in enumerate(BUTTON, 1): # Buttonの配置
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15), width=6, height=3)
                button.grid(row=y, column=x) # 列や行を指定して配置
                button.bind('<Button-1>', self.click_button) # Buttonが押された場合
    
    def click_button(self, event):
        check = event.widget['text'] # 押したボタンのCheck

        if check == '=': # イコールの場合
            if self.calc_str[-1:] in SYMBOL: # 記号の場合、記号よりも前で計算
                self.calc_str = self.calc_str[:-1]
                self.dis_str = self.calc_str[:-1]

            res = '= ' + str(eval(self.calc_str)) # eval関数の利用
            self.ans_var.set(res)
        elif check == 'C': # クリアの場合
            self.calc_str = ''
            self.dis_str = ''
            self.ans_var.set('')
        elif check == 'B': # バックの場合
            self.calc_str = self.calc_str[:-1]
            self.dis_str = self.dis_str[:-1]
        elif check in SYMBOL: # 記号の場合
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != '':
                if self.flague_var.get() != "":
                    self.calc_str = self.calc_str + flague_proc(self.flague_var,self.var_var) +check
                    self.dis_str =  self.dis_str + self.var_var + ")"+check
                else:
                    self.calc_str += check
                    self.dis_str += check
            elif self.calc_str[-1:] in SYMBOL: # 記号の場合、入れ替える
                self.calc_str = self.calc_str[:-1] + check
                self.dis_str = self.dis_str[:-1] + check
        elif check == "π":
            t = math.pi
            self.calc_str += str(t)
            self.dis_str += "π"
        elif check == "mod":
            self.calc_str += "%"
            self.dis_str += "mod"  
        elif check == "sin":
            self.flague_var.set("1")
            self.dis_str += "sin("
            self.dis_str += self.flague_var.get()
        else: # 数字などの場合
            if self.flague_var.get() != "":
                self.var_var.set(check)
                self.dis_var.set("w")
            else:
                self.calc_str += check
                self.dis_str += check+str(self.flague_var.get())

        self.dis_var.set(self.dis_str)
        self.calc_var.set(self.calc_str)
        
    


def main():
    # Window Setting
    app = tk.Tk()
    # Window size non resizable
    app.resizable(width=False, height=False)
    CaluGui(app)
    # Display
    app.mainloop() # Window をループで回すことで Widgit に対応できるようになる

if __name__ == '__main__':
    main()