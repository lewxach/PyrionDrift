# Orion Drift API Python Wrapper

THIS IS NOW TEMPORARILY DEPRECATED AS THE API BASE URL HAS CHANGED.

This is an unofficial Python wrapper for the **Orion Drift API** (codenamed A2), providing convenient access to the Orion Drift API endpoints. It allows interaction with users, stations, events, roles, and more.

## Features

- User Management: Get, create, update, or delete users.
- Station Management: Fetch, create, update, and delete stations.
- Events: Create, update, or delete station events.
- Roles & Permissions: Manage roles and assign them to users.
- Bans: Ban or unban users in stations.

## Installation

1. Clone this repository or copy the code.
2. Install the required dependencies using pip: `pip install requests`.

## How to get your API Key

Have an external file explorer for your Oculus headset

Go to the path `/sdcard/Android/data/com.AnotherAxiom.A2/files/UnrealGame/A2/A2/Saved/Logs/` in your headset

Download the `A2.log` file

Open it in your preferred text editor (ex,. Notepad)

Do Ctrl+F and type in `login to station dashboard with key`

You should see this large string of random letters and numbers like `oiauhfuhsdghu1.asdasd6.a71m` but it'll be MUCH larger

Copy that

And that's your API key! (That is a PERSONAL api key assigned to your account, don't give it out!!!)

## Usage

### Initialization

You must initialize the `OrionDriftAPI` class with your API key.

### Example: Get All Users

Call the `get_users` method to retrieve all users.

### Example: Create a Station

Use the `create_station` method to create a new station.

## Available Methods

### Users

- `get_users`
- `get_user`
- `create_or_update_user`
- `delete_user`
- `log_in_with_key`
- `log_in`
- `log_in_server`
- `create_user_api_key`

### Stations

- `get_stations`
- `get_station`
- `create_station`
- `update_station`
- `delete_station`
- `get_station_config`
- `set_station_config`
- `delete_station_config`

### Events

- `get_station_events`
- `create_station_event`
- `get_event`
- `update_station_event`
- `delete_station_event`

### Roles & Permissions

- `add_role_to_user`
- `remove_role_from_user`
- `create_role`
- `delete_role`

### Bans

- `ban_user`
- `unban_user`
- `get_station_bans`

## Contributing

Feel free to fork this project and submit pull requests.

## License

This project is licensed under the MIT License.
