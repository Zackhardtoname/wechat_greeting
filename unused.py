# pyautogui.click(2054, 1950)
# send = input("Send: ")
# if send == " ":
#     pyautogui.click(278, 2060)
#     pyautogui.click(235, 1931)
#     pyautogui.click(278, 2060)
#
#     continue

#
# pyautogui.click(x=1189, y=620) #message btn
# pyautogui.click(x=1189, y=668) #message btn loc 2
#
# pyautogui.click(2054, 1950)
# wish = contruct_wish(RemarkName, NickName)

# res = pyautogui.locateOnScreen('msg_2.jpg')
# if not res:
#     res = []
#     res.append(1214)
#     res.append(703)
# pyautogui.click(res[0], res[1]) #text

# if wish != None:
# print(wish)
# pyperclip.copy(wish)

# pyautogui.hotkey('ctrl', 'win', '1')  # ctrl-v to paste
# time.sleep(.3)
# pyautogui.press('enter')

# import itchat
#   ...:
#   ...:itchat.auto_login(True)
#
# friends = itchat.get_friends()
# with open('friends.pkl', 'wb') as f:
#    ...:    pickle.dump(friends, f)

# cur_pos = self.update_pos_and_font(cur_pos, font, msg)
# self.draw.text(self.cur_pos, footer2, font=font, fill=self.font_color)

# image = Image.open(filepath)
# self.img.save(f'./cards/{RemarkName}.jpg')
# image = Image.open(filepath)

# def get_friends():
# try:
#     with open('friends.pkl', 'rb') as f:
#         friends = pickle.load(f)
# except Exception as e:
#     print(e)
#     import itchat
#     itchat.auto_login()
#     friends = itchat.get_friends(update=False)[1:]
#     with open('friends.pkl', 'wb') as f:
#         pickle.dump(friends, f)
# return friends

# # Sometimes wechat would force log you out after sending too many messages
# def check_logged_in():
#     while (not fuzzy_match('./imgs/search_img.png')):
#         confirm = fuzzy_match('./imgs/compressed.jpg') or fuzzy_match('./imgs/login_img.png')
#         if confirm:
#             pyautogui.click(confirm[0], confirm[1])
#             pyautogui.click(confirm[0], confirm[1] + 100)
#             pyautogui.hotkey('winleft', 'left')
#             # pyautogui.hotkey('winleft', 'down')
#
#
# def fuzzy_match(fn, confidence=.9):
#     return pyautogui.locateCenterOnScreen(fn, confidence=confidence)
#
#
# def has_sent_img():
#     return fuzzy_match('./imgs/2020_delete.png')
