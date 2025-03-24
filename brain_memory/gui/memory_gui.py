import tkinter as tk
from tkinter import ttk, messagebox
from utils.memory_store import save_to_short_term, clean_expired_memory

class MemoryGUI:
    def on_save(self):
        content = self.input_entry.get()
        if not content.strip():
            messagebox.showwarning("입력값이 비어있습니다.")
            return
        
        save_to_short_term(content)
        self.output_text.insert("end", f"[Saved] {content}\n")
        self.input_entry.delete(0, "end")

    def on_clean_expired(self):
        removed = clean_expired_memory()
        self.output_text.insert("end", f"[Expired Removed] {removed} item(s) deleted\n")

    def __init__(self, root):
        self.root = root
        self.root.title("Brain Memory System")
        self.root.geometry("600x500")
        
        # 입력창 프레임
        self.input_frame = ttk.LabelFrame(root, text="Input Memory")
        self.input_frame.pack(fill="x", padx=10, pady=10)
        self.input_entry = ttk.Entry(self.input_frame, width=70)
        self.input_entry.pack(padx=10, pady=5)
        self.save_button = ttk.Button(self.input_frame, text="Save", command=self.on_save)
        self.save_button.pack(pady=5)

        # 검색창 프레임
        self.search_frame = ttk.LabelFrame(root, text="Search Memory")
        self.search_frame.pack(fill="x", padx=10, pady=10)
        self.search_entry = ttk.Entry(self.search_frame, width=70)
        self.search_entry.pack(padx=10, pady=5)
        self.search_button = ttk.Button(self.search_frame, text="Search")
        self.search_button.pack(pady=5)

        # TTL 정리 버튼
        self.clean_button = ttk.Button(self.search_frame, text="Clean Expired", command=self.on_clean_expired)
        self.clean_button.pack(pady=5)

        # 출력창 프레임
        self.output_frame = ttk.LabelFrame(root, text="Output")
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.output_text = tk.Text(self.output_frame, height=15)
        self.output_text.pack(padx=10, pady=5, fill="both", expand=True)
