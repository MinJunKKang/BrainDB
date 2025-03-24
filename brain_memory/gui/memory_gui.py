import tkinter as tk
from tkinter import ttk

class MemoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Memory System")
        self.root.geometry("600x500")
        
        # 입력창 프레임
        self.input_frame = ttk.LabelFrame(root, text="Input Memory")
        self.input_frame.pack(fill="x", padx=10, pady=10)
        self.input_entry = ttk.Entry(self.input_frame, width=70)
        self.input_entry.pack(padx=10, pady=5)
        self.save_button = ttk.Button(self.input_frame, text="Save")
        self.save_button.pack(pady=5)

        # 검색창 프레임
        self.search_frame = ttk.LabelFrame(root, text="Search Memory")
        self.search_frame.pack(fill="x", padx=10, pady=10)
        self.search_entry = ttk.Entry(self.search_frame, width=70)
        self.search_entry.pack(padx=10, pady=5)
        self.search_button = ttk.Button(self.search_frame, text="Search")
        self.search_button.pack(pady=5)

        # 출력창 프레임
        self.output_frame = ttk.LabelFrame(root, text="Output")
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.output_text = tk.Text(self.output_frame, height=15)
        self.output_text.pack(padx=10, pady=5, fill="both", expand=True)
