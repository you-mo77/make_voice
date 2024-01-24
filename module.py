import numpy as np
import soundfile as sf

# 基底音作成 (A, f, sec, fs -> 基底音)
def make_base_voice(A, f, sec, fs):
    # 時間軸生成
    t = np.arange(0, sec, 1/fs)

    # 基底音(f[Hz])
    base_voice = A * np.sin(2 * np.pi * f * t)

    return base_voice

# 声帯音声作成 (A, f, sec, fs, 基底音, n -> 声帯音声(基底音 + 倍音))
def make_voice_cords(A, f, sec, fs, base_voice, n):
    # 時間軸生成
    t = np.arange(0, sec, 1/fs)

    # 倍音生成(どうやら基底音より2,3倍波程度のほうが強いっぽい・・・？)
    overtone = np.zeros(fs * sec)
    overtone += 1.1 * A * np.sin(2 * np.pi * 2 * f * t)
    overtone += 1.2 * A * np.sin(2 * np.pi * 3 * f * t)
    if n >= 4:
        for i in range(4,n+1):
            overtone += 1.2 * (30 - i) / 30 * np.sin(2 * np.pi * i * f * t)

    # 声帯音声へ
    voice_cords = base_voice + overtone

    # 正規化
    voice_cords /= max(voice_cords)

    return voice_cords

# 音声出力
def sound_output(sound:np.ndarray, fs, fname):
    # 出力
    sf.write(f"{fname}.wav", sound.T, fs)

    return

# 実行関数
def main(A, f, sec, fs, n, fname):
    base_voice = make_base_voice(A, f, sec, fs)
    voice_cards = make_voice_cords(A, f, sec, fs, base_voice, n)
    sound_output(voice_cards, fs, fname)





