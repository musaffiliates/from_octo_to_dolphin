from library import OctoBrowser, DolphinAnty
from config import OCTO_TOKEN, DOLPHIN_TOKEN
from auxiliary import Auxiliary
from datetime import datetime
from termcolor import colored

octo_browser = OctoBrowser(OCTO_TOKEN)
dolphin_anty = DolphinAnty(DOLPHIN_TOKEN)

for item in octo_browser.get_profiles_uuids():
    info = octo_browser.get_profile_info(item)
    auxiliary = Auxiliary(info)
    response = dolphin_anty.create_profile(name=info['name'], tags=info['tags'], platform=auxiliary.platform(),
                                           useragent=info['useragent'], vendor=info['webgl_renderer'],
                                           renderer=info['webgl_renderer'], notes=auxiliary.notes(),
                                           proxy=auxiliary.proxy(), cpu=info['cpu_cores'],  ram=info['ram_memory'],
                                           screen_resolution=info['screen_resolution'],
                                           audio_inputs=info['audio_inputs'], video_inputs=info['video_inputs'],
                                           audio_outputs=info['audio_outputs'])
    if response['success'] == 1:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Profile {info["name"]} - '
              f'{colored("successfully created", "green")}')
    else:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Profile {info["name"]} - '
              f'{colored("Opps! Something went wrong!", "red")}')

print(f'\n\n{colored("Congratulations! Migration process successfully completed!", "green")}')
