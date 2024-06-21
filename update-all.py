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

print(f"{Fore.BLUE}Updating bedrgb! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "bedrgb.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating bedroomwall! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "bedroomwall.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating bedsense! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "bedsense.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating cabinetesp! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "cabinetesp.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating garagesensors! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "garagesensors.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating sonoff1! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "sonoff1.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating sonoff2! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "sonoff2.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating sonoff3! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "sonoff3.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating sonoff4! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "sonoff4.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating sonoff5! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "sonoff5.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating sunsense! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "sunsense.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)

print(f"{Fore.BLUE}Updating workbench! {Style.RESET_ALL}")
time.sleep(1)
subprocess.run(["esphome", "run", "workbench.yaml", "--no-logs"]) 
print(f"{Fore.BLUE}Updating complete! {Style.RESET_ALL}")
time.sleep(1)