import tkinter as tk
from tkinter import ttk, messagebox

products = {
    "laptop": {
        "name": "ProBook 15",
        "price": 899.99,
        "category": "electronics",
        "in_stock": True,
        "specs": {"ram_gb": 16, "storage_gb": 512, "cpu": "i7"}
    },
    "mouse": {
        "name": "ErgoClick Wireless",
        "price": 29.99,
        "category": "accessories",
        "in_stock": True,
        "specs": {"dpi": 1600, "wireless": True}
    },
    "keyboard": {
        "name": "MechType RGB",
        "price": 79.50,
        "category": "accessories",
        "in_stock": False,
        "specs": {"switch_type": "blue", "backlit": True}
    },
    "monitor": {
        "name": "ViewMax 27",
        "price": 249.00,
        "category": "electronics",
        "in_stock": True,
        "specs": {"size_inch": 27, "resolution": "1440p", "refresh_hz": 144}
    },
    "headphones": {
        "name": "SoundPro ANC",
        "price": 129.99,
        "category": "audio",
        "in_stock": True,
        "specs": {"anc": True, "wireless": True, "battery_h": 30}
    }
}

def on_buy():
    choice = combo.get().strip().lower()
    if not choice:
        messagebox.showwarning("No selection", "Please select a product.")
        return
    if choice not in products:
        messagebox.showerror("Invalid", "Invalid product name.")
        return

    product = products[choice]
    if not product["in_stock"]:
        messagebox.showinfo("Out of stock", f"{product['name']} is currently out of stock.")
        return

    info = (
        f"Product: {product['name']}\n"
        f"Price: ${product['price']:.2f}\n"
        f"Category: {product['category']}\n"
        f"Specs: {product['specs']}"
    )
    messagebox.showinfo("Selected Product", info)

root = tk.Tk()
root.title("Tech Store")
root.geometry("420x280")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="🛒 Tech Store",
    font=("Segoe UI", 18, "bold"),
    bg="#0f172a",
    fg="#e2e8f0"
)
title.pack(pady=(20, 10))

subtitle = tk.Label(
    root,
    text="Choose a product to buy",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#94a3b8"
)
subtitle.pack(pady=(0, 15))

combo = ttk.Combobox(
    root,
    values=[p["name"] for p in products.values()],
    state="readonly",
    font=("Segoe UI", 11)
)
combo.pack(pady=5)
combo.current(0)

buy_btn = tk.Button(
    root,
    text="Buy Now",
    command=on_buy,
    bg="#3b82f6",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=20,
    pady=6
)
buy_btn.pack(pady=15)

# Map displayed name back to key
def get_key_by_name(name):
    for k, v in products.items():
        if v["name"] == name:
            return k
    return None

def on_buy_wrapped():
    name = combo.get()
    key = get_key_by_name(name)
    if key is None:
        messagebox.showerror("Error", "Product not found.")
        return
    choice = key
    product = products[choice]
    if not product["in_stock"]:
        messagebox.showinfo("Out of stock", f"{product['name']} is currently out of stock.")
        return
    info = (
        f"Product: {product['name']}\n"
        f"Price: ${product['price']:.2f}\n"
        f"Category: {product['category']}\n"
        f"Specs: {product['specs']}"
    )
    messagebox.showinfo("Selected Product", info)

buy_btn.config(command=on_buy_wrapped)

root.mainloop()


