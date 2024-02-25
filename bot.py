import json  # data managment
import time
import pynput  # control keyboard and mouse
import numpy as np

# import pyscreenshot as ImageGrab  # only necessary when collecting data if a snap conversation is very long
from chatgpt_wrapper import ChatGPT  # Use this chatgpt wrapper I found on github
import pyperclip  # allows access to keyboard

# # from emoji import (
#     is_emoji,
# )  # figure out if emojis are in a persons name and stuff so we can remove those emojis
#
# def find_mse(ss1, ss2):
#   # Find the mean squared error between two screenshots
#   mse = np.mean((ss1.astype("float") - ss2.astype("float")) ** 2)
#   mse /= float(ss1.shape[0] * ss1.shape[1])
#   return mse
#
# def copy_a_chat(wait_until_done=False):
#   # Move the mouse to lower left hand cornor
#   mouse.position = (356, 977)
#   mouse.click(pynput.mouse.Button.left, 1)
#   time.sleep(0.2)
#   # Stard holding down the mouse button
#   mouse.press(pynput.mouse.Button.left)
#
#   # Move the mouse to upper left corner so that we start highlighting and scrolling up
#   for i in range(10):
#     time.sleep(0.1)
#     mouse.position = (365, 201 - i * 7)
#
#   if wait_until_done: # This will wait until we have copied the entire chat, or the chat stops loading.
#     start_time = time.time()
#     ss = ImageGrab.grab() # Take screenshot
#     time.sleep(1)
#     mse = (find_mse(np.asarray(ss), np.asarray(ImageGrab.grab()))) # Find difference between screen 1 second ago and now
#     while mse > 5e-5 and time.time() - start_time < 10: # If there is a very small difference or it has been 10 seconds
#       ss = ImageGrab.grab()
#       time.sleep(1)
#       mse = (find_mse(np.asarray(ss), np.asarray(ImageGrab.grab())))
#   else:
#     time.sleep(1) # Scroll up for 1 second and copy just that amount of chat
#
#   mouse.position = (365, 202) # Move mouse to upper left corner
#
#   # Copy chat
#   copy_to_clipboard()
#
#   # Stop dragging
#   mouse.release(pynput.mouse.Button.left)
#
#   data = pyperclip.paste()
#   return data
#
# def focus_left_window():
#
#   # Focus the left window:
#   keyboard.press(pynput.keyboard.Key.cmd_l)
#   keyboard.press(pynput.keyboard.Key.left)
#   time.sleep(0.2)
#   keyboard.release(pynput.keyboard.Key.cmd_l)
#   keyboard.release(pynput.keyboard.Key.left)
#
# def focus_right_window():
#   # Focus the right window:
#   keyboard.press(pynput.keyboard.Key.cmd_l)
#   keyboard.press(pynput.keyboard.Key.right)
#   time.sleep(0.2)
#   keyboard.release(pynput.keyboard.Key.cmd_l)
#   keyboard.release(pynput.keyboard.Key.right)
#
# def paste_data(data):
#   # Focus the left window:
#   # focus_left_window()
#
#   pyperclip.copy(data)
#
#   print("DATA HAS BEEN COPIED")
#   mouse.position = (386, 1034)
#
#   time.sleep(1)
#   print("CLICKING ON TEXT BOX")
#   # Click on the text box
#   mouse.click(pynput.mouse.Button.left, 1)
#   time.sleep(1)
#
#   print("PASTING DATA")
#   # paste
#   paste_from_clipboard()
#   time.sleep(1)
#
#   keyboard.press(pynput.keyboard.Key.enter)
#   time.sleep(0.5)
#   keyboard.release(pynput.keyboard.Key.enter)
#
# def copy_to_clipboard():
#   # Copy data
#   keyboard.press(pynput.keyboard.Key.ctrl)
#   keyboard.press("c")
#   time.sleep(0.1)
#   keyboard.release(pynput.keyboard.Key.ctrl)
#   keyboard.release("c")
#
# def paste_from_clipboard():
#   # paste
#   keyboard.press(pynput.keyboard.Key.ctrl)
#   keyboard.press("v")
#   time.sleep(0.1)
#   keyboard.release(pynput.keyboard.Key.ctrl)
#   keyboard.release("v")
#
# def refresh_webpage():
#   # Refresh the screen
#   keyboard.press(pynput.keyboard.Key.ctrl)
#   keyboard.press("r")
#   time.sleep(1)
#   keyboard.release(pynput.keyboard.Key.ctrl)
#   keyboard.release("r")
#
# def see_if_chat_is_forbidden(chat):
#
#   print("For the chat of", chat, "it has the following:", all([(person not in chat) for person in whitelist]))
#   # return False
#   return all([(person.upper() not in chat.upper()) for person in whitelist])
#
# def check_to_see_if_new_chats():
#
#   start_scrolling_position = (12, 348)
#   end_scrolling_position = (234, 1042)
#
#   # if we not at the tippy top
#   # start_scrolling_position = (230, 340)
#   # end_scrolling_position = (230, 1042)
#
#   mouse.position = start_scrolling_position
#   mouse.press(pynput.mouse.Button.left)
#   time.sleep(0.2)
#   mouse.position = end_scrolling_position
#   mouse.release(pynput.mouse.Button.left)
#
#   copy_to_clipboard()
#   data = pyperclip.paste()
#
#   # Clean data
#
#   data = data.replace("\nSearch\n", "")
#
#   data = "".join([c for c in data if not is_emoji(c)])
#
#   # get rid of all of these symbols ·, only if there is a \n and then a number after that \n
#   data = data.split("\n\n")
#
#   # Remove all emojis
#
#
#   # correct_data = ""
#   # for line in data.split("\n·\n"):
#   #   if len(line) > 0 and not line[0].isdigit():
#   #     correct_data += line + "\n"
#
#   individual_chats = data
#   individual_chats = [x for x in individual_chats if x != ""]
#
#   new_chat_indexs = []
#
#   for i, chat in enumerate(individual_chats):
#     if ("\nNew Chat" in chat or "Received" in chat) and not see_if_chat_is_forbidden(chat):
#       new_chat_indexs.append(i)
#
#   return [CONVERSATION_POSITIONS[index] for index in new_chat_indexs]
#
# def start_new_conversations_if_there_is_a_new_person():
#
#   # message if the person you're talkign hasn't started a conversation with you yet (automation)
#   message = "hey [name], what's going on?"
#
#   start_scrolling_position = (15, 334)
#   end_scrolling_position = (234, 1042)
#
#   # not tippy top
#
#   # start_scrolling_position = (230, 340)
#   # end_scrolling_position = (230, 1042)
#
#   mouse.position = start_scrolling_position
#   mouse.press(pynput.mouse.Button.left)
#   time.sleep(0.2)
#   mouse.position = end_scrolling_position
#   mouse.release(pynput.mouse.Button.left)
#
#   copy_to_clipboard()
#   data = pyperclip.paste()
#
#   # Clean data
#
#   data = data.replace("\nSearch\n\n", "")
#
#   data = "".join([c for c in data if not is_emoji(c)])
#
#   # get rid of all of these symbols ·, only if there is a \n and then a number after that \n
#   data = data.split("\n\n")
#
#   individual_chats = data
#   individual_chats = [x for x in individual_chats if x != ""]
#
#   new_peoples = []
#
#   for i, chat in enumerate(individual_chats):
#     if ("Say Hi!" in chat):
#       new_peoples.append([i, chat])
#
#   if len(new_peoples) == 0:
#     return len(new_peoples)
#
#   for people in new_peoples:
#     index = people[0]
#     chat = people[1]
#     name = chat.split("\n")[0]
#
#     # Add the name to the whitelist
#     out_file = open("whitelist.json", "w")
#     whitelist.append(name)
#     json.dump(whitelist, out_file, indent=1)
#     out_file.close()
#
#     name = name.lower()
#     name = name.capitalize()
#     name = name.split(" ")[0]
#     print("Starting a new conversation with", name)
#     # print("Going to say", message.replace("[name]", name))
#     temp_message = message.replace("[name]", name)
#     mouse.position = CONVERSATION_POSITIONS[index]
#     mouse.click(pynput.mouse.Button.left, 1)
#     time.sleep(1)
#     paste_data(temp_message)
#     time.sleep(1)
#
#     mouse.position = (176, 364)
#     time.sleep(0.75)
#     mouse.click(pynput.mouse.Button.left, 1)
#     return len(new_peoples)
#
# def collect_data_on_people_who_stopped_talked_with_you():
#
#
#   start_scrolling_position = (230, 340)
#   end_scrolling_position = (230, 1042)
#
#   mouse.position = start_scrolling_position
#   mouse.press(pynput.mouse.Button.left)
#   time.sleep(0.5)
#   mouse.position = end_scrolling_position
#   mouse.release(pynput.mouse.Button.left)
#
#   copy_to_clipboard()
#
#   data = pyperclip.paste()
#
#   # Clean data
#
#   data = data.replace("\nSearch\n\n", "")
#
#   data = "".join([c for c in data if not is_emoji(c)])
#
#   # get rid of all of these symbols ·, only if there is a \n and then a number after that \n
#   data = data.split("\n\n")
#
#   # Remove all emojis
#
#   # correct_data = ""
#   # for line in data.split("\n·\n"):
#   #   if len(line) > 0 and not line[0].isdigit():
#   #     correct_data += line + "\n"
#
#   individual_chats = data
#   individual_chats = [x for x in individual_chats if x != ""]
#
#   people_who_left_on_opened = []
#   for i, chat in enumerate(individual_chats):
#     if ("Opened" in chat or "Screenshot" in chat or "\n1d" in chat or "\n2d" in chat) and not see_if_chat_is_forbidden(chat):
#       people_who_left_on_opened.append([i, chat])
#   if len(people_who_left_on_opened) == 0:
#     return len(people_who_left_on_opened)
#
#   for people in people_who_left_on_opened:
#     index = people[0]
#     chat = people[1]
#     name = chat.split("\n")[0]
#
#     # Add the name to the AI victims data
#     print("We are looking at", name, index)
#     mouse.position = CONVERSATION_POSITIONS[index]
#     time.sleep(0.75)
#     mouse.click(pynput.mouse.Button.left, 1)
#     data_from_chat = copy_a_chat(wait_until_done=True)
#
#     # data_from_chat.replace(name.upper(), "OTHER_PERSONS_NAME")
#     with open("./Friends/" + "CONVERSATION_" + name.upper() + ".txt", "w") as f:
#       f.write(data_from_chat)
#
#     try:
#       whitelist.remove(name)
#     except Exception as e:
#       print("THERE WAS AN ERROR REMOVING:", name,"\t" , e)
#
#     # Remove the name to the whitelist
#     with open("whitelist.json", "w") as out_file:
#       json.dump(whitelist, out_file, indent=1)
#       out_file.close()
#     return len(people_who_left_on_opened)


if __name__ == "__main__":
    # Get mouse and keyboard
    # mouse = pynput.mouse.Controller()
    # keyboard = pynput.keyboard.Controller()
    #
    # # Position of 1st person in chat list, 2nd person in chat list, etc.
    # global CONVERSATION_POSITIONS
    # CONVERSATION_POSITIONS = [
    #     (176, 364),
    #     (176, 430),
    #     (176, 501),
    #     (176, 619),
    #     (176, 667),
    #     (176, 748),
    #     (176, 809),
    #     (176, 889),
    #     (176, 969),
    #     (176, 1050),
    # ]
    #
    # global whitelist  # People the bot is able to talk to
    # whitelist = json.load(open("./whitelist.json", "r"))

    bot = ChatGPT()

    # This is a function pyperclip needs to use
    # pyperclip.determine_clipboard()
    #
    # # Focus the left real quick
    # focus_left_window()
    #
    # start_time = time.time()
    #
    # previous_new_conversation_check_time = time.time()

    # try:
    # while True:
    #
    #     conversation_positions = check_to_see_if_new_chats()
    #
    #     # Every 3 minutes refresh the webpage to update to see if we added new people
    #     if time.time() - previous_new_conversation_check_time > 180:
    #         print("Checking for new people...")
    #         refresh_webpage()
    #         time.sleep(15)
    #
    #         # If there are new potential friends then message each of them :)
    #         while start_new_conversations_if_there_is_a_new_person() != 0:
    #             pass
    #         previous_new_conversation_check_time = time.time()
    #
    #     # If there are no new converstaions wait 10 seconds
    #     if len(conversation_positions) == 0:
    #         time.sleep(10)
    #         continue
    #
    #     # Click on the first chat (if someone messaged us then it will be the first chat)
    #     mouse.position = conversation_positions[-1]
    #     time.sleep(1)
    #     mouse.click(pynput.mouse.Button.left, 1)
    #     time.sleep(1)
    #
    #     data = copy_a_chat()
    #
    prompt = 'Your instruction is to continue what the character "ME" would say next in following conversation ME is trying to make friends with the other person. ME is very funny, a good listener, and talks casually. IMPORTANT: Only respond with what ME would say next\n The conversaion is delimited in triple backticks\n ```'

    # # Get the last N words in the conversation (can be changed if using different models for better context)
    # prompt += " ".join(data.split(" ")[-500:])
    # prompt += "```\n"

    # Debug statement to see that the code is working
    print("Asking the following question to ChatGPT:\n", prompt, "\n")
    response = bot.ask(prompt)

    print(
        "Response from ChatGPT\n\n", response, "\n"
    )  # prints the response from chatGPT

    # Clean the response
    #         if "ME" == response.split("\n")[0]:
    #             response = "\n".join(
    #                 response.split("\n")[1:]
    #             )  # removes the first line of the response
    #         elif "ME:" in response.split("\n")[0]:
    #             response = "\n".join(
    #                 response.split("ME:")[1:]
    #             )  # removes the first line of the response
    #
    #         # If the response is valid then send it
    #         if (
    #             response
    #             == "Unusable response produced by ChatGPT, maybe its unavailable."
    #         ):
    #             print("ChatGPT is down")
    #             mouse.position = (176, 364)
    #             time.sleep(0.75)
    #             mouse.click(pynput.mouse.Button.left, 1)
    #             # Wait 3 minutes
    #             time.sleep(180)
    #         else:
    #             # Past the response from chatgpt into the the chat and send it
    #             paste_data(response)
    #
    #             mouse.position = (176, 364)
    #             time.sleep(0.75)
    #             mouse.click(pynput.mouse.Button.left, 1)
    #
    # except KeyboardInterrupt:
    #     del mouse
    #     del keyboard
