# coding=utf8
from sys import stderr

import pyperclip
import pyautogui
from tqdm import tqdm
import gen_img
import pickle

pyautogui.PAUSE = 1
pause_time = 0
image_pause = 0

top_friend_position = (1002, -1107)
username_position = (2736, -1909)
bottom_friend_position = (1018, -67)
alias_position = (2445, -1951)  # TODO update
search_bar = (892, -2097)
first_search_res = (1069, -1935)
id_position = (2614, -1558)


def copy_selection():
    pyperclip.copy("")
    pyautogui.hotkey('ctrl', 'c')
    val = pyperclip.paste()
    pyperclip.copy("")
    return val


def click(coords, numClicks=1):
    pyautogui.click(coords[0], coords[1], numClicks)


def get_friends():
    # Get a list of current friends and save results into a file locally
    # Every year, delete the pkl file before the process
    try:
        with open('friends.pkl', 'rb') as f:
            friends = pickle.load(f)
    except FileNotFoundError:
        friends = []
        click(top_friend_position)
        # hard coded num of friends, so you don't need to detect end of friend list
        num_friends = 388
        last_selection = None
        for _ in tqdm(range(num_friends)):
            friend = {}
            click(username_position, 2)
            cur_selection = copy_selection()

            if last_selection == cur_selection:
                print("here")
                for _ in range(8):
                    pyautogui.hotkey('shift', 'tab')
                pyautogui.press('down')
                continue

            last_selection = cur_selection
            friend['username'] = cur_selection
            # click(alias_position, 2)
            # friend['alias'] = copy_selection()
            print(friend)
            friends.append(friend)
            # Get back to the friend list
            # 10 is probably more than necessary but
            for _ in range(7):
                pyautogui.hotkey('shift', 'tab')

            # click(bottom_friend_position, 1)
            pyautogui.press('down')

        # dedup
        aliases = {friend["alias"] for friend in friends if friend["alias"]}
        unique = []

        for alias in aliases:
            people = [friend for friend in friends if friend["alias"] == alias]
            if len(people) > 1:
                print(f"WARNING: {len(people)}", file=stderr)
            unique.append(people[0])

        with open('friends.pkl', 'wb') as f:
            pickle.dump(unique, f)

    return friends


def paste_img(name_to_use):
    pyperclip.copy("")
    generator = gen_img.Gen_Img()
    generator.gen_img(name_to_use)
    pyautogui.hotkey('ctrl', 'v')


def paste_wish(name_to_use):
    pyperclip.copy("")
    wish = f'祝{name_to_use}福兔迎祥! 感谢您给予的帮助!\n\nzackLight.com'
    pyperclip.copy(wish)
    pyautogui.hotkey('ctrl', 'v')


def send_wishes_gui():
    # missed = [""]
    skip = ["Zack Light", "A℡小袋鼠在线"]
    friends = get_friends()

    for i in tqdm(range(len(friends))):
        friend = friends[i]
        name_to_use = friend["alias"]

        if name_to_use in skip or "sent" in friend:
            continue

        print(f"{name_to_use}")

        # search
        click(search_bar, 2)
        pyperclip.copy("")
        pyperclip.copy(name_to_use)
        pyautogui.hotkey('ctrl', 'v')
        click(first_search_res)

        # send
        pyperclip.copy("")
        paste_wish(name_to_use)
        paste_img(name_to_use)
        pyautogui.press('enter')
        friend["sent"] = True

        # check_logged_in()
        with open('friends.pkl', 'wb') as f:
            pickle.dump(friends, f)


if __name__ == "__main__":
    get_friends()
    # send_wishes_gui()
