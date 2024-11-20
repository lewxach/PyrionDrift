import argparse
import json
import os
from api.PyrionDrift import OrionDriftAPI

class OrionDriftCLI:
    def __init__(self):
        self.api_key = None
        self.api = None

    def run(self):
        parser = argparse.ArgumentParser(description="Orion Drift API CLI")
        subparsers = parser.add_subparsers(dest="command", help="Available commands")
        parser.add_argument("--use-alt-dom", action="store_true", help="Use the alternate API domain.")
        parser.add_argument("--no-pass-key", action="store_true", help="Disable passing the API key")

        # User commands
        user_parser = subparsers.add_parser("user", help="User related commands")
        user_subparsers = user_parser.add_subparsers(dest="user_command")

        get_users_parser = user_subparsers.add_parser("list", help="Get users")
        get_users_parser.add_argument("--include-roles", action="store_true")
        get_users_parser.add_argument("--include-permissions", action="store_true")
        get_users_parser.add_argument("--page-size", type=int, default=100)
        get_users_parser.add_argument("--page", type=int, default=1)

        get_user_parser = user_subparsers.add_parser("get", help="Get user details")
        get_user_parser.add_argument("user_id", help="User ID")
        get_user_parser.add_argument("--include-roles", action="store_true")
        get_user_parser.add_argument("--include-permissions", action="store_true")
        get_user_parser.add_argument("--include-bans", action="store_true")

        create_user_parser = user_subparsers.add_parser("create", help="Create or update user")
        create_user_parser.add_argument("user_data", help="User data in JSON format")

        delete_user_parser = user_subparsers.add_parser("delete", help="Delete user")
        delete_user_parser.add_argument("user_id", help="User ID")

        login_parser = user_subparsers.add_parser("login", help="Log in")
        login_parser.add_argument("login_data", help="Login data in JSON format")

        login_server_parser = user_subparsers.add_parser("login-server", help="Log in server")
        login_server_parser.add_argument("server_login_data", help="Server login data in JSON format")

        create_api_key_parser = user_subparsers.add_parser("create-api-key", help="Create user API key")
        create_api_key_parser.add_argument("user_id", help="User ID")

        # Station commands
        station_parser = subparsers.add_parser("station", help="Station related commands")
        station_subparsers = station_parser.add_subparsers(dest="station_command")

        get_stations_parser = station_subparsers.add_parser("list", help="Get stations")
        get_stations_parser.add_argument("--include-config", action="store_true")
        get_stations_parser.add_argument("--include-deployments", action="store_true")
        get_stations_parser.add_argument("--include-offline-stations", action="store_true")
        get_stations_parser.add_argument("--page-size", type=int, default=100)
        get_stations_parser.add_argument("--page", type=int, default=1)

        get_station_parser = station_subparsers.add_parser("get", help="Get station details")
        get_station_parser.add_argument("station_id", help="Station ID")
        get_station_parser.add_argument("--include-config", action="store_true")
        get_station_parser.add_argument("--include-deployments", action="store_true")

        create_station_parser = station_subparsers.add_parser("create", help="Create station")
        create_station_parser.add_argument("station_data", help="Station data in JSON format")

        update_station_parser = station_subparsers.add_parser("update", help="Update station")
        update_station_parser.add_argument("station_id", help="Station ID")
        update_station_parser.add_argument("station_data", help="Station data in JSON format")

        delete_station_parser = station_subparsers.add_parser("delete", help="Delete station")
        delete_station_parser.add_argument("station_id", help="Station ID")

        # Station config commands
        config_parser = subparsers.add_parser("config", help="Station config related commands")
        config_subparsers = config_parser.add_subparsers(dest="config_command")

        get_config_parser = config_subparsers.add_parser("get", help="Get station config")
        get_config_parser.add_argument("station_id", help="Station ID")

        set_config_parser = config_subparsers.add_parser("set", help="Set station config")
        set_config_parser.add_argument("station_id", help="Station ID")
        set_config_parser.add_argument("config_data", help="Config data in JSON format")

        delete_config_parser = config_subparsers.add_parser("delete", help="Delete station config keys")
        delete_config_parser.add_argument("station_id", help="Station ID")
        delete_config_parser.add_argument("config_keys", help="Config keys to delete in JSON format")

        # Event commands
        event_parser = subparsers.add_parser("event", help="Event related commands")
        event_subparsers = event_parser.add_subparsers(dest="event_command")

        get_events_parser = event_subparsers.add_parser("list", help="Get station events")
        get_events_parser.add_argument("station_id", help="Station ID")
        get_events_parser.add_argument("--get-past-events", action="store_true")

        create_event_parser = event_subparsers.add_parser("create", help="Create station event")
        create_event_parser.add_argument("station_id", help="Station ID")
        create_event_parser.add_argument("event_data", help="Event data in JSON format")

        get_event_parser = event_subparsers.add_parser("get", help="Get event details")
        get_event_parser.add_argument("event_id", help="Event ID")

        update_event_parser = event_subparsers.add_parser("update", help="Update station event")
        update_event_parser.add_argument("station_id", help="Station ID")
        update_event_parser.add_argument("event_id", help="Event ID")
        update_event_parser.add_argument("event_data", help="Event data in JSON format")

        delete_event_parser = event_subparsers.add_parser("delete", help="Delete station event")
        delete_event_parser.add_argument("station_id", help="Station ID")
        delete_event_parser.add_argument("event_id", help="Event ID")

        # Role commands
        role_parser = subparsers.add_parser("role", help="Role related commands")
        role_subparsers = role_parser.add_subparsers(dest="role_command")

        add_role_parser = role_subparsers.add_parser("add", help="Add role to user")
        add_role_parser.add_argument("station_id", help="Station ID")
        add_role_parser.add_argument("user_id", help="User ID")
        add_role_parser.add_argument("role_id", help="Role ID")

        remove_role_parser = role_subparsers.add_parser("remove", help="Remove role from user")
        remove_role_parser.add_argument("station_id", help="Station ID")
        remove_role_parser.add_argument("user_id", help="User ID")
        remove_role_parser.add_argument("role_id", help="Role ID")

        create_role_parser = role_subparsers.add_parser("create", help="Create role")
        create_role_parser.add_argument("station_id", help="Station ID")
        create_role_parser.add_argument("role_data", help="Role data in JSON format")

        delete_role_parser = role_subparsers.add_parser("delete", help="Delete role")
        delete_role_parser.add_argument("station_id", help="Station ID")
        delete_role_parser.add_argument("role_id", help="Role ID")

        # Ban commands
        ban_parser = subparsers.add_parser("ban", help="Ban related commands")
        ban_subparsers = ban_parser.add_subparsers(dest="ban_command")

        ban_user_parser = ban_subparsers.add_parser("create", help="Ban user")
        ban_user_parser.add_argument("station_id", help="Station ID")
        ban_user_parser.add_argument("user_id", help="User ID")
        ban_user_parser.add_argument("duration", help="Ban duration")
        ban_user_parser.add_argument("reason", help="Ban reason")

        unban_user_parser = ban_subparsers.add_parser("remove", help="Unban user")
        unban_user_parser.add_argument("station_id", help="Station ID")
        unban_user_parser.add_argument("user_id", help="User ID")

        get_bans_parser = ban_subparsers.add_parser("list", help="Get station bans")
        get_bans_parser.add_argument("station_id", help="Station ID")
        get_bans_parser.add_argument("--include-revoked", action="store_true")
        get_bans_parser.add_argument("--include-expired", action="store_true")

        args = parser.parse_args()
        
        if args.no_pass_key:
            self.api_key = None
        else:
            self.api_key = ""
            
        if args.use_alt_dom:
            self.api = OrionDriftAPI(self.api_key, base_url="https://a2-station-api-prod-708695367983.us-central1.run.app")
        else:
            self.api = OrionDriftAPI(self.api_key)
        
        if args.command == "user":
            self.handle_user_commands(args)
        elif args.command == "station":
            self.handle_station_commands(args)
        elif args.command == "config":
            self.handle_config_commands(args)
        elif args.command == "event":
            self.handle_event_commands(args)
        elif args.command == "role":
            self.handle_role_commands(args)
        elif args.command == "ban":
            self.handle_ban_commands(args)
        else:
            parser.print_help()

    def handle_user_commands(self, args):
        if args.user_command == "list":
            result = self.api.get_users(args.include_roles, args.include_permissions, args.page_size, args.page)
        elif args.user_command == "get":
            result = self.api.get_user(args.user_id, args.include_roles, args.include_permissions, args.include_bans)
        elif args.user_command == "create":
            result = self.api.create_or_update_user(json.loads(args.user_data))
        elif args.user_command == "delete":
            result = self.api.delete_user(args.user_id)
        elif args.user_command == "login":
            result = self.api.log_in(json.loads(args.login_data))
        elif args.user_command == "login-server":
            login_server = {
                "sigma": "skibidi",
                "rizzy": "gyatt",
                "ilove": "livvydunne"
            }
            result = self.api.log_in_server(login_server)
        elif args.user_command == "create-api-key":
            result = self.api.create_user_api_key(args.user_id)
        else:
            print("Invalid user command")
            return

        print(json.dumps(result, indent=2))

    def handle_station_commands(self, args):
        if args.station_command == "list":
            result = self.api.get_stations(args.include_config, args.include_deployments, args.include_offline_stations, args.page_size, args.page)
            with open("stations.json", "w") as json_file:
                json.dump(result, json_file, indent=4)
                
        elif args.station_command == "get":
            result = self.api.get_station(args.station_id, args.include_config, args.include_deployments)
        elif args.station_command == "create":
            result = self.api.create_station(json.loads(args.station_data))
        elif args.station_command == "update":
            result = self.api.update_station(args.station_id, json.loads(args.station_data))
        elif args.station_command == "delete":
            result = self.api.delete_station(args.station_id)
        else:
            print("Invalid station command")
            return

        print(json.dumps(result, indent=2))

    def handle_config_commands(self, args):
        if args.config_command == "get":
            result = self.api.get_station_config(args.station_id)
        elif args.config_command == "set":
            result = self.api.set_station_config(args.station_id, json.loads(args.config_data))
        elif args.config_command == "delete":
            result = self.api.delete_station_config(args.station_id, json.loads(args.config_keys))
        else:
            print("Invalid config command")
            return

        print(json.dumps(result, indent=2))

    def handle_event_commands(self, args):
        if args.event_command == "list":
            result = self.api.get_station_events(args.station_id, args.get_past_events)
        elif args.event_command == "create":
            result = self.api.create_station_event(args.station_id, json.loads(args.event_data))
        elif args.event_command == "get":
            result = self.api.get_event(args.event_id)
        elif args.event_command == "update":
            result = self.api.update_station_event(args.station_id, args.event_id, json.loads(args.event_data))
        elif args.event_command == "delete":
            result = self.api.delete_station_event(args.station_id, args.event_id)
        else:
            print("Invalid event command")
            return

        print(json.dumps(result, indent=2))

    def handle_role_commands(self, args):
        if args.role_command == "add":
            result = self.api.add_role_to_user(args.station_id, args.user_id, args.role_id)
        elif args.role_command == "remove":
            result = self.api.remove_role_from_user(args.station_id, args.user_id, args.role_id)
        elif args.role_command == "create":
            result = self.api.create_role(args.station_id, json.loads(args.role_data))
        elif args.role_command == "delete":
            result = self.api.delete_role(args.station_id, args.role_id)
        else:
            print("Invalid role command")
            return

        print(json.dumps(result, indent=2))

    def handle_ban_commands(self, args):
        if args.ban_command == "create":
            result = self.api.ban_user(args.station_id, args.user_id, args.duration, args.reason)
        elif args.ban_command == "remove":
            result = self.api.unban_user(args.station_id, args.user_id)
        elif args.ban_command == "list":
            result = self.api.get_station_bans(args.station_id, args.include_revoked, args.include_expired)
        else:
            print("Invalid ban command")
            return

        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    cli = OrionDriftCLI()
    cli.run()