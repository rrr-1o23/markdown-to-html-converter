# Markdown to HTML Converter

#### 使用技術
<p style="display: inline">
<img src="https://img.shields.io/badge/-Linux-212121.svg?logo=linux&style=popout">
<img src="https://img.shields.io/badge/-Python-FFC107.svg?logo=python&style=popout">
<img src="https://img.shields.io/badge/-Markdown-000000.svg?logo=markdown&style=plastic">
</p>

&nbsp;

## 概要

任意のマークダウンファイルをHTMLファイルに変換するプログラムです．

#### 操作方法
ターミナルを立ち上げ以下のコマンドを実行します．
```bash
$ python main.py markdown inputfile_path outputfile_path
```
ここで，markdownは実行するコマンド，inputfile_pathは.mdファイルへのパス，
outputfile_pathはプログラム実行後に生成される.htmlファイルパスです，

#### 実行例
```bash
$ python main.py　markdown sample.md sample.html
```

&nbsp;

## 環境構築
### 開発環境
| OS・言語・ライブラリ | バージョン |
| :------- | :------ |
| Ubuntu | 22.04.4 LTS |
| Python | 3.10.12 |
| python-markdown | 3.6 |
<br>

### python-markdownのインストール手順

https://pypi.org/project/Markdown/

**Ubuntu**<br>
```bash
$ pip install markdown
```

&nbsp;
