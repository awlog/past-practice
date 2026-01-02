import tkinter as tk
from tkinter import ttk

# Initialize the main menu
root = tk.Tk()
root.title("Dashboard")
root.geometry("800x500")
root.configure(bg="#f0f2f5")

# Heading
header = tk.Label(root, text="My Dashboard", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="#333")
header.pack(pady=20)

# Create a frame for the stat card
stats_frame = tk.Frame(root, bg="#f0f2f5")
stats_frame.pack(pady=10)

# Function to create a stat card
def create_card(parent, title, value, bg_color):
    card = tk.Frame(parent, bg=bg_color, width=200, height=100, padx=10, pady=10)
    card.pack_propagate(False)
    card.pack(side="left", padx=15)

    label_title = tk.Label(card, text=title, font=("Arial", 12), bg=bg_color, fg="White")
    label_title.pack(anchor="w")

    label_value = tk.Label(card, text=value, font=("Arial", 20, "bold"), bg=bg_color, fg="white")
    label_value.pack(anchor="w")

# Sample stat cards
create_card(stats_frame, "Users", "1024", "#4CAF50")
create_card(stats_frame, "Sales", "25,000", "#2196F3")
create_card(stats_frame, "Orders", "250", "#FF5722")

# Add some action buttons

btn_frame = tk.Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=30)

tk.Button(btn_frame, text="Refresh", font=("Arial", 12), bg="#007Bff", fg="white", padx=20, pady=5).pack(side="left", padx=10)
tk.Button(btn_frame, text="Add Date", font=("Arial", 12), bg="#28A745", fg="white", padx=20, pady=5).pack(side="left", padx=10)

# Run the appliation

root.mainloop()