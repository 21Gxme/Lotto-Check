import requests
from bs4 import BeautifulSoup
import tkinter as tk


url = "https://www.lottery.co.th/small"
data = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(data.text, "html.parser")
lottery = soup.find_all("button", {"class": "btn-primary"})
lottery_list = []
for i in lottery:
    lottery_list.append(i.text)
print(lottery_list)


root = tk.Tk()
root.title("Lottery")
root.geometry("300x200")
root.resizable(False, False)
msg1 = tk.Label(root, text="รางวัลที่ 1", font=("Arial", 20))
msg1.grid(row=0, column=0, padx=10, pady=10)
reward = tk.Label(root, text=lottery_list[0], font=("Arial", 20))
reward.grid(row=0, column=1, padx=10, pady=10)
msg2 = tk.Label(root, text="เลขท้าย 2 ตัว", font=("Arial", 20))
msg2.grid(row=1, column=0, padx=10, pady=10)
reward = tk.Label(root, text=lottery_list[1], font=("Arial", 20))
reward.grid(row=1, column=1, padx=10, pady=10)
msg3 = tk.Label(root, text="เลขท้าย 3 ตัว", font=("Arial", 20))
msg3.grid(row=2, column=0, padx=10, pady=10)
reward = tk.Label(root, text=lottery_list[2], font=("Arial", 20))
reward.grid(row=2, column=1, padx=10, pady=10)
reward = tk.Label(root, text=lottery_list[3], font=("Arial", 20))
reward.grid(row=2, column=2, padx=10, pady=10)
msg4 = tk.Label(root, text="เลขหน้า 3 ตัว", font=("Arial", 20))
msg4.grid(row=3, column=0, padx=10, pady=10)
reward = tk.Label(root, text=lottery_list[4], font=("Arial", 20))
reward.grid(row=3, column=1, padx=10, pady=10)
reward = tk.Label(root, text=lottery_list[5], font=("Arial", 20))
reward.grid(row=3, column=2, padx=10, pady=10)

root.mainloop()
