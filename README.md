# PhotoSort-Lite
![GitHub License](https://img.shields.io/github/license/diy-turtle/PhotoSort-Lite)
![GitHub top language](https://img.shields.io/github/languages/top/diy-turtle/PhotoSort-Lite)
![GitHub Release](https://img.shields.io/github/v/release/diy-turtle/PhotoSort-Lite)

軽量版写真、動画リネームソフト

## 特徴
- 軽量動作
- 撮影日時によるリネーム (Unix 時間)

## 使い方
### 1. **ファイルのダウンロードまたはクローン**
以下のいずれかの方法で、PhotoSort-Lite のプログラムを自分のPCにダウンロードしてください。
    - ダウンロード
        - **https://github.com/diy-turtle/PhotoSort-Lite.git** から最新版のZIPファイルをダウンロードし、解凍します。
    - クローン
        - ターミナルまたはGit GUIツールを使って、以下のコマンドを実行します。
```
git clone https://github.com/diy-turtle/PhotoSort-Lite
```


### 2. **config.json ファイルの作成**

config.jsonファイルは、PhotoSort-Liteの設定を保存するファイルです。以下の内容を参考に、config.jsonファイルを作成してください。

#### config.json
```json
{
    "version": "1.0.0",
    "type": "lite",
    "folder": "./user_content/upload/",
    "extensions": ["jpg", "gif", "png", "mov"]
}
```

#### config.jsonの詳細
| キー | 内容 | 必須 | 規定値 |
| --- | --- | --- | --- |
| version | config.json が作成されたときの PhotoSort-Lite のバージョン | はい | 1.0.0 |
| type | 軽量版かどうかを表します。| はい | lite |
| folder | PhotoSort-Lite でリネームする写真があるフォルダを表します。 | はい | ./user_content/upload/ |
| extensions | リネームするファイルの拡張子を保存します。 | はい | jpg, gif, png, mov |

### 3. プログラムの実行

