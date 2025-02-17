import serial
import time

# Connect to Arduino (Change COM Port accordingly, e.g., 'COM3' for Windows, '/dev/ttyUSB0' for Linux)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for connection

def detect_obstacle(threshold=20):
    while True:
        try:
            data = arduino.readline().decode().strip()
            if data:
                distance = float(data)
                print(f"Distance: {distance} cm")

                if distance < threshold:
                    print("⚠️ Obstacle Detected!")
                else:
                    print("No Obstacle")
                    
            time.sleep(1)  # Delay between readings

        except ValueError:
            print("Invalid Data Received")
        except KeyboardInterrupt:
            print("\nStopping...")
            arduino.close()
            break

# Run the detection function
detect_obstacle()
