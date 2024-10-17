import requests

class OrionDriftAPI:
    def __init__(self, api_key, base_url="https://api.oriondriftvr.com"):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def _handle_request(self, method, url, **kwargs):
        try:
            response = method(url, headers=self.headers, **kwargs)
            response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

    # User Endpoints
    def get_users(self, include_roles=False, include_permissions=False, page_size=100, page=1):
        url = f"{self.base_url}/v1/users"
        params = {
            "include_roles": include_roles,
            "include_permissions": include_permissions,
            "page_size": page_size,
            "page": page
        }
        return self._handle_request(requests.get, url, params=params)

    def get_user(self, user_id, include_roles=False, include_permissions=False, include_bans=False):
        url = f"{self.base_url}/v1/users/{user_id}"
        params = {
            "include_roles": include_roles,
            "include_permissions": include_permissions,
            "include_bans": include_bans
        }
        return self._handle_request(requests.get, url, params=params)

    def create_or_update_user(self, user_data):
        url = f"{self.base_url}/users"
        return self._handle_request(requests.post, url, json=user_data)

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        return self._handle_request(requests.delete, url)

    def log_in_with_key(self):
        url = f"{self.base_url}/users/log_in_with_key"
        return self._handle_request(requests.post, url)

    def log_in(self, login_data):
        url = f"{self.base_url}/users/log_in"
        return self._handle_request(requests.post, url, json=login_data)

    def log_in_server(self, server_login_data):
        url = f"{self.base_url}/users/log_in_server"
        return self._handle_request(requests.post, url, json=server_login_data)

    def create_user_api_key(self, user_id):
        url = f"{self.base_url}/users/{user_id}/api_key"
        return self._handle_request(requests.post, url)

    # Station Endpoints
    def get_stations(self, include_config=False, include_deployments=False, include_offline_stations=True, page_size=100, page=1):
        url = f"{self.base_url}/v1/stations"
        params = {
            "include_config": include_config,
            "include_deployments": include_deployments,
            "include_offline_stations": include_offline_stations,
            "page_size": page_size,
            "page": page
        }
        return self._handle_request(requests.get, url, params=params)

    def get_station(self, station_id, include_config=True, include_deployments=True):
        url = f"{self.base_url}/stations/{station_id}"
        params = {
            "include_config": include_config,
            "include_deployments": include_deployments
        }
        return self._handle_request(requests.get, url, params=params)

    def create_station(self, station_data):
        url = f"{self.base_url}/stations/create"
        return self._handle_request(requests.post, url, json=station_data)

    def update_station(self, station_id, station_data):
        url = f"{self.base_url}/stations/{station_id}"
        return self._handle_request(requests.patch, url, json=station_data)

    def delete_station(self, station_id):
        url = f"{self.base_url}/stations/{station_id}"
        return self._handle_request(requests.delete, url)

    # Station Config
    def get_station_config(self, station_id):
        url = f"{self.base_url}/stations/{station_id}/config"
        return self._handle_request(requests.get, url)

    def set_station_config(self, station_id, config_data):
        url = f"{self.base_url}/stations/{station_id}/config"
        return self._handle_request(requests.post, url, json=config_data)

    def delete_station_config(self, station_id, config_keys):
        url = f"{self.base_url}/stations/{station_id}/config"
        return self._handle_request(requests.delete, url, json=config_keys)

    # Events
    def get_station_events(self, station_id, get_past_events=False):
        url = f"{self.base_url}/v1/stations/{station_id}/events"
        params = {"get_past_events": get_past_events}
        return self._handle_request(requests.get, url, params=params)

    def create_station_event(self, station_id, event_data):
        url = f"{self.base_url}/v1/stations/{station_id}/event"
        return self._handle_request(requests.post, url, json=event_data)

    def get_event(self, event_id):
        url = f"{self.base_url}/v1/events/{event_id}"
        return self._handle_request(requests.get, url)

    def update_station_event(self, station_id, event_id, event_data):
        url = f"{self.base_url}/v1/stations/{station_id}/event/{event_id}"
        return self._handle_request(requests.patch, url, json=event_data)

    def delete_station_event(self, station_id, event_id):
        url = f"{self.base_url}/v1/stations/{station_id}/event/{event_id}"
        return self._handle_request(requests.delete, url)

    # Roles
    def add_role_to_user(self, station_id, user_id, role_id):
        url = f"{self.base_url}/stations/{station_id}/users/{user_id}/roles/{role_id}"
        return self._handle_request(requests.post, url)

    def remove_role_from_user(self, station_id, user_id, role_id):
        url = f"{self.base_url}/stations/{station_id}/users/{user_id}/role/{role_id}"
        return self._handle_request(requests.delete, url)

    def create_role(self, station_id, role_data):
        url = f"{self.base_url}/stations/{station_id}/roles"
        return self._handle_request(requests.post, url, json=role_data)

    def delete_role(self, station_id, role_id):
        url = f"{self.base_url}/stations/{station_id}/roles/{role_id}"
        return self._handle_request(requests.delete, url)

    # Bans
    def ban_user(self, station_id, user_id, duration, reason):
        url = f"{self.base_url}/v1/stations/{station_id}/users/{user_id}/ban"
        params = {"duration": duration}
        data = {"reason": reason}
        return self._handle_request(requests.post, url, params=params, json=data)

    def unban_user(self, station_id, user_id):
        url = f"{self.base_url}/v1/stations/{station_id}/users/{user_id}/unban"
        return self._handle_request(requests.patch, url)

    def get_station_bans(self, station_id, include_revoked=False, include_expired=False):
        url = f"{self.base_url}/v1/stations/{station_id}/bans"
        params = {
            "include_revoked": include_revoked,
            "include_expired": include_expired
        }
        return self._handle_request(requests.get, url, params=params)