import time
from main.clickAutomationHelper import *


if __name__ == '__main__':
    # click_all_heart_shields()
    # quest_checker()

    while True:
        if this_is_on_screen("button_buy_energy"):
            print("WARNING: Waiting 8 Minutes because out of energy.")
            time.sleep(600)
        if this_is_on_screen("alert_maintenence"):
            print("WARNING: Waiting 15 Minutes because of maintenence")
            time.sleep(900)
            click_button("screenshots/button_maintenence_ok")
        run_max_level_routine()
        time.sleep(1)
        click_button("button_replay")
        time.sleep(1)
