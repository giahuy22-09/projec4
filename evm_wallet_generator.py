import tkinter as tk
from tkinter import messagebox
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins
from eth_account import Account
import secrets
import os

def create_wallet():
    try:
        # Tạo cụm từ Mnemonic ngẫu nhiên 24 từ
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(24)
        
        # Tạo seed từ Mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
        
        # Tạo BIP44 cho Ethereum
        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
        bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)
        bip44_chg_ctx = bip44_acc_ctx.Change(False)
        bip44_addr_ctx = bip44_chg_ctx.AddressIndex(0)
        
        # Lấy khóa bí mật và địa chỉ
        private_key = bip44_addr_ctx.PrivateKey().Raw().ToHex()
        address = Account.from_key(private_key).address
        
        # Lưu thông tin vào file
        with open('wallet_info.txt', 'w') as f:
            f.write("=== THÔNG TIN VÍ ETHEREUM ===\n")
            f.write("\nCẢNH BÁO: KHÔNG CHIA SẺ THÔNG TIN NÀY VỚI BẤT KỲ AI!\n")
            f.write("\nCụm từ Mnemonic (24 từ):\n")
            f.write(str(mnemonic) + "\n")
            f.write("\nKhóa bí mật (Private Key):\n")
            f.write(private_key + "\n")
            f.write("\nĐịa chỉ ví:\n")
            f.write(address + "\n")
            f.write("\n=== HƯỚNG DẪN BẢO MẬT ===\n")
            f.write("1. Giữ bí mật cụm từ Mnemonic và khóa bí mật\n")
            f.write("2. Không chia sẻ file này với bất kỳ ai\n")
            f.write("3. Lưu trữ an toàn và tạo bản sao dự phòng\n")
        
        # Hiển thị địa chỉ ví và thông báo
        address_label.config(text=f"Địa chỉ ví của bạn:\n{address}")
        messagebox.showinfo(
            "Thành công",
            "Đã tạo ví thành công!\n\n" +
            "Thông tin ví đã được lưu vào file 'wallet_info.txt'\n\n" +
            "QUAN TRỌNG: Hãy bảo vệ file này cẩn thận!"
        )
        
    except Exception as e:
        messagebox.showerror(
            "Lỗi",
            f"Đã xảy ra lỗi khi tạo ví:\n{str(e)}\n\nVui lòng thử lại!"
        )

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tạo Ví Ethereum")
window.geometry("600x400")
window.configure(bg="#f0f0f0")

# Tiêu đề
title_label = tk.Label(
    window,
    text="Chương trình Tạo Ví Ethereum",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0"
)
title_label.pack(pady=20)

# Nút tạo ví
create_button = tk.Button(
    window,
    text="Tạo Ví Mới",
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
    text="Địa chỉ ví sẽ hiển thị ở đây",
    font=("Arial", 10),
    bg="#f0f0f0",
    wraplength=500
)
address_label.pack(pady=20)

# Thông tin cảnh báo
warning_label = tk.Label(
    window,
    text="CẢNH BÁO: Không chia sẻ thông tin ví với bất kỳ ai!\n" +
         "Hãy lưu giữ file wallet_info.txt một cách an toàn.",
    font=("Arial", 10, "bold"),
    fg="red",
    bg="#f0f0f0",
    wraplength=500
)
warning_label.pack(pady=20)

# Khởi chạy ứng dụng
window.mainloop()