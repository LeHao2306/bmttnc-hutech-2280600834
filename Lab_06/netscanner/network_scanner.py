import requests
from scapy.all import ARP, Ether, srp

def local_network_scan(ip_range):
    # Tạo gói ARP
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]  # Gửi và nhận gói
    
    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "vendor": get_vendor_by_mac(received.hwsrc)
        })
    
    return devices

def get_vendor_by_mac(mac):
    try:
        # Gửi yêu cầu để lấy thông tin nhà cung cấp từ API
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error fetching vendor information: {e}")
        return "Unknown"

def main():
    ip_range = "192.168.1.1/24"  # Thay đổi IP range nếu cần
    devices = local_network_scan(ip_range)

    print("Devices on the local network:")
    if devices:
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")
    else:
        print("No devices found.")

if __name__ == "__main__":
    main()
