# import time

# kettle = [
#     "Water",
#     "Milk",
#     "Tea Leaves",
#     "Sugar",
#     "Ginger"
# ]

# print(">>> Hey Dear, wait... tea is boiling")
# time.sleep(0.5)


# for kettle in range(5, 0, -1):
#     print(f"⏳ Boiling...{kettle}")
#     time.sleep(1)

# print("\n☕✨ Chai Ready Hai!")

# import time
# import tkinter as tk
# from threading import Thread

# # 👇 Ingredients code ke andar
# ingredients = [
#     "Water 💧",
#     "Milk 🥛",
#     "Tea Leaves 🍃",
#     "Sugar 🍬",
#     "Ginger 🫚"
# ]

# def make_tea():
#     output("Hey Dear, wait... tea is boiling 🔥\n")
#     time.sleep(1)

#     for c in range(5, 0, -1):
#         output(f"⏳ Boiling... {c}\n")
#         time.sleep(1)

#     # ingredients use (hidden)
#     for _ in ingredients:
#         time.sleep(0.2)

#     output("\n☕✨ Chai Ready Hai!")

# def output(text):
#     text_box.insert(tk.END, text)
#     text_box.see(tk.END)

# root = tk.Tk()
# root.title("Python Tea Maker ☕")
# root.geometry("420x300")

# text_box = tk.Text(root, font=("Menlo", 13))  # Menlo = mac terminal font
# text_box.pack(expand=True, fill="both")

# Thread(target=make_tea).start()
# root.mainloop()

