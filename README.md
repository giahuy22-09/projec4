# Ứng dụng Kiểm tra Số dư Ví Ronin

Đây là một ứng dụng TypeScript đơn giản để kiểm tra số dư của địa chỉ ví trên mạng Ronin Saigon (testnet). Ứng dụng này sử dụng giao thức JSON-RPC để kết nối trực tiếp với blockchain.

## Yêu cầu Hệ thống

- Node.js (phiên bản 14.0.0 trở lên)
- npm (Node Package Manager, thường được cài đặt cùng Node.js)

## Hướng dẫn Cài đặt

1. **Cài đặt Node.js và npm**
   - Tải và cài đặt Node.js từ [trang chủ Node.js](https://nodejs.org/)
   - Sau khi cài đặt, mở Terminal (hoặc Command Prompt) và kiểm tra phiên bản:
     ```bash
     node --version
     npm --version
     ```

2. **Cài đặt các thư viện cần thiết**
   - Mở Terminal trong thư mục dự án
   - Chạy lệnh sau để cài đặt các thư viện:
     ```bash
     npm install
     ```

## Cách Sử dụng

1. **Chạy chương trình**
   - Trong Terminal, chạy lệnh:
     ```bash
     npm start
     ```

2. **Sử dụng ứng dụng**
   - Khi chương trình chạy, nó sẽ yêu cầu bạn nhập địa chỉ ví
   - Nhập địa chỉ ví EVM (bắt đầu bằng '0x')
   - Chương trình sẽ hiển thị số dư của ví bằng đơn vị RON

## Ví dụ

```
🔍 KIỂM TRA SỐ DƯ VÍ TRÊN MẠNG RONIN SAIGON
==========================================

Nhập địa chỉ ví (0x...): 0x742d35Cc6634C0532925a3b844Bc454e4438f44e

📍 Thông tin ví:
Địa chỉ: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
Số dư: 10.5 RON
```

## Xử lý Lỗi Thường Gặp

1. **Địa chỉ ví không hợp lệ**
   - Đảm bảo địa chỉ ví bắt đầu bằng '0x'
   - Kiểm tra độ dài địa chỉ (phải đủ 42 ký tự bao gồm '0x')

2. **Lỗi kết nối mạng**
   - Kiểm tra kết nối internet
   - Đảm bảo bạn có thể truy cập mạng Ronin Saigon

## Tìm hiểu thêm

- [Tài liệu về Ronin Network](https://docs.skymavis.com/ronin/)
- [Tài liệu về ethers.js](https://docs.ethers.io/)
- [Giới thiệu về JSON-RPC](https://ethereum.org/en/developers/docs/apis/json-rpc/)