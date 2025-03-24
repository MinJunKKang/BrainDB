import tkinter as tk
from gui.memory_gui import MemoryGUI
#from utils.init_memory import init_project

if __name__ == "__main__":
    #print("프로젝트 초기화 중...")
    #init_project()
    root = tk.Tk()
    app = MemoryGUI(root)
    root.mainloop()