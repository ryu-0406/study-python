# coding:utf-8
#メッセージの表示
import tkinter as tk
import tkinter.messagebox as tmg

#ボタンがクリックされた時の処理
def ButtonClick():
    tmsg.showinfo("テスト", "クリックされたよ")

#メインのプログラム
root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

labell = tk.Label(root, text="数を入力してね", 
font=("Helvetica", 14))
labell.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font=("Helvetica", 14) commando=ButtonClick)
button1.place(x = 220, y = 60)

root.mainloop()