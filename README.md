# 语音互动智能助手项目

## 项目概述

本项目是一个语音互动智能助手，通过语音识别、OpenAI 接口和语音合成，用户可以与系统进行对话。项目包括唤醒词功能，以减少不必要的 API 调用，同时在系统启动时播放提示音，提示用户系统已准备就绪。

## 功能

- **语音识别**: 使用 Vosk 语音识别库，将语音转换为文本。
- **OpenAI 交互**: 使用 OpenAI 的 GPT-4 模型，根据用户的文本输入生成对话内容。
- **语音合成**: 使用百度语音合成 API，将生成的文本转换为语音并播放。
- **唤醒词功能**: 仅在检测到唤醒词“小可爱”时才开始与 OpenAI 的对话，节省 API 调用成本。
- **启动提示音**: 系统启动时播放提示音，提示用户系统已准备好。

## 项目结构

```bash
├── src
│ ├── main.py # 主程序入口
│ ├── voice_recognition.py # 语音识别模块
│ ├── openai_interaction.py # OpenAI 交互模块
│ ├── text_to_speech.py # 语音合成模块
│ ├── config.py # 配置文件 (API keys等)
│ ├── audio_control.py # 音频输入输出设置模块 (可选)
├── README.md # 项目说明文档
└── generate_initial_voice.py # 生成启动提示音的脚本
```

## 安装指南

```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname/src
```

自动安装依赖
```bash
pip install -r requirements.txt
```

手动安装
```bash
pip install baidu-aip vosk pyaudio requests mpg321
```

## 配置API密钥
```python
# config.py

API_KEY = "your-openai-api-key"

# 百度语音合成 API
APP_ID = 'your-baidu-app-id'
API_KEY = 'your-baidu-api-key'
SECRET_KEY = 'your-baidu-secret-key'
```

## 生成启动/或者其他声音段
```bash
python generate_initial_voice.py
```


## 使用说明
确保麦克风和扬声器已正确连接，并运行主程序：
```bash
复制代码
python main.py
```
程序启动后将播放启动提示音，提示用户系统已准备好。

当你说出唤醒词“小可爱”后，系统将开始监听并与 OpenAI 进行交互，然后通过百度语音合成进行回复。

你可以随时说出“退出”或“结束”来终止对话。

## 注意事项
API 调用成本: 使用 OpenAI API 是有成本的，因此请谨慎使用。

唤醒词功能有助于减少不必要的 API 调用。

音频设备: 请确保你的音频输入输出设备配置正确，以确保最佳的使用体验。

## 贡献
欢迎贡献！如果你有任何建议或改进，请提交 issue 或 pull request。