# hideme
Protect your privacy and keep out anyone tracking you over WiFi networks.

## Disclaimer
I'm not responsible for bricked devices, dead SD cards, thermonuclear war, or you getting fired because the alarm app failed (like it did for me...).

## Features

- Randomizes MAC address.
- Randomizes Hostname.
- No reboot required.

## Requirements

- Qualcomm Snapdragon Android Device.
- Root permission.
- Terminal Emulator (Termux for best compatibility)

## Setup (Using Termux)

- Install [Termux](https://f-droid.org/en/packages/com.termux/).
- Give Termux Root Permission.
- Install Python: `pkg install python`.
- Save `hideme.py` script to your Android device.
- Using any Root explorer, navigate to: `/data/data/com.termux/files/usr/etc/bash.bashrc`
- Add this line at the end: `alias hideme='python /path/to/script/hideme.py'`
- Restart Termux.

## Usage

Just type `hideme` on Termux.

## Note

To revert to your original MAC, reboot your device.
