import json
import tkinter as tk
import sort

# 設定ファイルの読み込み
with open("../user_content/config.json") as config_json:
    config_data = json.load(config_json)

# ウィンドウの作成
root = tk.Tk()
root.title("PhotoSort-Lite (ver1.0.1)")

# フォルダ名
folder = tk.Label(root, text="フォルダ :" + config_data["folder"])
folder.pack()

# 適応ボタン
apply_btn = tk.Button(root, text="適応", command=sort.PhotoSort_lite)
apply_btn.pack()

# 対応する拡張子
file_extensions = tk.Label(root, text="対応する拡張子 :" + str(config_data["extensions"]))
file_extensions.pack()

# ライセンス
license = tk.Label(root, text="MIT License")
license.pack()

root.mainloop()
