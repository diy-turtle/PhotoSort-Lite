import json

# 設定ファイルの読み込み
with open("./user_content/config.json") as config_json:
    config_data = json.load(config_json)

print(config_data["version"])
