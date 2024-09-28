import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

def calculate_difference():
    buy_price = float(buy_price_entry.get())
    qty = int(qty_entry.get())
    sale_price = float(sell_price_entry.get())

    buy_amount = buy_price * qty
    sell_amount = sale_price * qty
    difference = sell_amount - buy_amount
    percent = (difference / buy_amount) * 100

    buy_amount_label.config(text=f"Buy Amount: {buy_amount:,.2f}")
    sell_amount_label.config(text=f"Sell Amount: {sell_amount:,.2f}")
    difference_label.config(text=f"Difference: {difference:,.2f}")
    percent_label.config(text=f"Percent: {percent:.2f}%")

def create_circular_image(image_path, size):
    img = Image.open(image_path).resize(size, Image.Resampling.LANCZOS)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    img.putalpha(mask)
    return img

root = tk.Tk()
root.title("Profit Loss Calculator | by @Arslanr369")
root.geometry("600x400")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14))

logo_size = (110, 110)
logo_img_left = create_circular_image(r"C:\Users\user\Documents\GitHub\python_testing\profit\logo_left.png", logo_size)
logo_img_right = create_circular_image(r"C:\Users\user\Documents\GitHub\python_testing\profit\logo_right.png", logo_size)
logo_photo_left = ImageTk.PhotoImage(logo_img_left)
logo_photo_right = ImageTk.PhotoImage(logo_img_right)

root.iconphoto(False, logo_photo_right)

header_frame = tk.Frame(root)
header_frame.grid(row=0, column=0, columnspan=3, pady=10)

logo_label_left = tk.Label(header_frame, image=logo_photo_left)
logo_label_left.pack(side=tk.LEFT, padx=20)

title_label = tk.Label(header_frame, text="Profit Loss Calculator", font=("Helvetica", 20, "bold"))
title_label.pack(side=tk.LEFT)

logo_label_right = tk.Label(header_frame, image=logo_photo_right)
logo_label_right.pack(side=tk.RIGHT, padx=20)

ttk.Label(root, text="Buy Price", font=("Helvetica", 14)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
buy_price_entry = ttk.Entry(root, font=("Helvetica", 12))
buy_price_entry.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Quantity", font=("Helvetica", 14)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
qty_entry = ttk.Entry(root, font=("Helvetica", 12))
qty_entry.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(root, text="Sell Price", font=("Helvetica", 14)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
sell_price_entry = ttk.Entry(root, font=("Helvetica", 12))
sell_price_entry.grid(column=1, row=3, padx=10, pady=15)

calc_button = ttk.Button(root, text="Calculate", command=calculate_difference, style="TButton")
calc_button.grid(row=4, column=0, columnspan=2, pady=10)

buy_amount_label = ttk.Label(root, text="Buy Amount: ", font=("Helvetica", 14))
buy_amount_label.grid(column=2, row=1, padx=10, pady=5, sticky='w')

sell_amount_label = ttk.Label(root, text="Sell Amount: ", font=("Helvetica", 14))
sell_amount_label.grid(column=2, row=2, padx=10, pady=5, sticky='w')

difference_label = ttk.Label(root, text="Difference: ", font=("Helvetica", 14))
difference_label.grid(column=2, row=3, padx=10, pady=5, sticky='w')

percent_label = ttk.Label(root, text="Percent:", font=("Helvetica", 14))
percent_label.grid(column=2, row=4, padx=10, pady=3, sticky='w')

footer_label = tk.Label(root, text="Thanks for Downloading and Please Share This App.", font=("Helvetica", 12), fg="gray")
footer_label.grid(row=5, column=0, columnspan=3, pady=5)

suggestion_label = tk.Label(root, text="For Suggestions Or To Give a Tip, Connect With Me On Social Media: @Arslanr369", font=("Helvetica", 12), fg="blue")
suggestion_label.grid(row=6, column=0, columnspan=3, pady=5)

root.mainloop()
