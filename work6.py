import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
rand = ["◯", "X"]


# リセットが押された時の処理
# def button_reset():


# button3が押された時の処理
def button_action():
    global action
    action = "◯"
    button3.config(text=action)


# 出力ラベルの作成
label1 = tk.Label(window, text="あなたは◯です", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# リセットボタン
button2 = tk.Button(
    window,
    text="リセット",
    # command=button_reset,
    bg=fg_color,
    fg=bg_color,
    font=("Helvetica", 25),
)
button2.pack(pady=10)

# 大きな空欄
button_frame = tk.Frame(window, bg=fg_color)
button_frame.pack(pady=10)

# 大きな空欄
button_frame2 = tk.Frame(window, bg=fg_color)
button_frame2.pack(pady=10)

# ボタンの作成
button3 = tk.Button(
    button_frame,
    text="",
    command=button_action,
    bg=fg_color,
    fg=bg_color,
    font=("Helvetica", 25),
)
button3.grid(row=0, column=0, padx=10, pady=10)

# ボタンの作成
button4 = tk.Button(
    button_frame,
    text="",
    command=button_action,
    bg=fg_color,
    fg=bg_color,
    font=("Helvetica", 25),
)
button4.grid(row=0, column=1, padx=10, pady=10)

# ボタンの作成
button5 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button5.grid(row=0, column=2, padx=10, pady=10)

# ボタンの作成
button6 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button6.grid(row=1, column=0, padx=10, pady=10, columnspan=1)

# ボタンの作成
button7 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button7.grid(row=1, column=1, padx=10, pady=10)

# ボタンの作成
button8 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button8.grid(row=1, column=2, padx=10, pady=10)

# ボタンの作成
button8 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button8.grid(row=2, column=0, padx=10, pady=10)

# ボタンの作成
button9 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button9.grid(row=2, column=1, padx=10, pady=10)

# ボタンの作成
button10 = tk.Button(
    button_frame, text="", bg=fg_color, fg=bg_color, font=("Helvetica", 25)
)
button10.grid(row=2, column=2, padx=10, pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
