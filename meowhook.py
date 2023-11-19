import requests, colorama, time, os


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://cdn.discordapp.com/emojis/1103290034930581615.png"})
            if data.status_code == 204:
                print(f"{colorama.Back.CYAN} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.CYAN}Webhook deleted!')
    print(f'{colorama.Fore.GREEN}All tasks complete.')


def initialize():
    print(f"""{colorama.Fore.CYAN}
                               _                 _    
                              | |               | |   
  _ __ ___   ___  _____      _| |__   ___   ___ | | __
 | '_ ` _ \ / _ \/ _ \ \ /\ / / '_ \ / _ \ / _ \| |/ /
 | | | | | |  __/ (_) \ V  V /| | | | (_) | (_) |   <
 |_| |_| |_|\___|\___/ \_/\_/ |_| |_|\___/ \___/|_|\_\.
                                       -by zurly
     """)
    webhook = input("Enter the webhook > ")
    name = input("Enter custom webhook name > ")
    message = input("Enter the message to be spammed > ")
    delay = input("Enter the delay between messages [int/float] (0.1 recommended) > ")
    amount = input("Enter the amount of messages to be spammed [int/inf] (100 recommended) > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls')
    os.system('title x_x - meowhook')
    colorama.init()
    initialize()