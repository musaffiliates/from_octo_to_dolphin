import requests


class DolphinAnty:
    def __init__(self, token):
        self.token = token

    def create_profile(self, name, tags, platform, useragent, vendor, renderer, notes, proxy, cpu, ram,
                       screen_resolution, audio_inputs, video_inputs, audio_outputs):
        headers = {
            'Authorization': self.token,
        }

        json_data = {
            'name': name,
            'tags': tags,
            'platform': platform,
            'browserType': 'anty',
            'mainWebsite': '',
            'useragent': {
                'mode': 'manual',
                'value': useragent,
            },
            'webrtc': {
                'mode': 'altered',
                'ipAddress': None,
            },
            'canvas': {
                'mode': 'real',
            },
            'webgl': {
                'mode': 'real',
            },
            'webglInfo': {
                'mode': 'manual',
                'vendor': vendor,
                'renderer': renderer,
            },
            'clientRect': {
                'mode': 'real',
            },
            'notes': {
                'content': notes,
                'color': 'blue',
                'style': 'text',
                'icon': None,
            },
            'timezone': {
                'mode': 'auto',
                'value': None,
            },
            'locale': {
                'mode': 'auto',
                'value': None,
            },
            'proxy': proxy,
            'statusId': 0,
            'geolocation': {
                'mode': 'auto',
                'latitude': None,
                'longitude': None,
                'accuracy': None,
            },
            'cpu': {
                'mode': 'manual',
                'value': cpu,
            },
            'memory': {
                'mode': 'manual',
                'value': ram,
            },
            'screen': {
                'mode': 'manual',
                'resolution': screen_resolution,
            },
            'mediaDevices': {
                'mode': 'manual',
                'audioInputs': audio_inputs,
                'videoInputs': video_inputs,
                'audioOutputs': audio_outputs,
            },
            'ports': {
                'mode': 'protect',
                'blacklist': '3389,5900,5800,7070,6568,5938',
            },
            'doNotTrack': False
        }

        response = requests.post('http://142.132.182.77:81/browser_profiles', headers=headers, json=json_data)

        return response.json()


class OctoBrowser:
    def __init__(self, token):
        self.token = token

    def get_profiles_uuids(self):
        url = "https://app.octobrowser.net/api/v2/automation/profiles"

        uuids = []
        page = 0
        while True:
            params = {
                'page': f'{page}',
                'page_len': '10',
            }
            headers = {
                'X-Octo-Api-Token': self.token,
            }

            response = requests.request("GET", url, headers=headers, params=params)

            if response.json()['data']:
                for uuid in response.json()['data']:
                    uuids.append(uuid['uuid'])
                page += 1
                continue
            else:
                return uuids

    def get_profile_info(self, profile_uuid):
        url = f"https://app.octobrowser.net/api/v2/automation/profiles/{profile_uuid}"

        headers = {
            'X-Octo-Api-Token': self.token,
        }

        response = requests.request("GET", url, headers=headers)

        result = response.json()['data']

        return {
            'name': result['title'],
            'notes': result['description'],
            'useragent': result['user_agent'],
            'proxy': result['proxy'],
            'tags': result['tags'],
            'platform': result['fingerprint']['os'],
            'webgl_renderer': result['fingerprint']['renderer'],
            'cpu_cores': result['fingerprint']['cpu'],
            'ram_memory': result['fingerprint']['ram'],
            'screen_resolution': result['fingerprint']['screen'],
            'audio_inputs': result['fingerprint']['media_devices']['audio_in'],
            'video_inputs': result['fingerprint']['media_devices']['video_in'],
            'audio_outputs': result['fingerprint']['media_devices']['audio_out'],
        }
