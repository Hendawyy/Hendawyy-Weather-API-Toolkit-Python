import Components


while True:
    print("\nMenu:")
    print("1. Get Current Temperature")
    print("2. Get Temperature After")
    print("3. Get Latitude & Longitude")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Components.get_current_temperature_input()
        elif choice == 2:
            Components.get_weather_forecast_from_input()
        elif choice == 3:
            Components.get_lat_long_input()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a valid choice.")