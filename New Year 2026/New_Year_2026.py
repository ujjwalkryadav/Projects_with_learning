import sys
import time
import random
import os
import subprocess
import shutil

# ============ COLORS ============
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
COLORS = [
    "\033[31m", "\033[32m", "\033[33m",
    "\033[34m", "\033[35m", "\033[36m"
]

# ============ BASIC ============
def clear():
    os.system("clear")

def sound(file="Ping.aiff", times=1, delay=0.03):
    for _ in range(times):
        subprocess.Popen(
            ["afplay", f"/System/Library/Sounds/{file}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(delay)

def typing(text, delay=0.04, color=""):
    for c in text:
        sys.stdout.write(color + c + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ============ 2025 FLOOD (RED) ============
def flood_2025(lines=20):
    clear()
    for _ in range(lines):
        print(RED + ("2025 " * random.randint(8, 14)) + RESET)
        sound()
        time.sleep(0.05)

# ============ SERVER OVERLOADED (SCROLL + FLIP) ============
def server_overloaded_scroll(duration=4):
    clear()
    width = shutil.get_terminal_size().columns
    height = shutil.get_terminal_size().lines

    texts = ["SERVER OVERLOADED", "OVERLOADED SERVER"]
    buffer = []
    start = time.time()
    i = 0

    sound("Basso.aiff", 6)

    while time.time() - start < duration:
        text = texts[i % 2]
        i += 1
        line = (text + " ") * (width // (len(text) + 1))
        buffer.append(line[:width])

        if len(buffer) > height:
            buffer.pop(0)

        clear()
        for l in buffer:
            print(GREEN + l + RESET)

        time.sleep(0.07)

# ============ DELETE & RESET ============
def delete_and_reset():
    clear()
    typing("Deleting old problems", 0.05)

    # FUNNY + ERROR FAIL SOUND
    sound("Sosumi.aiff", 2, 0.05)
    sound("Funk.aiff", 1, 0.05)
    sound("Ping.aiff", 1, 0.05)
    typing("❌ Failed... Problems are permanent 😂", 0.05)

    reset_lines = [
        "Delete Negative People ✔",
        "Forget Your Past ✔",
        "Accept Your Mistakes ✔",
        "Restart Your Life ✔"
    ]

    for line in reset_lines:
        typing(line, 0.06)
        sound()
        time.sleep(0.5)

    typing("\nDeleting 2025...", 0.05)
    sound("Basso.aiff", 4)
    time.sleep(1)

    typing("New Year Loading...", 0.05)
    sound("Ping.aiff", 3)
    time.sleep(1)

# ============ REAL TIME SWITCH ============
def real_time_switch():
    for sec in [55, 56, 57, 58, 59]:
        clear()
        print(f"2025 31 December 23 Hours 59 min {sec} sec")
        sound()
        time.sleep(1)

    clear()
    sound("Glass.aiff", 5)
    print("2026 1 January")
    typing("Loading Successfully ✔", 0.06)
    time.sleep(1)

# ============ ENDLESS CELEBRATION ============
def full_screen_wish():
    width = shutil.get_terminal_size().columns
    height = shutil.get_terminal_size().lines
    message = "HAPPY NEW YEAR 2026"
    emojis = ["🎉", "🎆", "🔥", "✨", "🥳"]

    while True:
        clear()
        color = random.choice(COLORS)
        emoji = random.choice(emojis)
        offset = random.randint(0, 10)

        for _ in range(height):
            line = (message + " " + emoji + " ") * (width // (len(message) + 3))
            print(color + (" " * offset) + line[:width] + RESET)

        time.sleep(0.15)

# ============ MAIN ============
clear()
time.sleep(0.5)

flood_2025()                 # RED flood
server_overloaded_scroll()   # GREEN scroll + flip
delete_and_reset()
real_time_switch()
full_screen_wish()           # ENDLESS celebration
