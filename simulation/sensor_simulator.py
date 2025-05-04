import time
import can

def simulate_speed_ramp():
    # Explicitly specify the bus name
    bus = can.interface.Bus(channel='vcan0', bustype='virtual')  # virtual CAN bus name
    speed = 0
    while speed <= 120:
        msg = can.Message(
            arbitration_id=0x100,
            data=[speed],
            is_extended_id=False
        )
        try:
            bus.send(msg)
            print(f"Sent CAN message: Speed = {speed} km/h")
        except can.CanError:
            print("Failed to send CAN message")
        speed += 10
        time.sleep(1)

if __name__ == "__main__":
    simulate_speed_ramp()

