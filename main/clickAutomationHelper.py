import pyautogui as ptg
import time
import win32gui
from main import imagesearch
from PIL import Image
from pathlib import Path

from main.imagesearch import imagesearch, click_image, imagesearcharea

project_dir = str(Path(__file__).parents[1])
screenshots_dir = project_dir + '\\main\\screenshots\\'


def this_is_on_screen(imageName, x1=None, y1=None, x2=None, y2=None):
    image_path = screenshots_dir + imageName + '.png'
    if x1 and y1 and x2 and y2:
        pos = imagesearcharea(image_path, x1, y1, x2, y2)
    else:
        pos = imagesearch(image_path, precision=.85)

    if pos[0] != -1:
        ptg.moveTo(pos[0], pos[1])
        return True
    else:
        return False


def click_button(button_name):
    button_path = screenshots_dir + button_name + '.png'
    pos = imagesearch(button_path)
    img = Image.open(button_path)

    if pos[0] != -1:
        click_image(button_path, pos, "left", 0.001, offset=5)
        img.close()
        return True
    else:
        img.close()
        return False


def drag_right_to_left(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.moveTo(x, y)
        ptg.dragTo(1, y, .5, button='left')
    else:
        ptg.moveTo(1300, 300)
        ptg.dragTo(1, 300, .3, button='left')


def drag_bottom_to_top(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.leftClick(x, y)
        ptg.dragTo(x, 255, 1, button='left')
        # ptg.scroll(-10000)
    if x and not y:
        ptg.moveTo(x, 996)
        ptg.dragTo(x, 255, 1, button='left')
    if not x and not y:
        ptg.moveTo(930, 996)
        ptg.dragTo(928, 255, 1, button='left')


def clickstage(stageNumber):
    pos = imagesearch(stageNumber, precision=.9)
    posList = list(pos)
    posList[0] = posList[0] + 859
    posList[1] = posList[1] + 50
    pos = tuple(posList)
    if pos[0] != -1:
        ptg.moveTo(pos[0], pos[1])
        ptg.click(clicks=1, button='left')
    else:
        print("Stage Number Not There")


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def move_to_end_of_chamption_list():
    drag_right_to_left(1342, 925)
    time.sleep(1)
    drag_right_to_left(1342, 925)
    time.sleep(1)
    drag_right_to_left(1342, 925)
    time.sleep(1)


def remove_old_food_champs(champ_position):
    if champ_position[0] == 1:
        ptg.moveTo(465, 291)
        ptg.click(clicks=1, button='left')
    if champ_position[1] == 1:
        ptg.moveTo(461, 484)
        ptg.click(clicks=1, button='left')
    if champ_position[2] == 1:
        ptg.moveTo(298, 394)
        ptg.click(clicks=1, button='left')


def click_last_four_champs_in_champ_list():
    ptg.moveTo(1360, 943)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

    ptg.moveTo(1351, 764)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

    ptg.moveTo(1226, 759)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

    ptg.moveTo(1230, 940)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)


def sort_champ_list_by_level():
    ptg.moveTo(138, 607)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)
    ptg.moveTo(392, 492)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)


def run_max_level_routine():
    champ_position_array = []
    if this_is_on_screen("word_max_level", 447, 403, 668, 732):
        print("max level 0")

    if this_is_on_screen("word_max_level", 700, 391, 921, 863):
        print("max level 1")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if this_is_on_screen("word_max_level", 986, 409, 1200, 864):
        print("max level 2")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if this_is_on_screen("word_max_level", 1254, 399, 1467, 858):
        print("max level 3")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if champ_position_array != [0, 0, 0]:
        click_button("button_edit_team")
        time.sleep(1)
        if this_is_on_screen("note_full_energy"):
            print("WARNING: Waiting 8 Minutes because out of energy.")
            time.sleep(600)
            click_button("button_edit_team")
        time.sleep(1)
        remove_old_food_champs(champ_position_array)
        sort_champ_list_by_level()
        move_to_end_of_chamption_list()
        click_last_four_champs_in_champ_list()
        click_button("button_start")
    else:
        print("No new max levels found")


def minimize_window():
    ptg.hotkey('win', 'down')


def from_home_navigate_to_campaign_12_3_start():
    if this_is_on_screen("button_home_battle"):
        click_button("button_home_battle")
        time.sleep(1)
        click_button("button_campaign")
        time.sleep(1)
        drag_right_to_left()
        drag_right_to_left()
        drag_right_to_left()
        click_button("campaign_12")
        time.sleep(1)
        drag_bottom_to_top()
        time.sleep(1)
        clickstage("campaign_12_3")
        time.sleep(1)
        click_button("button_start")


def click_all_heart_shields():
    while this_is_on_screen("button_heart_shield"):
        click_x = 650
        click_y = 307
        click_y_shield_col(click_x, click_y)
        drag_bottom_to_top(x=650)


def click_y_shield_col(click_x, click_y):
    for x in range(0, 6):
        click_x_shield_row(click_x, click_y)
        click_y += 140


def click_x_shield_row(click_x, click_y):
    for x in range(0, 6):
        ptg.click(x=click_x, y=click_y, clicks=1, button='left', interval=0.02)
        click_x += 133


def click_battle_button():
    click_button("button_battle")
    print("Battle button found")


def quest_checker():
    click_button("button_quests")
    time.sleep(2)
    ptg.click(x=188, y=188)
    time.sleep(1)
    drag_bottom_to_top()
    return this_is_on_screen("quests_beat_campaign_3_times")


def summon_three_champions():
    click_button("button_portal")
    time.sleep(2)
    click_button("button_summon_buy")


def clan_boss_routine():
    click_button("button_battle")
    time.sleep(1)
    drag_right_to_left()
    time.sleep(1)
    click_button("battle_menu_clanBoss")
    time.sleep(1)
    click_button("clanBoss_brutal")
    time.sleep(1)
    click_button("clanBoss_button_battle")
    time.sleep(1)
    click_button("clanBoss_button_start")
    while True:
        if this_is_on_screen("note_result"):
            click_button("button_replay")
            time.sleep(1)
            if this_is_on_screen("clanBoss_buy_key"):
                break
    click_button("button_bastion")
    click_button("button_bastion")


def collect_gem_mine():
    ptg.click(x=121,y=856)

def get_image_coordinates(button_name):
    button_path = screenshots_dir + button_name + '.png'
    pos = imagesearch(button_path)
    return pos


def campaign_routine():
    victory_count = 0
    do_boss_campaign = quest_checker()
    click_button("button_exit")
    time.sleep(1)
    click_button("button_battle")
    time.sleep(1)
    click_button("battle_menu_campaign")
    time.sleep(1)

    while (this_is_on_screen("campaign_12") == False):
        drag_right_to_left()

    time.sleep(.5)
    click_button("campaign_12")

    if do_boss_campaign:
        while (this_is_on_screen("campaign_12_7") == False):
            drag_bottom_to_top()
            click_button("campaign_button_battle7")
            quest_complete_max = 3
        time.sleep(.5)
    else:
        click_button("campaign_12_3")
        click_button("campaign_button_battle3")
        quest_complete_max = 7

    time.sleep(.5)
    click_button("campaign_button_start")

    while victory_count < quest_complete_max:
        if this_is_on_screen("button_buy_energy"):
            time.sleep(600)
        click_button("button_replay")
        if this_is_on_screen("screen_victory"):
            victory_count += 1

    click_button("button_bastion")

def summon_3_champions_routine():
    summon_count = 0
    click_button("button_portal")
    time.sleep(1)
    click_button("portal_menu_button_summon")
    summon_count += 1
    time.sleep(5)

    while summon_count < 3:
        time.sleep(1)
        if this_is_on_screen("portal_menu_button_summonRepeat"):
            click_button("portal_menu_button_summonRepeat")
            summon_count += 1

    time.sleep(5)

    while True:
        if this_is_on_screen("button_exit"):
            click_button("button_exit")
            time.sleep(.5)
            click_button("button_exit")
            break

def market_routine():
    click_button("button_market")
    time.sleep(1)
    if not this_is_on_screen("market_menu_button_5000"):
        drag_bottom_to_top()

    else:
        click_button("market_menu_button_5000")
        time.sleep(.5)
        click_button("market_menu_button_5000_buy")

    time.sleep(.5)

    click_button("button_exit")