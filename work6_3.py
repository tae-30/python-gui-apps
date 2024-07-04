import tkinter as tk
import random

# お約束のコード
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)


# ボタンが押された時の処理を担当するクラス
class Maru:
    def button_action(self, button):
        if button.cget("text") == "":
            button.config(text="◯")
            button.config(state="disabled")  # ボタンを無効化
            if check_win_maru():
                label2.config(text="あなたの勝ちです")
            else:
                cpu_action()


class Batu:
    def button_action(self, button):
        if button.cget("text") == "":
            button.config(text="✖️")
            button.config(state="disabled")  # ボタンを無効化
            if check_win_batu():
                label2.config(text="コンピュータの勝ちです")
            else:
                maru_action()


# コンピュータの動きを決定する関数
def cpu_action():
    # 勝利できるマスを探す
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                buttons[i][j].config(text="✖️")
                buttons[i][j].config(state="disabled")  # ボタンを無効化
                if check_win_batu():
                    return
                buttons[i][j].config(text="")

    # 勝利できるマスがない場合、防御にまわる
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                buttons[i][j].config(text="◯")
                buttons[i][j].config(state="disabled")  # ボタンを無効化
                if check_win_maru():
                    buttons[i][j].config(text="✖️")
                    return
                buttons[i][j].config(text="")

    # 勝利も防御もできない場合、ランダムに配置する
    random_action = []
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                random_action.append((i, j))

    if random_action:
        i, j = random.choice(random_action)
        buttons[i][j].config(text="✖️")
        buttons[i][j].config(state="disabled")  # ボタンを無効化


# 人間の動きを決定する関数
def maru_action():
    # 勝利できるマスを探す
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                buttons[i][j].config(text="◯")
                buttons[i][j].config(state="disabled")  # ボタンを無効化
                if check_win_maru():
                    return
                buttons[i][j].config(text="")


# ボタンが押された時の処理を行う関数
def button_action(i, j):
    if buttons[i][j].cget("state") == "normal":  # ボタンが有効な場合のみ
        maru_instance = Maru()
        maru_instance.button_action(buttons[i][j])


# リセットボタンが押された時の処理を行う関数
def reset_action():
    for row in buttons:
        for button in row:
            button.config(text="")
            button.config(state="normal")  # ボタンを有効化する

    label2.config(text="")


# ラベルを設置
label1 = tk.Label(window, text="あなたは◯です", bg=bg_color, fg=fg_color)
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
            font=("Helvetica", 25),
        )
        button.grid(row=i, column=j, padx=10, pady=10)
        row_button.append(button)
    buttons.append(row_button)


# 勝利判定を行う関数（◯が揃った場合）
def check_win_maru():
    for row in buttons:
        if (
            row[0].cget("text") == "◯"
            and row[1].cget("text") == "◯"
            and row[2].cget("text") == "◯"
        ):
            return True

    for col in range(3):
        if (
            buttons[0][col].cget("text") == "◯"
            and buttons[1][col].cget("text") == "◯"
            and buttons[2][col].cget("text") == "◯"
        ):
            return True

    if (
        buttons[0][0].cget("text") == "◯"
        and buttons[1][1].cget("text") == "◯"
        and buttons[2][2].cget("text") == "◯"
    ):
        return True

    if (
        buttons[2][0].cget("text") == "◯"
        and buttons[1][1].cget("text") == "◯"
        and buttons[0][2].cget("text") == "◯"
    ):
        return True

    return False


# 勝利判定を行う関数（✖️が揃った場合）
def check_win_batu():
    for row in buttons:
        if (
            row[0].cget("text") == "✖️"
            and row[1].cget("text") == "✖️"
            and row[2].cget("text") == "✖️"
        ):
            return True

    for col in range(3):
        if (
            buttons[0][col].cget("text") == "✖️"
            and buttons[1][col].cget("text") == "✖️"
            and buttons[2][col].cget("text") == "✖️"
        ):
            return True

    if (
        buttons[0][0].cget("text") == "✖️"
        and buttons[1][1].cget("text") == "✖️"
        and buttons[2][2].cget("text") == "✖️"
    ):
        return True

    if (
        buttons[2][0].cget("text") == "✖️"
        and buttons[1][1].cget("text") == "✖️"
        and buttons[0][2].cget("text") == "✖️"
    ):
        return True

    return False


# お約束のコード
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color, font=("Helvetica", 25))
label2.pack(pady=10)

window.mainloop()
