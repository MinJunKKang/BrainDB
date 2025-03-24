from tkinter import simpledialog

def ask_emotion():
    emotions = ["좋음", "중간", "싫음"]
    return simpledialog.askstring("감정 선택", f"감정을 선택하세요:\n{', '.join(emotions)}")