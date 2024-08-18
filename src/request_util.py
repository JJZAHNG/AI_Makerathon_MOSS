import hashlib
import hmac
import base64
import time
import json
import urllib.parse
import requests
import wave
import os


class authorization:
    def __init__(self):
        self.SecretId = "AKIDRkrKDWo2HrPuhWQd9y7PNaoz7Zdqrq4G"  # 替换为你的SecretId
        self.SecretKey = "hitzdYVRkz40P9wjJBFT3iL3oXC84JuS"  # 替换为你的SecretKey
        self.AppId = 1303109784  # 替换为你的AppId
        self.Expired = 3600  # 设置请求的过期时间

    def init(self):
        pass

    def generate_sign(self, request_data):
        # 拼接签名原文字符串
        sorted_params = sorted(request_data.items())
        params_str = urllib.parse.urlencode(sorted_params)
        sign_str = f"POSTtts.cloud.tencent.com/stream?{params_str}"

        print(f"Sign String: {sign_str}")  # 调试输出

        # 使用 HmacSHA1 算法计算签名
        hash_hmac = hmac.new(self.SecretKey.encode('utf-8'), sign_str.encode('utf-8'), hashlib.sha1)
        signature = base64.b64encode(hash_hmac.digest()).decode('utf-8')

        print(f"Generated Signature: {signature}")  # 调试输出

        return signature


class request:
    def __init__(self):
        self.Codec = 'pcm'
        self.ModelType = 1
        self.PrimaryLanguage = 1
        self.ProjectId = 0
        self.SampleRate = 16000
        self.SessionId = str(int(time.time()))  # 可以使用时间戳生成SessionId
        self.Speed = 0  # 语速（-2至2之间）
        self.Text = ''
        self.VoiceType = 1007  # 默认中文女声
        self.Volume = 5  # 音量（0至10之间）

    def init(self, text=''):
        self.Text = text


def generate_speech(text, output_file="output.wav"):
    req = request()
    req.init(text=text)  # 初始化请求文本
    auth = authorization()
    auth.init()

    request_data = {
        'Action': 'TextToStreamAudio',
        'AppId': auth.AppId,  # 确保 AppId 是整数
        'Codec': req.Codec,
        'Expired': int(time.time()) + auth.Expired,
        'ModelType': req.ModelType,
        'PrimaryLanguage': req.PrimaryLanguage,
        'ProjectId': req.ProjectId,
        'SampleRate': req.SampleRate,
        'SecretId': auth.SecretId,
        'SessionId': req.SessionId,
        'Speed': req.Speed,
        'Text': req.Text,
        'Timestamp': int(time.time()),
        'VoiceType': req.VoiceType,
        'Volume': req.Volume
    }

    signature = auth.generate_sign(request_data=request_data)
    header = {
        "Content-Type": "application/json",
        "Authorization": f"TC3-HMAC-SHA256 Credential={auth.SecretId}/{int(time.time())}, SignedHeaders=content-type;host, Signature={signature}"
    }

    url = "https://tts.cloud.tencent.com/stream"

    response = requests.post(url, headers=header, data=json.dumps(request_data), stream=True)

    if response.status_code != 200 or str(response.content).find("Error") != -1:
        print("Error in TTS request:", response.content)
        return

    with wave.open(output_file, 'wb') as wavfile:
        wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
        for chunk in response.iter_content(1000):
            wavfile.writeframes(chunk)

    print(f"Audio saved to {output_file}")


if __name__ == '__main__':
    test_text = "这是一个测试。"
    generate_speech(test_text)
    os.system("mpg321 output.wav")
