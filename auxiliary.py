class Auxiliary:
    def __init__(self, result):
        self.result = result

    def proxy(self):
        if self.result['proxy']:
            return {
                'name': self.result['proxy']['host'],
                'host': self.result['proxy']['host'],
                'port': self.result['proxy']['port'],
                'type': self.result['proxy']['type'],
                'login': self.result['proxy']['login'],
                'password': self.result['proxy']['password'],
                'changeIpUrl': self.result['proxy']['change_ip_url']
            }
        else:
            return None

    def platform(self):
        if self.result['platform'] == 'mac':
            platform = 'macos'
            return platform
        elif self.result['platform'] == 'win':
            platform = 'windows'
            return platform

    def notes(self):
        if self.result['notes']:
            return self.result['notes']
        else:
            return None
