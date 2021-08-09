#removed code from bmc_control_m
    def authenticate(self, credentials_file, https=True):
        self.https = https
        with open(credentials_file) as json_file:
            credentials = json.load(json_file)
            self.username = credentials["user"]
            self.password = credentials["password"]
            self.uri = credentials["uri"]

        # login
        r_login = requests.post(
            self.uri + "/automation-api/session/login",
            json={"username": self.username, "password": self.password},
            verify=self.https,
        )

        if r_login.status_code != requests.codes.ok:
            print("Failure Logining into ", self.uri)
            print(r_login.content)
            return r_login.status_code

        print("Successfully logged into ", self.uri)
        self.token = r_login.json()["token"]
        print("Token =", self.token)
        return r_login.status_code
