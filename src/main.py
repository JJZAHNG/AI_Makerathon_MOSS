# main.py

from voice_recognition import recognize_speech
from openai_interaction import get_openai_response
from text_to_speech import synthesize_speech
import os
#import audio_control  # 如果音频控制不需要，可以注释掉这行

# 如果需要初始化音频输入输出设备，可以取消注释以下行
# audio_control.set_audio_input_output()

WAKE_WORD = "小可爱"

def play_initial_voice():
    initial_voice_file = 'initial_voice.mp3'
    if os.path.exists(initial_voice_file):
        os.system(f"mpg321 {initial_voice_file}")
    else:
        print(f"启动提示音文件 {initial_voice_file} 不存在。")

def main():
    play_initial_voice()  # 首先播放启动提示音

    print("系统已启动，等待唤醒词...")

    while True:
        # 语音识别
        print("请说话...")
        recognized_text = recognize_speech()  # 在播放提示音后，再开始语音识别

        if recognized_text:
            print(f"你说的是: {recognized_text}")

            # 检查是否用户说了唤醒词
            if WAKE_WORD in recognized_text:
                print(f"唤醒词 '{WAKE_WORD}' 检测到，开始对话...")

                # 与OpenAI进行交互
                recognized_text = recognized_text.replace(WAKE_WORD, "").strip()  # 移除唤醒词
                if recognized_text:
                    response = get_openai_response(recognized_text)
                    print(f"OpenAI回应: {response}")

                    # 调用百度语音合成，将OpenAI的响应文本转换为语音
                    synthesize_speech(response)
                else:
                    print("没有有效的对话内容，等待下一次唤醒...")

            elif "退出" in recognized_text or "结束" in recognized_text:
                print("对话结束。")
                break
            else:
                print("未检测到唤醒词，继续等待...")
        else:
            print("未识别到有效的语音输入。")

if __name__ == '__main__':
    main()
