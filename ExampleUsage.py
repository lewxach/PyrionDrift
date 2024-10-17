from api.PyrionDrift import OrionDriftAPI

api = None

def get_user_by_id():
    """Fetches a user by user ID."""
    try:
        user_id = input("Enter user ID: ")
        user = api.get_user(user_id)
        if user:
            print(f"User ID: {user['user_id']}, Username: {user['username']}, Platform: {user['platform']}")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error fetching user: {e}")

def get_all_stations():
    """Fetches all stations."""
    try:
        stations = api.get_stations()
        print("Listing Stations:")
        for station in stations['items']:
            print(f"Station ID: {station['station_id']}, Station Name: {station['station_name']}")
    except Exception as e:
        print(f"Error fetching stations: {e}")

def main():
    print("Orion Drift API Utility")
    print("1. Get User by ID")
    print("2. Get All Stations")

    choice = input("Choose an option: ")

    if choice == '1':
        get_user_by_id()
    elif choice == '2':
        get_all_stations()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    try:
        api_key = input("Give your Orion Drift API key: ")
        api = OrionDriftAPI(api_key=api_key)
        main()
    except Exception as e:
        print(f"Error initializing API: {e}")
