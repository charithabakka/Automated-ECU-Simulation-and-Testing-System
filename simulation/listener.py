import can

def listen_for_messages():
    # Explicitly specify the bus name
    bus = can.interface.Bus(channel='vcan0', bustype='virtual')  # virtual CAN bus name
    print("Listening for CAN messages...")
    try:
        while True:
            message = bus.recv(timeout=30)  # wait longer for messages
            if message:
                print(f"Received: ID={hex(message.arbitration_id)} Data={message.data}")
            else:
                print("No message received (timeout).")
                break
    except KeyboardInterrupt:
        print("Stopped listening.")

if __name__ == "__main__":
    listen_for_messages()

