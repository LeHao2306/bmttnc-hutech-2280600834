import socket

def handle_request(client_socket, request_data):
    """Xử lý yêu cầu từ client."""
    if "GET /admin" in request_data:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nWelcome to the admin page!"
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, this is a simple web server!"

    # Gửi phản hồi về client và đóng kết nối
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    """Khởi tạo server và xử lý kết nối client."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))  # Lắng nghe trên localhost và cổng 8080
    server_socket.listen(5)  # Cho phép tối đa 5 kết nối đồng thời

    print("Server listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # Nhận dữ liệu từ client
            request_data = b''  # Khởi tạo biến chứa dữ liệu nhận
            while True:
                data = client_socket.recv(1024)
                request_data += data
                if len(data) < 1024:  # Nếu nhận đủ dữ liệu, thoát vòng lặp
                    break
            
            # Giải mã dữ liệu nhận được với UTF-8 và bỏ qua các byte không hợp lệ
            request_data = request_data.decode('utf-8', errors='ignore')
            print(f"Received data: {request_data}")  # In ra dữ liệu nhận được từ client

            # Xử lý yêu cầu từ client
            handle_request(client_socket, request_data)

        except UnicodeDecodeError as e:
            print(f"Error decoding data: {e}")
            client_socket.close()

        except Exception as e:
            print(f"An error occurred: {e}")
            client_socket.close()

if __name__ == "__main__":
    main()
