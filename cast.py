import time
import random
import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()

pychromecast.discovery.stop_discovery(browser)

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Home"])

castaudio = chromecasts[0]

castaudio.wait()

#castaudio.set_volume(0.35)

#print(castaudio.name)

#print(castaudio.status)

abatharAzan = 'http://10.0.4.164/audio/Abathar-Azan.mp3' #'https://ecnetsolutions.ca/Duas/Abathar-Azan.mp3'
azaan = 'http://10.0.4.164/audio/Azaan.mp3' #'https://ecnetsolutions.ca/Duas/Azaan.mp3'
beautifulAzan = 'http://10.0.4.164/audio/adhaan.mp3' #'https://ecnetsolutions.ca/Duas/Beautiful-Azan.mp3'
syedjalalAzan = 'http://10.0.4.164/audio/Azan-Syed-Jalal.mp3' #'https://ecnetsolutions.ca/Duas/Azan-Syed-Jalal.mp3'
azanIraq = 'http://10.0.4.164/audio/AzanIraq.mp3'
AdhaanShia2 = 'http://10.0.4.164/audio/AdhaanShia2.mp3' 
items = [abatharAzan, azaan, beautifulAzan, beautifulAzan, syedjalalAzan, azanIraq, AdhaanShia2]
play = random.choice(items)

mc = castaudio.media_controller
#print(play)
mc.play_media(play, 'audio/mp3')

mc.block_until_active()

#print(mc.status)


pychromecast.discovery.stop_discovery(browser)
