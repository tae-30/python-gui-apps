import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

"""
データ型
    変数は決まったデータ型を持つ
    int: 数値型 ex) 1, 2, 3
    str: 文字列型 ex) "Hello", "World", "0", "123", ""
    bool: 真偽値型 ex) True, False
    (new!) リスト: 複数のデータをまとめたもの ex) [1, 2, 3], ["Hello", "World"]    

Paiza 配列 -> https://paiza.jp/works/python3/primer/beginner-python4
Paiza ランダム選択 -> https://paiza.jp/works/python3/primer/beginner-python1/4005
"""

# 名簿リストの作成。ここに名前を追加していく
name_list = []

# TODO 5. ボタンを押すと名前を追加してラベルに表示する関数を作成
# Pythonで改行する文字は→”\n” (“エミリー\nマック\nジョン\n”)

# TODO 1. ラベル: 名前を入力してください

# TODO 2. エントリー: 名前を入力するための入力フィールド

# TODO 3. ボタン: ボタンを押すと配列に名前が追加される

# TODO 4. ラベル: 配列に追加された名前を表示する

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
