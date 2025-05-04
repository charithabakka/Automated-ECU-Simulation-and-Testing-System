import time
import can

def simulate_speed():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    msg = can.Message(arbitration_id=0x100, data=[50], is_extended_id=False)
    try:
        bus.send(msg)
        print("✅ Sent: Speed = 50 km/h")
    except can.CanError:
        print("❌ Message not sent")

if __name__ == "__main__":
    simulate_speed()

