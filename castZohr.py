import time

import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()

pychromecast.discovery.stop_discovery(browser)

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Home"])

castaudio = chromecasts[0]

castaudio.wait()

#castaudio.set_volume(0.35)

#print(castaudio.name)

#print(castaudio.status)

mc = castaudio.media_controller

mc.play_media('https://ecnetsolutions.ca/Duas/SuraFatir.mp3', 'audio/mp3')

mc.block_until_active()

#print(mc.status)

pychromecast.discovery.stop_discovery(browser)
