import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def fetch_customers():
    response = requests.get(BASE_URL + "customers/")
    if response.status_code == 200:
        customers = response.json()
        customer_list.delete(0, tk.END)
        for customer in customers:
            customer_list.insert(tk.END, f"{customer['first_name']} {customer['last_name']}")
    else:
        messagebox.showerror("Error", "Failed to fetch customers")

def add_customer():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone_number = phone_number_entry.get()
    address = address_entry.get("1.0", tk.END)

    data = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "address": address.strip(),
    }

    response = requests.post(BASE_URL + "customers/", json=data)
    if response.status_code == 201:
        messagebox.showinfo("Success", "Customer added successfully")
        fetch_customers()
    else:
        messagebox.showerror("Error", "Failed to add customer")

# Tkinter GUI setup
root = tk.Tk()
root.title("Mental Health Records")

# Input fields
tk.Label(root, text="First Name").grid(row=0, column=0)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

tk.Label(root, text="Last Name").grid(row=1, column=0)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

tk.Label(root, text="Phone Number").grid(row=2, column=0)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Text(root, height=4, width=30)
address_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Customer", command=add_customer).grid(row=4, column=0, pady=10)
tk.Button(root, text="Fetch Customers", command=fetch_customers).grid(row=4, column=1, pady=10)

# Customer list
customer_list = tk.Listbox(root, width=50)
customer_list.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()