
def get_mock_motor_speed():
    # Replace this with actual code to get motor speed data
    return 3000  # Example motor speed in RPM

def get_mock_vibration_level():
    # Replace this with actual code to get vibration level data
    return 0.25  # Example vibration level

def main():
    while True:
        print("\nMenu:")
        print("1. Test Motor Speed")
        print("2. Test Vibration Level")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            motor_speed = get_mock_motor_speed()
            print(f"Motor speed: {motor_speed} RPM")
        elif choice == "2":
            vibration_level = get_mock_vibration_level()
            print(f"Vibration level: {vibration_level}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

