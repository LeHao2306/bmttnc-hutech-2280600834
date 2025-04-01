from scapy.all import *
import socket

# Danh sách các cổng phổ biến cần kiểm tra
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

# Hàm kiểm tra các cổng mở
def scan_common_ports(target, timeout=2):
    open_ports = []
    target_ip = socket.gethostbyname(target)
    
    for port in COMMON_PORTS:
        # Gửi gói tin SYN để kiểm tra cổng mở
        response = sr1(TCP(dst=target_ip, dport=port, flags="S"), timeout=timeout, verbose=0)
        
        # Nếu nhận được phản hồi, cổng mở
        if response:
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:  # SYN+ACK
                open_ports.append(port)
                send(IP(dst=target_ip)/TCP(dport=port, flags="R"), verbose=0)  # Gửi gói tin Reset
    return open_ports

# Hàm chính để chạy Port Scanner
def main():
    target_domain = input("Enter the target domain: ")  # Nhập domain cần kiểm tra
    open_ports = scan_common_ports(target_domain)  # Kiểm tra cổng mở

    # In ra các cổng mở
    if open_ports:
        print("Open common ports:")
        print(open_ports)
    else:
        print("No open common ports found.")

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
