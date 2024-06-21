#################################################################
############ SCRIPT TO BE USED TO UPDATE ALL DEVICES ############
################ RUN WITH `python update-all.py` ################
#################################################################


import subprocess
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def update_function(deviceyaml):
    print(f"{Fore.BLUE}Updating " + deviceyaml + f"! {Style.RESET_ALL}")
    time.sleep(1)
    subprocess.run(["esphome", "run", deviceyaml, "--no-logs"]) 
    print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
    time.sleep(1)

update_function("bedrgb.yaml")
update_function("bedroomwall.yaml")
update_function("bedsense.yaml")
update_function("cabinetesp.yaml")
update_function("garagesensors.yaml")
update_function("sonoff1.yaml")
update_function("sonoff2.yaml")
update_function("sonoff3.yaml")
update_function("sonoff4.yaml")
update_function("sonoff5.yaml")
update_function("sunsense.yaml")
update_function("workbench.yaml")