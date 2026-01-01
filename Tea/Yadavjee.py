import time
import os

width = 31
height = 9

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    for heart_col in range(4, width - 4):
        clear()

        # Top border
        print("┌" + "─" * width + "┐")

        # Title
        title = "Y A D A V 😎"
        pad = (width - len(title)) // 2
        print("│" + " " * pad + title + " " * (width - len(title) - pad) + "│")

        # Jail area
        for row in range(height):
            line = ""
            for col in range(width):
                if col % 3 == 0:
                    line += "|"
                else:
                    line += " "

            # Place heart in middle row
            if row == height // 2:
                line = line[:heart_col] + "❤️" + line[heart_col + 1:]

            print("│" + line[:width] + "│")

        # Bottom border
        print("└" + "─" * width + "┘")

        time.sleep(0.08)