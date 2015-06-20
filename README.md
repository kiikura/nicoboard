

# ニコニコ動画風共有型プレゼンテーションツール「ニコプレ」


## 仕様検討

### 注意事項
複数プロジェクタ出力によるオーバーレイの場合、光の性質上「白」化したものを黒くすることはできない。  
そのため黒っぽい主映像が必要である。かつ文字色は白っぽい方が目立つ。

→常設ように真っ黒プレゼンを作っておく。Ctrl-Bか・・・。プレゼン用PCはデスクトップ真っ黒

### Room
board側はURLの後部をroom名にする。defaultはhackday
rabbitmqのtopicエクスチェンジでパス指定。/topic/[ルーム名]

### 管理機能
音と表示は管理者が制御できること。  
キーボード操作でいいかな。もしくはメッセージ投稿による制御でもいい。わたしがその画面端末みてないもんな。
メッセージ投稿でやろう。(隠しコマンド@admin-mute, @admin-off, @admin-on)


### アニメーション方法
CSSアニメーションにより実装。
同時作動するコメントは各グループ（naka, ue, shita)ごとに（20,5,5）で想定。
あふれた場合はキューイング（遅延実行）するか破棄。


### メッセージ
1行にする。
改行された場合別メッセージ扱い。  
※複数一括投稿用にできる口は用意する。

### コマンド検討
すべてメッセージ内に埋め込めるようにする。
@コマンド[半角英数以外の文字](一般的には空白で）

コメントコマンド
- 出力位置
@ue
@shita
@naka

- 文字サイズ
@big 大きめにする
@small 小さめにする

- 音
@chime 時間来た時用のチーン音

- 読み上げ
http://www.cyokodog.net/blog/web-speechi-api/
rate(声の速さ)とpitch（声の高さ）でも変更可能。ランダムにする？デフォルトでrate=1.2くらいにしてもいい気がするけど。
読み上げチャンネルは１つ？ちょっと現実的じゃないかな。

@speak native音声で読み上げ
@speak-ja 「Google 日本人」音声で読み上げ
@speak-en 「Google US English」「Google UK English Male」「Google UK English Female」でランダム。


- 表示タイミング
@[数値] 秒数で指定。遅延タイミングで表示。

- 文字色
@red
@pink
@yellow
@green

‘‘‘
	var NicoColors = {
//		'white'  : '#ffffff',
		'red'    : '#FF0000',
		'pink'   : '#FF8080',
		'orange' : '#FFC000',
		'yellow' : '#FFFF00',
		'green'  : '#00FF00',
		'cyan'   : '#00FFFF',
		'blue'   : '#0000FF',
		'purple' : '#C000FF',
		'black'  : '#000000',

		'white2'         : '#CCCC99',
		'niconicowhite'  : '#CCCC99',
		'red2'           : '#CC0033',
		'truered'        : '#CC0033',
		'pink2'          : '#FF33CC',
		'orange2'        : '#FF6600',
		'passionorange'  : '#FF6600',
		'yellow2'        : '#999900',
		'madyellow'      : '#999900',
		'green2'         : '#00CC66',
		'elementalgreen' : '#00CC66',
		'cyan2'          : '#00CCCC',
		'blue2'          : '#3399FF',
		'marineblue'     : '#3399FF',
		'purple2'        : '#6633CC',
		'nobleviolet'    : '#6633CC',
		'black2'         : '#666666'
	};
‘‘‘


### emoji検討
:xxx: で表記する。
http://qiita.com/volpe28v@github/items/ddc8de8b1fda021de47a

emojify.js
http://hassankhan.github.io/emojify.js/
チートシート(入力時の参考に)
http://www.emoji-cheat-sheet.com/
jquery-textcomplete
http://yuku-t.com/jquery-textcomplete/


### Twitter API を調べる

Stream APIがあるみたい。裏でデータをフィードするのに使えそう

twitter stream -> worker -> board-queue -> board

課題：アプリ登録ができないモバイルの番号がうんぬんといわれる・・・。

Stream API を使ってみる： http://syncer.jp/twitter-api-create-application
Twitter Dev Center: https://dev.twitter.com/

Pythonの例
http://qiita.com/mima_ita/items/ecdf7de2fe619378beee


