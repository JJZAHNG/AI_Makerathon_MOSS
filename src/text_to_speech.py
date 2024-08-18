# text_to_speech.py

from aip import AipSpeech
import os
from config import APP_ID, API_KEY, SECRET_KEY  # 从配置文件导入API密钥

# 初始化AipSpeech对象
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def synthesize_speech(text):
    # 调用百度语音合成接口
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,   # 音量，范围是0-15，默认值为5
        'spd': 5,   # 语速，范围是0-9，默认值为5
        'pit': 5,   # 音调，范围是0-9，默认值为5
        'per': 4    # 发音人选择，4为情感度丫丫童声，3为情感度度逍遥，默认值为1（度小美）
    })

    # 如果合成成功，返回的是二进制音频数据
    if not isinstance(result, dict):
        output_file = 'output.mp3'
        with open(output_file, 'wb') as f:
            f.write(result)
        print("语音合成成功，文件已保存为 output.mp3")

        # 自动播放音频
        os.system(f"mpg321 {output_file}")
    else:
        # 如果合成失败，返回的是错误信息字典
        print("语音合成失败，错误信息：", result)
