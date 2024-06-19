import http.server
import socket
import threading

# 获取本地IP地址
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# 启动本地HTTP服务器
def start_http_server(port):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    return httpd

# 获取公网URL
def get_public_url(local_ip, port):
    return f"http://{local_ip}:{port}"

def main():
    # 本地服务器端口
    port = 8000

    # 获取本地IP地址
    local_ip = get_local_ip()
    print(f"Local IP Address: {local_ip}")

    # 启动HTTP服务器
    httpd = start_http_server(port)
    print(f"Local HTTP server started at port {port}")

    try:
        # 输出公网URL
        public_url = get_public_url(local_ip, port)
        print(f"Public URL: {public_url}")

        # 持续运行服务器
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.shutdown()

if __name__ == "__main__":
    main()
