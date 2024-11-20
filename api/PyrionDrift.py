import requests

class APIError(Exception):
    # idk y i made this lol, i wanna give it functionality but meh
    pass

class OrionDriftAPI:
    def __init__(self, api_key, base_url="https://api.oriondrift.net"):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def _handle_request(self, method, endpoint, params=None, json=None):
        try:
            url = f"{self.base_url}{endpoint}"
            response = method(url, headers=self.headers, params=params, json=json)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIError(f"Error occurred during API request: {e}")

    # user endpoints
    def get_users(self, include_roles=False, include_permissions=False, page_size=100, page=1):
        params = {
            "include_roles": include_roles,
            "include_permissions": include_permissions,
            "page_size": page_size,
            "page": page
        }
        return self._handle_request(requests.get, "/v1/users", params)

    def get_user(self, user_id, include_roles=False, include_permissions=False, include_bans=False):
        params = {
            "include_roles": include_roles,
            "include_permissions": include_permissions,
            "include_bans": include_bans
        }
        return self._handle_request(requests.get, f"/v1/users/{user_id}", params)

    def create_or_update_user(self, user_data):
        return self._handle_request(requests.post, "/users", json=user_data)

    def delete_user(self, user_id):
        return self._handle_request(requests.delete, f"/users/{user_id}")

    def log_in_with_key(self):
        return self._handle_request(requests.post, "/users/log_in_with_key")

    def log_in(self, login_data):
        return self._handle_request(requests.post, "/users/log_in", json=login_data)

    def log_in_server(self, server_login_data):
        return self._handle_request(requests.post, "/users/log_in_server", json=server_login_data)

    def create_user_api_key(self, user_id):
        return self._handle_request(requests.post, f"/users/{user_id}/api_key")

    # station endpoints
    def get_stations(self, include_config=False, include_deployments=False, include_offline_stations=True, page_size=100, page=1):
        params = {
            "include_config": include_config,
            "include_deployments": include_deployments,
            "include_offline_stations": include_offline_stations,
            "page_size": page_size,
            "page": page
        }
        return self._handle_request(requests.get, "/v1/stations", params)

    def get_station(self, station_id, include_config=True, include_deployments=True):
        params = {
            "include_config": include_config,
            "include_deployments": include_deployments
        }
        return self._handle_request(requests.get, f"/stations/{station_id}", params)

    def create_station(self, station_data):
        return self._handle_request(requests.post, "/stations/create", json=station_data)

    def update_station(self, station_id, station_data):
        return self._handle_request(requests.patch, f"/stations/{station_id}", json=station_data)

    def delete_station(self, station_id):
        return self._handle_request(requests.delete, f"/stations/{station_id}")

    # station cfg shiz
    def get_station_config(self, station_id):
        return self._handle_request(requests.get, f"/stations/{station_id}/config")

    def set_station_config(self, station_id, config_data):
        return self._handle_request(requests.post, f"/stations/{station_id}/config", json=config_data)

    def delete_station_config(self, station_id, config_keys):
        return self._handle_request(requests.delete, f"/stations/{station_id}/config", json=config_keys)

    # event stuff
    def get_station_events(self, station_id, get_past_events=False):
        params = {"get_past_events": get_past_events}
        return self._handle_request(requests.get, f"/v1/stations/{station_id}/events", params)

    def create_station_event(self, station_id, event_data):
        return self._handle_request(requests.post, f"/v1/stations/{station_id}/event", json=event_data)

    def get_event(self, event_id):
        return self._handle_request(requests.get, f"/v1/events/{event_id}")

    def update_station_event(self, station_id, event_id, event_data):
        return self._handle_request(requests.patch, f"/v1/stations/{station_id}/event/{event_id}", json=event_data)

    def delete_station_event(self, station_id, event_id):
        return self._handle_request(requests.delete, f"/v1/stations/{station_id}/event/{event_id}")

    # role endpoints
    def add_role_to_user(self, station_id, user_id, role_id):
        return self._handle_request(requests.post, f"/stations/{station_id}/users/{user_id}/roles/{role_id}")

    def remove_role_from_user(self, station_id, user_id, role_id):
        return self._handle_request(requests.delete, f"/stations/{station_id}/users/{user_id}/role/{role_id}")

    def create_role(self, station_id, role_data):
        return self._handle_request(requests.post, f"/stations/{station_id}/roles", json=role_data)

    def delete_role(self, station_id, role_id):
        return self._handle_request(requests.delete, f"/stations/{station_id}/roles/{role_id}")

    # ban stuffs (scary!!)
    def ban_user(self, station_id, user_id, duration, reason):
        params = {"duration": duration}
        data = {"reason": reason}
        return self._handle_request(requests.post, f"/v1/stations/{station_id}/users/{user_id}/ban", params=params, json=data)

    def unban_user(self, station_id, user_id):
        return self._handle_request(requests.patch, f"/v1/stations/{station_id}/users/{user_id}/unban")

    def get_station_bans(self, station_id, include_revoked=False, include_expired=False):
        params = {"include_revoked": include_revoked, "include_expired": include_expired}
        return self._handle_request(requests.get, f"/v1/stations/{station_id}/bans", params)