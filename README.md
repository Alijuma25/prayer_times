**Prayer Times Automation**

This repository contains scripts to automate prayer time announcements using a Raspberry Pi and Chromecast.

**Features**

Plays Azaan (Adhan) and Imsak alerts at the correct times.
Uses pychromecast to cast audio to a Chromecast device.
Allows customization of prayer times.
Includes update scripts for prayer time calculations.

**Files Included**

praytimes.py – Handles prayer time calculations.
updateAzaanTimers.py – Updates Azaan schedule.
castFajr.py, castImsak.py, castZohr.py, castMaghrib.py – Scripts to cast prayer time audio.
playFajr.sh, playImsak.sh, playZohr.sh, playMaghrib.sh, playAzaan.sh – Shell scripts to execute the casting scripts.

**Notes**

The scripts require a local server to host the audio files.
Update the audio file paths as needed.
