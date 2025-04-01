import subprocess
from scapy.all import *

def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = []
    for line in output_lines:
        if len(line.split()) > 4:
            interface = line.split()[3]
            status = line.split()[1]
            # Kiểm tra nếu giao diện đang kết nối
            if status == 'Connected':
                interfaces.append(interface)
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))

def main():
    # Lấy các giao diện mạng hợp lệ
    interfaces = get_interfaces()
    
    if not interfaces:
        print("No network interfaces found.")
        return
    
    print("Danh sách các giao diện mạng:")
    for i, iface in enumerate(interfaces, start=1):
        print(f"{i}. {iface}")
    
    while True:
        try:
            # Yêu cầu người dùng chọn giao diện
            choice = int(input("Chọn một giao diện mạng (nhập số): "))
            if choice < 1 or choice > len(interfaces):
                print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
                continue
            selected_iface = interfaces[choice - 1]
            print(f"Đang bắt gói tin trên giao diện: {selected_iface}")
            break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    
    # Bắt gói tin trên giao diện đã chọn
    try:
        sniff(iface=selected_iface, prn=packet_handler, filter="tcp")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
