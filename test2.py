import tkinter as tk
import time
import math
import threading
import pyperclip
import keyboard

class MessageSender:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-topmost", True)  # Giữ cửa sổ luôn ở trên cùng
        self.running = False
        self.paused = False
        self.count = 0
        self.count_add1 = 0
        self.count_add2 = 0
        self.count_add3 = 0

        # Các giá trị đầu vào
        self.round_value = [0, 13, 12, 14]
        self.add1_code = ["65", "66", "67", "68"]
        self.diamon_value = [11, 23, 17, 7]
        self.add2_code = ["54", "53", "52", "51"]
        self.heart_value = [15, 14, 23, 5]
        self.add3_code = ["75", "74", "73", "72"]
        self.limit2 = [75, 50, 25, 25]
        self.limit3 = [75, 50, 25, 25]
        self.limit3p = [6, 5, 4, 3]

        # Bộ đếm
        self.current_add1_index = 0
        self.current_add2_index = 0
        self.current_add3_index = 0

        # Khởi tạo GUI
        self.setup_gui()

       

    def setup_gui(self):
        self.start_button = tk.Button(self.root, text="Bắt đầu", command=self.toggle_start_stop)
        self.start_button.pack(pady=20)

        self.pause_button = tk.Button(self.root, text="Tạm dừng", command=self.toggle_pause_resume)
        self.pause_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="Trạng thái: Đang dừng")
        self.status_label.pack(pady=20)

        self.count_label = tk.Label(self.root, text="Count: 0")
        self.count_label.pack()

        self.count_add1_label = tk.Label(self.root, text="Count Add1: 0")
        self.count_add1_label.pack()

        self.count_add2_label = tk.Label(self.root, text="Count Add2: 0")
        self.count_add2_label.pack()

        self.count_add3_label = tk.Label(self.root, text="Count Add3: 0")
        self.count_add3_label.pack()

        self.value_add1_label = tk.Label(self.root, text="Value Add1: " + str(self.round_value))
        self.value_add1_label.pack()

        self.value_add2_label = tk.Label(self.root, text="Value Add2: " + str(self.diamon_value))
        self.value_add2_label.pack()

        self.value_add3_label = tk.Label(self.root, text="Value Add3: " + str(self.heart_value))
        self.value_add3_label.pack()

    def toggle_start_stop(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def toggle_pause_resume(self):
        if self.paused:
            self.paused = False
            self.pause_button.config(text="Tạm dừng")
        else:
            self.paused = True
            self.pause_button.config(text="Tiếp tục")

    def start(self):
        self.running = True
        self.status_label.config(text="Trạng thái: Đang chạy")
        self.start_button.config(text="Kết thúc")

        # Tạo một thread riêng biệt để thực hiện vòng lặp gửi tin nhắn
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        self.status_label.config(text="Trạng thái: Đang dừng")
        self.start_button.config(text="Bắt đầu")

    def run(self):
        while self.running:
            if not self.paused:
                self.count += 1

                # Tính toán số lần gửi tin nhắn phụ
                limit2_rounded = math.ceil(self.limit2[self.current_add2_index] / self.limit3p[self.current_add3_index])
                limit3_rounded = self.limit3[self.current_add3_index]

                # Gửi tin nhắn chính
                if self.count % 1 == 0:  # Gửi tin nhắn chính mỗi lần
                    self.send_main_message()

                # Kiểm tra điều kiện để gửi add1
                if self.count_add1 >= limit2_rounded:
                    self.send_add1()

                # Kiểm tra điều kiện để gửi add2
                if self.count_add2 >= self.limit2[self.current_add2_index]:
                    self.send_add2()

                # Kiểm tra điều kiện để gửi add3
                if self.count_add3 >= self.limit3[self.current_add3_index]:
                    self.send_add3()

                # Cập nhật các label trên GUI
                self.update_labels()

                time.sleep(0.1)  # Tạm dừng 0.1 giây giữa các vòng lặp

    def send_main_message(self):
        message = "owo hunt"
        pyperclip.copy(message)
        self.paste_and_send()
        self.count_add1 += 1
        self.count_add2 += 1
        self.count_add3 += 1

    def send_add1(self):
        if self.round_value[self.current_add1_index] > 0:
            message = f"owo use {self.add1_code[self.current_add1_index]}"
            pyperclip.copy(message)
            self.paste_and_send()
            self.round_value[self.current_add1_index] -= 1
        self.count_add1 = 0

        if self.round_value[self.current_add1_index] == 0 and self.current_add1_index < len(self.round_value) - 1:
            self.current_add1_index += 1

    def send_add2(self):
        if self.diamon_value[self.current_add2_index] > 0:
            message = f"owo use {self.add2_code[self.current_add2_index]}"
            pyperclip.copy(message)
            self.paste_and_send()
            self.diamon_value[self.current_add2_index] -= 1
        self.count_add2 = 0

        if self.diamon_value[self.current_add2_index] == 0 and self.current_add2_index < len(self.diamon_value) - 1:
            self.current_add2_index += 1

    def send_add3(self):
        if self.heart_value[self.current_add3_index] > 0:
            message = f"owo use {self.add3_code[self.current_add3_index]}"
            pyperclip.copy(message)
            self.paste_and_send()
            self.heart_value[self.current_add3_index] -= 1
        self.count_add3 = 0

        if self.heart_value[self.current_add3_index] == 0 and self.current_add3_index < len(self.heart_value) - 1:
            self.current_add3_index += 1

    def paste_and_send(self):
        """Dán và gửi tin nhắn bằng Ctrl+V và Enter."""
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.1)  # Đợi một chút để dán
        keyboard.press_and_release('enter')

    def update_labels(self):
        self.count_label.config(text=f"Count: {self.count}")
        self.count_add1_label.config(text=f"Count Add1: {self.count_add1}/{math.ceil(self.limit2[self.current_add2_index] / self.limit3p[self.current_add3_index])}")
        self.count_add2_label.config(text=f"Count Add2: {self.count_add2}/{self.limit2[self.current_add2_index]}")
        self.count_add3_label.config(text=f"Count Add3: {self.count_add3}/{self.limit3[self.current_add3_index]}")
        self.value_add1_label.config(text=f"Value Add1: {self.round_value}")
        self.value_add2_label.config(text=f"Value Add2: {self.diamon_value}")
        self.value_add3_label.config(text=f"Value Add3: {self.heart_value}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tin Nhắn Gửi Tự Động")
    root.geometry("400x600")
    app = MessageSender(root)
    root.mainloop()
