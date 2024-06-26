import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
str_list = ["今日はいい天気", "昨日は雨", "今日も雨", "明日は曇り", "明日は晴れ"]
odai = random.choice(str_list)


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    global odai
    user_input_text = entry1.get()
    if odai == user_input_text:
        odai = random.choice(str_list)
        label1.config(text=odai)
    entry1.delete(0, tk.END)


# 出力ラベルの作成
label1 = tk.Label(window, text=odai, bg=bg_color, fg=fg_color, font=("Helvetica", 24))
label1.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color, font=("Helvetica", 24))
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(
    window,
    text="OK",
    command=button_action,
    font=("Helvetica", 18),
    bg=fg_color,
    fg=bg_color,
)
button1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
