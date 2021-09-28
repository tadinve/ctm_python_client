import ctm_api_client as ctm_api_client
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Session:
    def __init__(self, endpoint=None, username=None, password=None, api_key=None):
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.api_key = api_key

        self.configuration = ctm_api_client.Configuration()
        self.configuration.host = endpoint
        self.configuration.verify_ssl = False

        if password:
            self.configuration.api_key_prefix["Authorization"] = "Bearer"
            self.configuration.api_key["Authorization"] = self.get_token()
        else:
            self.configuration.api_key["Authorization"] = api_key

    def login(self):
        api_session = ctm_api_client.SessionApi(
            ctm_api_client.ApiClient(self.configuration)
        )
        res = api_session.do_login(
            {"username": self.username, "password": self.password}
        )

        return res

    def get_token(self):
        return self.login().token
