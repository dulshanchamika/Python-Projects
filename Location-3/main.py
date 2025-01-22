import serial
import time


def read_gps_data(port, baudrate=9600, timeout=1):
    """
    Reads and parses GPS data from a hardware sensor.

    Parameters:
        port (str): The serial port to which the GPS module is connected (e.g., COM3 or /dev/ttyUSB0).
        baudrate (int): The baud rate for the serial communication.
        timeout (int): Timeout for the serial read.

    Returns:
        None: Continuously prints GPS data.
    """
    try:
        # Open the serial port
        with serial.Serial(port, baudrate, timeout=timeout) as gps:
            print(f"Connected to GPS on {port}")

            while True:
                # Read a line of data from the GPS module
                line = gps.readline().decode('utf-8', errors='ignore').strip()

                # Print the raw data
                print(f"Raw GPS data: {line}")

                # Process data if it's a valid NMEA sentence
                if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                    print(f"Processed GPS sentence: {line}")

                # Pause for readability
                time.sleep(0.1)

    except serial.SerialException as e:
        print(f"Error connecting to GPS module: {e}")
    except KeyboardInterrupt:
        print("Program stopped by user.")


# Example usage: Replace 'COM3' or '/dev/ttyUSB0' with your GPS module's port
read_gps_data(port='/dev/ttyUSB0')  # Replace with the correct port for your system
