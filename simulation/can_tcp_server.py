# simulation/can_tcp_server.py (on Linux)
import socket
import can

def send_can_over_tcp():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5005))  # Listen on all interfaces
    server.listen(1)
    print("🔌 Waiting for LabVIEW to connect...")
    conn, addr = server.accept()
    print(f"✅ Connected to {addr}")

    try:
        while True:
            msg = bus.recv()
            if msg:
                data_str = f"{msg.arbitration_id},{','.join(map(str, msg.data))}\n"
                conn.sendall(data_str.encode())
    except KeyboardInterrupt:
        print("🛑 Stopped")
    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    send_can_over_tcp()
