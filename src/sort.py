import os
import json

# 設定ファイルの読み込み
with open("./user_content/config.json") as config_json:
    config_data = json.load(config_json)

# 拡張子が含まれているかを調べるプログラム
def is_include(filename):
    file_extensions = config_data["extensions"]
    for i in range(len(file_extensions)):
        if filename.lower().find(file_extensions[i]) != -1:
            return file_extensions[i]
    return False

# 写真を並べ替えるプログラム
def PhotoSort_lite():
    file_name_list = os.listdir(config_data["folder"])

    # 画像、動画ファイルのリネーム
    for i in range(len(file_name_list)):
        file_pass = config_data["folder"] + file_name_list[i]
        if is_include(file_name_list[i]) != False:
            print("リネーム後のファイル名 :" + file_name_list[i])
            took_time = os.stat(file_pass).st_ctime
            os.rename(file_pass, config_data["folder"] + str(took_time).replace(".", "") + "." + is_include(file_name_list[i]))

    print("完了しました")
    return "finish"
