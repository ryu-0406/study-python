# coding:utf-8
import tkinter as tk

# 円の座標
x = 300
y = 200

def click(event):
    global x, y
    # いまの円を消す
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white, width=0")

#　ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

#　キャンバスを描く
canvas =tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

#　イベントを設定する
canvas.bind("<Button-1>", click)

root.mainloop()