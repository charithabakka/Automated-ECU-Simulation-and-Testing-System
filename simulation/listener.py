import can

def listen():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print("🎧 Listening on vcan0...")
    msg = bus.recv(timeout=5)
    if msg:
        print(f"📥 Received: ID={hex(msg.arbitration_id)} Data={list(msg.data)}")
    else:
        print("⌛ Timeout - No message received")

if __name__ == "__main__":
    listen()


