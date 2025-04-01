import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 123477)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE  # Thay đổi theo nhu cầu của bạn
context.check_hostname = False  # Thay đổi theo nhu cầu của bạn

# Thiết lập kết nối SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

ssl_socket.connect(server_address)

# Bắt đầu luồng để nhận dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()


try:
    while True:
        message = input("Nhập thông điệp để gửi: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()
    

