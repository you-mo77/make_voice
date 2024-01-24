import module

# 基底音振幅(基本的に1でいいはず)
A = 1
# 基底音周波数
f = 260
# 音声長(サンプル音源を作るので基本1)
sec = 1
# サンプリング周波数
fs = 48000
# 倍数音の数(2以上を想定したプログラム)
n = 20
# 出力ファイル名
fname = "test"

### 実行 ###
module.main(A, f, sec, fs, n, fname)