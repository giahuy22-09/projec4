import tkinter as tk
from tkinter import messagebox

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy tính đơn giản")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

# Hàm kiểm tra đầu vào có phải là số hợp lệ không
def is_valid_number(num_str):
    if not num_str:  # Kiểm tra chuỗi rỗng
        return False
    try:
        float(num_str)  # Thử chuyển đổi sang số
        return True
    except ValueError:
        return False

# Hàm thực hiện phép tính
def calculate(operation):
    num1 = entry1.get()
    num2 = entry2.get()
    
    # Kiểm tra đầu vào
    if not is_valid_number(num1) or not is_valid_number(num2):
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
        return
    
    # Chuyển đổi sang số
    num1 = float(num1)
    num2 = float(num2)
    
    # Thực hiện phép tính tương ứng
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "×":
            result = num1 * num2
        elif operation == "÷":
            if num2 == 0:  # Kiểm tra chia cho 0
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                return
            result = num1 / num2
        
        # Hiển thị kết quả, làm tròn đến 2 chữ số thập phân
        result_label.config(text=f"Kết quả: {result:.2f}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo và định vị các thành phần giao diện
# Nhãn và ô nhập số thứ nhất
num1_label = tk.Label(window, text="Số thứ nhất:", bg="#f0f0f0", font=("Arial", 12))
num1_label.pack(pady=5)
entry1 = tk.Entry(window, font=("Arial", 12))
entry1.pack(pady=5)

# Nhãn và ô nhập số thứ hai
num2_label = tk.Label(window, text="Số thứ hai:", bg="#f0f0f0", font=("Arial", 12))
num2_label.pack(pady=5)
entry2 = tk.Entry(window, font=("Arial", 12))
entry2.pack(pady=5)

# Khung chứa các nút phép tính
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

# Tạo các nút phép tính
buttons = [
    ("+", "#4CAF50"),  # Xanh lá
    ("-", "#2196F3"),  # Xanh dương
    ("×", "#FFC107"),  # Vàng
    ("÷", "#FF5722")   # Cam
]

for symbol, color in buttons:
    btn = tk.Button(
        button_frame,
        text=symbol,
        width=5,
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        command=lambda s=symbol: calculate(s)
    )
    btn.pack(side=tk.LEFT, padx=5)

# Nhãn hiển thị kết quả
result_label = tk.Label(
    window,
    text="Kết quả: ",
    bg="#f0f0f0",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

# Khởi chạy ứng dụng
window.mainloop()