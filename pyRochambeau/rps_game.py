import tkinter as tk
from tkinter import messagebox
import random
import json
import os

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("بازی سنگ، کاغذ، قیچی")
        self.scores = {"user": 0, "computer": 0, "draw": 0}
        self.load_scores()

        # رابط کاربری
        self.label = tk.Label(root, text="انتخاب کنید:", font=("Arial", 14))
        self.label.pack(pady=10)

        # دکمه‌ها برای انتخاب کاربر
        tk.Button(root, text="سنگ", command=lambda: self.play("سنگ"), width=10).pack(pady=5)
        tk.Button(root, text="کاغذ", command=lambda: self.play("کاغذ"), width=10).pack(pady=5)
        tk.Button(root, text="قیچی", command=lambda: self.play("قیچی"), width=10).pack(pady=5)

        # نمایش نتیجه و امتیازات
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 12))
        self.score_label.pack(pady=10)

        # دکمه‌های اضافی
        tk.Button(root, text="شروع مجدد", command=self.reset_game).pack(pady=5)
        tk.Button(root, text="نمایش آمار", command=self.show_stats).pack(pady=5)

    def load_scores(self):
        """بارگذاری امتیازات از فایل JSON"""
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as file:
                self.scores = json.load(file)

    def save_scores(self):
        """ذخیره امتیازات در فایل JSON"""
        with open("scores.json", "w") as file:
            json.dump(self.scores, file, indent=4)

    def get_score_text(self):
        """متن نمایش امتیازات"""
        return f"امتیاز شما: {self.scores['user']} | کامپیوتر: {self.scores['computer']} | مساوی: {self.scores['draw']}"

    def play(self, user_choice):
        """اجرای یک دور بازی"""
        choices = ["سنگ", "کاغذ", "قیچی"]
        computer_choice = random.choice(choices)

        # تعیین برنده
        if user_choice == computer_choice:
            result = "مساوی!"
            self.scores["draw"] += 1
        elif (user_choice == "سنگ" and computer_choice == "قیچی") or \
             (user_choice == "کاغذ" and computer_choice == "سنگ") or \
             (user_choice == "قیچی" and computer_choice == "کاغذ"):
            result = "شما بردید!"
            self.scores["user"] += 1
        else:
            result = "کامپیوتر برد!"
            self.scores["computer"] += 1

        # به‌روزرسانی رابط
        self.result_label.config(text=f"شما: {user_choice} | کامپیوتر: {computer_choice}\n{result}")
        self.score_label.config(text=self.get_score_text())
        self.save_scores()

    def reset_game(self):
        """ریست کردن بازی"""
        self.scores = {"user": 0, "computer": 0, "draw": 0}
        self.save_scores()
        self.score_label.config(text=self.get_score_text())
        self.result_label.config(text="")
        messagebox.showinfo("ریست", "بازی ریست شد!")

    def show_stats(self):
        """نمایش آمار کلی"""
        total = self.scores["user"] + self.scores["computer"] + self.scores["draw"]
        if total == 0:
            stats = "هنوز بازی انجام نشده است!"
        else:
            user_percent = (self.scores["user"] / total) * 100
            computer_percent = (self.scores["computer"] / total) * 100
            draw_percent = (self.scores["draw"] / total) * 100
            stats = (f"آمار بازی:\n"
                     f"کل دورها: {total}\n"
                     f"برد شما: {self.scores['user']} ({user_percent:.1f}%)\n"
                     f"برد کامپیوتر: {self.scores['computer']} ({computer_percent:.1f}%)\n"
                     f"مساوی: {self.scores['draw']} ({draw_percent:.1f}%)")
        messagebox.showinfo("آمار", stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()