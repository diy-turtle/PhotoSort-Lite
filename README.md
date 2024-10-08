# PhotoSort-Lite
![GitHub License](https://img.shields.io/github/license/diy-turtle/PhotoSort-Lite)
![GitHub top language](https://img.shields.io/github/languages/top/diy-turtle/PhotoSort-Lite)
![GitHub Release](https://img.shields.io/github/v/release/diy-turtle/PhotoSort-Lite)

軽量版写真・動画リネームソフト

![ver1_0_1 - スクリーンショット](https://github.com/user-attachments/assets/33a6de66-b3b6-4f3b-bc3d-54c65543aa44)

## 主な特徴
- 軽量で高速な動作
- 作成日時によるリネーム (Unix 時間)

## 使い方
### 1. **ファイルのダウンロードまたはクローン**
以下のいずれかの方法で、PhotoSort-Lite ソフトウェアを自分のPCにダウンロードしてください。
- ダウンロード
    - **https://github.com/diy-turtle/PhotoSort-Lite.git** から最新版のZIPファイルをダウンロードし、解凍します。
- クローン
    - ターミナルまたはGit GUIツールを使って、以下のコマンドを実行します。
```
git clone https://github.com/diy-turtle/PhotoSort-Lite
```


### 2. **config.json ファイルの作成**

config.jsonファイルは、PhotoSort-Liteの設定を保存するファイルです。以下の内容を参考に、config.jsonファイルを作成してください。ファイルは、 ./user_content/ に保存してください。

#### config.json
```json
{
    "version": "1.0.1",
    "type": "lite",
    "folder": "./user_content/upload/",
    "extensions": ["jpg", "gif", "png", "mov"]
}
```

#### config.jsonの詳細
| キー | 内容 | 必須 | 規定値 |
| --- | --- | --- | --- |
| version | config.json が作成されたときの PhotoSort-Lite のバージョン | はい | 1.0.1 |
| type | プログラムのタイプ | はい | lite |
| folder | PhotoSort-Lite でリネームする写真があるフォルダ | はい | ./user_content/upload/ |
| extensions | リネームするファイルの拡張子 | はい | jpg, gif, png, mov |

### 3. プログラムの実行
./src/main.py を実行してください。
```
cd src
python main.py
```

> [!NOTE]
> #### プログラムの役割
> | ファイル名 | 役割 |
> | --- | --- |
> | ./src/main.py | 他のプログラムの実行や GUI 画面の作成 |
> | ./src/sort.py | 写真を並び替え |


## 使用したライブラリ
### メインプログラム (main.py)
- json (https://jsons.readthedocs.io/) (Apache License 2.0)

    JSON データの読み書き
- tkinter (https://docs.python.org/3/library/tkinter.html) (Python Software Foundation License)

    Tkinter GUI ツールキット


### サブモジュール (sort.py)
- os (https://docs.python.org/3/library/os.html) (標準ライブラリ)

    オペレーティングシステムとのやり取り
  
- json (https://jsons.readthedocs.io/) (Apache License 2.0)

    JSON データの読み書き
