import os.path
import os
import time
import getopt
import sys

# These are the partitions on most A/B devices with fastbootd support, this is script is made for
# OnePlus 8T but can be adapted for any device
partitions = ("boot", "dtbo", "recovery", "vbmeta", "vbmeta_system", "system", "product", "system_ext", "odm", "vendor")

# Fancy colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print("\n" + color.BOLD + color.UNDERLINE + color.CYAN + "2021-2022\nby FraSharp @ GitHub.com" + color.END)

print(color.RED + "\npreparing to flash rom, 5 seconds to abort..." + color.END)
time.sleep(5)

print(color.RED + "starting to flash rom...\n" + color.END)
time.sleep(1)

for partition in partitions:
	if not os.path.exists(f"./{partition}.img"):
		print(color.BOLD + color.PURPLE + f"no {partition} to flash" + color.END)
	elif partition == "vbmeta" or partition == "vbmeta_system":
		os.system(f"fastboot flash --disable-verity {partition} {partition}.img")
	else:
		os.system(f"fastboot flash {partition} {partition}.img")

print("\n" + color.BOLD + color.RED + "format data if coming from another rom, else just reboot" + color.END)
