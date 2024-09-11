import tkinter as tk
from datetime import datetime


window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"
fg_color = "white"
highlight_color = "white"

row_cou = 3
# today = datetime.today()


# エンターが押されたときに新しい入力欄を作成し計算する処理
def enter_action(event):
    global row_cou
    today = datetime.today()
    try:
        money = int(money_entry.get())
        money2 = int(money_entry2.get())
        money_calc = money - money2
        money_entry.delete(0, tk.END)
        money_entry.insert(0, str(money_calc))
    # エラーが起きた場合、passする
    except ValueError:
        pass
    # 商品名を保存
    new_label = tk.Label(
        frame,
        text="",
        bg=bg_color,
        fg=fg_color,
        font=("Times", 20),
        highlightbackground=highlight_color,
        highlightthickness=1,
    )
    new_label.grid(row=row_cou, column=1)
    new_label.config(text=name_entry2.get())
    # 金額を保存
    new_label2 = tk.Label(
        frame,
        text="",
        bg=bg_color,
        fg=fg_color,
        font=("Times", 20),
        highlightbackground=highlight_color,
        highlightthickness=1,
    )
    new_label2.grid(row=row_cou, column=2)
    new_label2.config(text=money_entry2.get())
    # 日付を保存
    new_label3 = tk.Label(
        frame,
        text=today.strftime("%m-%d"),
        bg=bg_color,
        fg=fg_color,
        font=("Times", 20),
        highlightbackground=highlight_color,
        highlightthickness=1,
    )
    new_label3.grid(row=row_cou, column=0)
    # day_get = day_label.get()
    # new_label3.config(text=day_get)

    # day_entry.delete(0, tk.END)
    name_entry2.delete(0, tk.END)
    money_entry2.delete(0, tk.END)

    row_cou += 1
    name_entry2.focus_set()


# 右矢印が押された時のカーソルの動き
def right_action(event):
    focus = window.focus_get()

    if focus == name_entry2:
        money_entry2.focus_set()
    # elif focus == money_entry2:
    #     pass


# 左矢印が押された時のカーソルの動き
def left_action(event):
    focus = window.focus_get()

    if focus == money_entry2:
        name_entry2.focus_set()
    # elif focus == name_entry2:
    #     pass


# 上矢印が押された時のカーソルの動き
def up_action(event):
    focus = window.focus_get()

    if focus == money_entry2 or focus == name_entry2:
        money_entry.focus_set()
    elif focus == money_entry:
        name_entry2.focus_set()


# 下矢印が押された時のカーソルの動き
def down_action(event):
    focus = window.focus_get()

    if focus == money_entry:
        name_entry2.focus_set()
    elif focus == name_entry2:
        money_entry.focus_set()


label1 = tk.Label(window, text="家計簿", bg=bg_color, fg=fg_color, font=("Times", 40))
label1.pack(pady=10)

frame = tk.Frame(window, bg=bg_color)
frame.pack(pady=10)


label2 = tk.Label(frame, text="残り", bg=bg_color, fg=fg_color, font=("Times", 25))
label2.grid(row=0, column=0)

# 残りの金額を表示する欄
money_entry = tk.Entry(
    frame,
    text="",
    bg=bg_color,
    fg=fg_color,
    font=("Times", 25),
    highlightbackground=highlight_color,
    highlightthickness=1,
)
money_entry.grid(row=0, column=1)
money_entry.bind("<Up>", up_action)
money_entry.bind("<Down>", down_action)

label3 = tk.Label(frame, text="円", bg=bg_color, fg=fg_color, font=("Times", 25))
label3.grid(row=0, column=2, sticky="w")

day = tk.Label(frame, text="日付", bg=bg_color, fg=fg_color, font=("Times", 20))
day.grid(row=1, column=0)

buy_label = tk.Label(frame, text="用途", bg=bg_color, fg=fg_color, font=("Times", 20))
buy_label.grid(row=1, column=1)

money_label = tk.Label(frame, text="金額", bg=bg_color, fg=fg_color, font=("Times", 20))
money_label.grid(row=1, column=2)


# 日付を表示
day_label = tk.Label(
    frame,
    text=datetime.today().strftime("%m-%d"),
    bg=bg_color,
    fg=fg_color,
    font=("Times", 20),
    width=5,
    highlightbackground=highlight_color,
    highlightthickness=1,
)
day_label.grid(row=2, column=0, sticky="w")

# 商品名を入力する欄
name_entry2 = tk.Entry(
    frame,
    text="",
    bg=bg_color,
    fg=fg_color,
    font=("Times", 20),
    width=15,
    highlightbackground=highlight_color,
    highlightthickness=1,
)
name_entry2.grid(row=2, column=1)
name_entry2.bind("<Return>", enter_action)
name_entry2.bind("<Right>", right_action)
name_entry2.bind("<Left>", left_action)
name_entry2.bind("<Up>", up_action)
name_entry2.bind("<Down>", down_action)

# 金額を入力する欄
money_entry2 = tk.Entry(
    frame,
    text="",
    bg=bg_color,
    fg=fg_color,
    font=("Times", 20),
    width=15,
    highlightbackground=highlight_color,
    highlightthickness=1,
)
money_entry2.grid(row=2, column=2)
money_entry2.bind("<Return>", enter_action)
money_entry2.bind("<Right>", right_action)
money_entry2.bind("<Left>", left_action)
money_entry2.bind("<Up>", up_action)
money_entry2.bind("<Down>", down_action)

window.mainloop()
