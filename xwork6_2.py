import tkinter as tk
import random

# お約束のコード
window = tk.Tk()
window.title("GUI App")
window.geometry("600x500")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
# bg_color2 = "#FF0000"

window.configure(bg=bg_color)

maru_batu = 0


# ボタンが押された時の処理
def button_action(i, j):
    global maru_batu
    if buttons[i][j].cget("text") == "":
        if maru_batu == 0:
            buttons[i][j].config(text="◯")
            maru_batu = 1
            if maru_batu == 1:
                cpu_action()
        elif maru_batu == 1:
            buttons[i][j].config(text="✖️")
            maru_batu = 0
    if check_win("◯"):
        label2.config(text="あなたの勝ちです")
    elif check_draw():
        label2.config(text="引き分けです")


# コンピュータの動きを処理する関数
def cpu_action():
    global maru_batu
    # 真ん中が空いている場合真ん中を取る
    if buttons[1][1].cget("text") == "":
        buttons[1][1].config(text="✖️")
        maru_batu = 0
        return
    # 勝利できるマスを探す
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                # 全ての空白にバツを置いてみる
                buttons[i][j].config(text="✖️")
                # もし勝利条件を満たした場合
                if check_win("✖️"):
                    label2.config(text="コンピュータの勝ちです")
                    return  # 関数の処理を終了する
                buttons[i][j].config(text="")

    # 勝利できるマスがない場合、防御にまわる
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                # 全ての空白にマルを置いてみる
                buttons[i][j].config(text="◯")
                # もしマルの勝利条件を満たした場合
                if check_win("◯"):
                    # バツを置いて阻止する
                    buttons[i][j].config(text="✖️")
                    maru_batu = 0
                    return  # 終了
                buttons[i][j].config(text="")

    # 勝利も防御もできない場合、ランダムに
    random_action = []
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                random_action.append((i, j))

    if random_action:
        i, j = random.choice(random_action)
        buttons[i][j].config(text="✖️")
        maru_batu = 0


# リセットボタンが押された時の処理を行う関数
def reset_action():
    global maru_batu
    for row in buttons:
        for button in row:
            button.config(text="")
            button.config(state="normal")
    label2.config(text="")
    maru_batu = 0


# ラベルを設置
label1 = tk.Label(
    window, text="あなたは◯です", bg=bg_color, fg=fg_color, font=("Helvetica", 25)
)
label1.pack(pady=10)

# リセットボタンを設置
button_set = tk.Button(
    window,
    text="リセット",
    command=reset_action,
    bg=fg_color,
    fg=bg_color,
    font=("Helvetica", 25),
)
button_set.pack(pady=10)

# ボタンをまとめて配置するフレームを作成
button_frame = tk.Frame(window, bg=fg_color)
button_frame.pack(pady=10)

# ボタンを作成して配置するループ
buttons = []
for i in range(3):
    row_button = []
    for j in range(3):
        button = tk.Button(
            button_frame,
            text="",
            command=lambda r=i, c=j: button_action(r, c),
            bg=fg_color,
            fg=bg_color,
            width=2,
            height=2,
            font=("Helvetica", 25),
        )
        button.grid(row=i, column=j, padx=10, pady=10)
        row_button.append(button)
    buttons.append(row_button)


# 勝利判定を行う関数
def check_win(a):
    for row in buttons:
        if (
            row[0].cget("text") == a
            and row[1].cget("text") == a
            and row[2].cget("text") == a
        ):
            return True

    for col in range(3):
        if (
            buttons[0][col].cget("text") == a
            and buttons[1][col].cget("text") == a
            and buttons[2][col].cget("text") == a
        ):
            return True

    if (
        buttons[0][0].cget("text") == a
        and buttons[1][1].cget("text") == a
        and buttons[2][2].cget("text") == a
    ):
        return True

    if (
        buttons[2][0].cget("text") == a
        and buttons[1][1].cget("text") == a
        and buttons[0][2].cget("text") == a
    ):
        return True

    return False


# 引き分け判定を行う関数
def check_draw():
    for row in buttons:
        for button in row:
            # ボタンに空白が残っている場合Falseを返す
            if button.cget("text") == "":
                return False
    # 空白がない場合Trueを返す
    return True


label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color, font=("Helvetica", 25))
label2.pack(pady=10)

window.mainloop()
