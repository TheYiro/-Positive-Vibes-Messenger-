# 🌟Positive Vibes Messenger

This project uses Python and PyAutoGUI to automate sending messages to a selected text box.

## 📋 Project Description

"Positive Vibes Messenger" sends positive messages and random affirmations to any text box at regular time intervals. With a list of carefully selected messages, this tool is designed to controllably spam a text box.

## 🚀 Features

- Automatic sending of positive messages. 🌈
- List of random affirmation messages. 🌟
- Customizable time interval between messages. ⏳

## 🛠️ Instructions for Use

1. **Installation of Dependencies**:
 - Make sure you have Python and the necessary libraries installed:
 ```bash
 pip install pyautogui
 ```

2. **Initial Configuration**:
 - Run the script and select the text box where you want to send the messages in the next 5 seconds.

3. **Program Execution**:
 - The program will send a random message every 3 seconds. You can modify the time interval by changing the value in `time.sleep(3)`.

## 📜 Example Code

```python
import pyautogui
import time
import random

# Random message list
messages = [
 "I am open to receive all the good that the universe has to offer me.",
 "Today is a perfect day to manifest your biggest dreams. 🌟✨",
 "Every positive thought brings you closer to what you want. 💭💖",
 "The chain of positive events begins with your attitude. 🔗😊",
 # (list of messages continues)
]

def send_random_message():
 message = random.choice(messages)
 pyautogui.write(message)
 pyautogui.press('enter')

print("You have 5 seconds to select the text box...")
time.sleep(5)

while True:
 send_random_message()
 time.sleep(3)
```

---

<h3 align="center"><i>By Joaco ✨</i></h3>
