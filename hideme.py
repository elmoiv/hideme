from random import randint as r, shuffle as s, choice as c
from os import popen

MAC_FILE = '/sys/devices/platform/soc/a000000.qcom,wcnss-wlan/wcnss_mac_addr'
ALL = [*map(chr, range(1500, 15500))]
R = lambda e=255: r(0, e)

def su(cmd):
    """
    Execute Super User commands (without logging)
    """
    _ = popen(f'su -c "{cmd}"').read()
    
# Turn Off Wifi
print('\nTurning WiFi OFF...')
su('svc wifi disable')

# Change MAC Address
new_mac = "%x%x:%02x:%02x:%02x:%02x:%02x" \
        % (R(15), c(range(0, 16, 2)), R(), R(), R(), R(), R())

## Write new mac to the Xiaomi specific file
su(f'printf \\"{new_mac}\n\\" > {MAC_FILE}')

# Change Host Name
s(ALL)
new_host = ''.join(ALL[:r(10, 18)])
su(f'setprop net.hostname "{new_host}"')

# Result
print('\nNew Mac Address:', new_mac)
print('New Host Name:  ', new_host, '\n')

# Turn On WiFi
print('Turning WiFi ON...')
su('svc wifi enable')

print('\nDone')