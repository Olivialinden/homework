
def calculate_motor_speed(revolutions, time_seconds):
    rpm = (revolutions / time_seconds) * 60
    return rpm

def calculate_torque(force, lever_arm_length):
    torque = force * lever_arm_length
    return torque


def main():
    while True:
        print("\nMenu:")
        print("1. Car Motor Speed Measurement")
        print("2. Car Motor Torque Testing")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Car Motor Speed Measurement")
            print("******************************************************")

            revolutions = float(input("Enter the number of revolutions: "))
            time_seconds = float(input("Enter the time taken (seconds): "))

            motor_speed = calculate_motor_speed(revolutions, time_seconds)

            print(f"\nCalculated Motor Speed: {motor_speed} RPM")
       
        elif choice == "2":
            print("Car Motor Torque Testing")
            print("******************************************************")

            force = float(input("Enter the force applied (Newtons): "))
            lever_arm_length = float(input("Enter the lever arm length (meters): "))

            torque = calculate_torque(force, lever_arm_length)

            print(f"\nCalculated Torque: {torque} Nm")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

