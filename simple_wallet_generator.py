# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import secrets
import os

def generate_private_key():
    """Tạo khóa bí mật ngẫu nhiên"""
    return secrets.token_hex(32)

def get_address_from_private_key(private_key):
    """Mô phỏng việc tạo địa chỉ ví từ khóa bí mật"""
    # Trong thực tế, chúng ta sẽ sử dụng thư viện web3 để tạo địa chỉ thật
    # Đây chỉ là mô phỏng để học sinh hiểu nguyên lý
    return f"0x{secrets.token_hex(20)}"

def create_wallet():
    try:
        # Tạo khóa bí mật ngẫu nhiên
        private_key = generate_private_key()
        
        # Tạo địa chỉ ví (mô phỏng)
        address = get_address_from_private_key(private_key)
        
        # Lưu thông tin vào file
        with open('wallet_info.txt', 'w', encoding='utf-8') as f:
            f.write(u"=== THÔNG TIN VÍ ETHEREUM (MÔ PHỎNG) ===\n")
            f.write(u"\nCẢNH BÁO: KHÔNG CHIA SẺ THÔNG TIN NÀY VỚI BẤT KỲ AI!\n")
            f.write(u"\nKhóa bí mật (Private Key):\n")
            f.write(private_key + "\n")
            f.write(u"\nĐịa chỉ ví:\n")
            f.write(address + "\n")
            f.write(u"\n=== HƯỚNG DẪN BẢO MẬT ===\n")
            f.write(u"1. Giữ bí mật khóa bí mật\n")
            f.write(u"2. Không chia sẻ file này với bất kỳ ai\n")
            f.write(u"3. Lưu trữ an toàn và tạo bản sao dự phòng\n")
            f.write(u"\nLưu ý: Đây là phiên bản học tập, không sử dụng cho ví thật!\n")
        
        # Hiển thị địa chỉ ví và thông báo
        address_label.config(text=f"Địa chỉ ví của bạn:\n{address}")
        messagebox.showinfo(
            "Thành công",
            "Đã tạo ví mô phỏng thành công!\n\n" +
            "Thông tin ví đã được lưu vào file 'wallet_info.txt'\n\n" +
            "Lưu ý: Đây chỉ là phiên bản học tập!"
        )
        
    except Exception as e:
        messagebox.showerror(
            "Lỗi",
            f"Đã xảy ra lỗi khi tạo ví:\n{str(e)}\n\nVui lòng thử lại!"
        )

# Tạo cửa sổ chính
window = tk.Tk()
window.title(u"Tạo Ví Ethereum (Mô phỏng)")
window.geometry("600x400")
window.configure(bg="#f0f0f0")

# Tiêu đề
title_label = tk.Label(
    window,
    text=u"Chương trình Mô phỏng Tạo Ví Ethereum\n(Phiên bản học tập)",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0"
)
title_label.pack(pady=20)

# Nút tạo ví
create_button = tk.Button(
    window,
    text=u"Tạo Ví Mới",
    command=create_wallet,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10
)
create_button.pack(pady=20)

# Nhãn hiển thị địa chỉ
address_label = tk.Label(
    window,
    text=u"Địa chỉ ví sẽ hiển thị ở đây",
    font=("Arial", 10),
    bg="#f0f0f0",
    wraplength=500
)
address_label.pack(pady=20)

# Thông tin giải thích
info_label = tk.Label(
    window,
    text=u"Đây là phiên bản mô phỏng dành cho học tập.\n" +
         u"Chương trình này giúp bạn hiểu cách hoạt động của ví Ethereum.\n" +
         u"Không sử dụng thông tin này cho ví thật!",
    font=("Arial", 10),
    bg="#f0f0f0",
    wraplength=500
)
info_label.pack(pady=10)

# Thông tin cảnh báo
warning_label = tk.Label(
    window,
    text=u"CẢNH BÁO: Đây chỉ là mô phỏng để học tập!\n" +
         u"Không sử dụng thông tin này cho ví Ethereum thật.",
    font=("Arial", 10, "bold"),
    fg="red",
    bg="#f0f0f0",
    wraplength=500
)
warning_label.pack(pady=20)

# Khởi chạy ứng dụng
window.mainloop()