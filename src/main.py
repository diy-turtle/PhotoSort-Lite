import json
import tkinter as tk
import sort

# 設定ファイルの読み込み
with open("../user_content/config.json") as config_json:
    config_data = json.load(config_json)

# 使用できるバージョン
can_use_version = ["1.0.0", "1.0.1"]

# ウィンドウの作成
root = tk.Tk()
title = ""
if config_data["version"] == "1.0.1":
    title = "PhotoSort-Lite (ver1.0.1)"
elif config_data["version"] in can_use_version:
    title = "PhotoSort-Lite (互換性モード)"
else:
    title = "PhotoSort-Lite (こちらのバージョンは互換性がありません。期待する動作が得られない可能性があります。)"
root.title(title)

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
