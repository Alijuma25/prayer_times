import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()

pychromecast.discovery.stop_discovery(browser)

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Home"])

castaudio = chromecasts[0]

castaudio.wait()

mc = castaudio.media_controller

mc.play_media('http://10.0.4.165/imsak.mp3', 'audio/mp3')

mc.block_until_active()

pychromecast.discovery.stop_discovery(browser)
