// Import các thư viện cần thiết
import { ethers } from 'ethers';
import * as readlineSync from 'readline-sync';

// Định nghĩa URL của nút Ronin Saigon Testnet
const RONIN_SAIGON_RPC = 'https://saigon-testnet.roninchain.com/rpc';

// Hàm kiểm tra xem một chuỗi có phải là địa chỉ ví hợp lệ hay không
function isValidAddress(address: string): boolean {
    try {
        // Sử dụng hàm getAddress của ethers để kiểm tra và chuẩn hóa địa chỉ
        ethers.utils.getAddress(address);
        return true;
    } catch {
        return false;
    }
}

// Hàm chính để kiểm tra số dư của ví
async function checkBalance(address: string): Promise<void> {
    try {
        // Tạo kết nối đến mạng Ronin Saigon thông qua JsonRpcProvider
        const provider = new ethers.providers.JsonRpcProvider(RONIN_SAIGON_RPC);

        // Kiểm tra tính hợp lệ của địa chỉ ví
        if (!isValidAddress(address)) {
            console.log('❌ Lỗi: Địa chỉ ví không hợp lệ!');
            return;
        }

        // Lấy số dư của địa chỉ ví (kết quả là BigNumber)
        const balance = await provider.getBalance(address);

        // Chuyển đổi số dư từ Wei sang RON (1 RON = 10^18 Wei)
        const balanceInRON = ethers.utils.formatEther(balance);

        // Hiển thị kết quả
        console.log('\n📍 Thông tin ví:');
        console.log(`Địa chỉ: ${address}`);
        console.log(`Số dư: ${balanceInRON} RON`);

    } catch (error) {
        // Xử lý các lỗi có thể xảy ra
        if (error instanceof Error) {
            if (error.message.includes('network')) {
                console.log('❌ Lỗi: Không thể kết nối đến mạng Ronin Saigon. Vui lòng kiểm tra kết nối internet!');
            } else {
                console.log('❌ Lỗi:', error.message);
            }
        }
    }
}

// Hàm main để chạy chương trình
async function main() {
    console.log('🔍 KIỂM TRA SỐ DƯ VÍ TRÊN MẠNG RONIN SAIGON');
    console.log('==========================================');

    // Nhập địa chỉ ví từ người dùng
    const address = readlineSync.question('\nNhập địa chỉ ví (0x...): ');

    // Kiểm tra số dư
    await checkBalance(address);
}

// Chạy chương trình
main().catch(error => {
    console.log('❌ Lỗi không mong muốn:', error);
});