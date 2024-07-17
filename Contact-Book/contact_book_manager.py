import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass@123",
    database="codesoft"
)
cursor = conn.cursor()


def add_contact():
    name = name_var.get()
    mobile = mobile_var.get()
    email = email_var.get()
    address = address_var.get()

    if name == "" or mobile == "" or email == "" or address == "":
        messagebox.showerror("Input Error", "All fields are required")
        return

    cursor.execute("INSERT INTO contacts (name, mobile, email, address) VALUES (%s, %s, %s, %s)",
                   (name, mobile, email, address))
    conn.commit()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully")
    view_contacts()


def view_contacts():
    for row in contacts_list.get_children():
        contacts_list.delete(row)

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    for row in rows:
        contacts_list.insert("", tk.END, values=row)


def search_contact():
    search_by = search_by_var.get()
    search_value = search_value_var.get()
    query = f"SELECT * FROM contacts WHERE {search_by} LIKE %s"
    cursor.execute(query, ('%' + search_value + '%',))
    rows = cursor.fetchall()

    for row in contacts_list.get_children():
        contacts_list.delete(row)

    for row in rows:
        contacts_list.insert("", tk.END, values=row)


def update_contact():
    selected_item = contacts_list.selection()
    if not selected_item:
        messagebox.showerror("Selection Error", "Select a contact to update")
        return

    contact_id = contacts_list.item(selected_item[0], "values")[0]

    name = name_var.get()
    mobile = mobile_var.get()
    email = email_var.get()
    address = address_var.get()

    cursor.execute("UPDATE contacts SET name=%s, mobile=%s, email=%s, address=%s WHERE id=%s",
                   (name, mobile, email, address, contact_id))
    conn.commit()
    clear_fields()
    messagebox.showinfo("Success", "Contact updated successfully")
    view_contacts()


def delete_contact():
    selected_item = contacts_list.selection()
    if not selected_item:
        messagebox.showerror("Selection Error", "Select a contact to delete")
        return

    contact_id = contacts_list.item(selected_item[0], "values")[0]
    cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
    conn.commit()
    contacts_list.delete(selected_item[0])
    messagebox.showinfo("Success", "Contact deleted successfully")


def clear_fields():
    name_var.set("")
    mobile_var.set("")
    email_var.set("")
    address_var.set("")


root = tk.Tk()
root.title("Contact Book")
root.configure(background="#a765a7")
root.title("ContactBook")
root.iconbitmap("icon.ico")
name_var = tk.StringVar()
mobile_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()

lbl_title = tk.Label(root, text="CONTACT BOOK APPLICATION", font="Poppins 15 bold", background="#a765a7")
lbl_title.grid(row=0, column=0, columnspan=5)

lbl_name = tk.Label(root, text="Name-", background="#a765a7")
lbl_name.grid(row=1, column=0)
name_ent = tk.Entry(root, textvariable=name_var)
name_ent.grid(row=1, column=1)

lbl_mob = tk.Label(root, text="MobileNo.-", background="#a765a7")
lbl_mob.grid(row=2, column=0)
mobile_ent = tk.Entry(root, textvariable=mobile_var)
mobile_ent.grid(row=2, column=1)

lbl_add = tk.Label(root, text="Address-", background="#a765a7")
lbl_add.grid(row=3, column=0)
address_ent = tk.Entry(root, textvariable=address_var)
address_ent.grid(row=3, column=1)

lbl_email = tk.Label(root, text="Email-", background="#a765a7")
lbl_email.grid(row=4, column=0)
email_ent = tk.Entry(root, textvariable=email_var)
email_ent.grid(row=4, column=1)

btn_add = tk.Button(root, text="ADD", command=add_contact, background="#f0e98a")
btn_add.grid(row=1, column=2, pady=10)

btn_update = tk.Button(root, text="UPDATE", command=update_contact, background="#f0e98a")
btn_update.grid(row=1, column=3, pady=10)

btn_delete = tk.Button(root, text="DELETE", command=delete_contact, background="#f0e98a")
btn_delete.grid(row=2, column=2, pady=10)

btn_clear = tk.Button(root, text="CLEAR", command=clear_fields, background="#f0e98a")
btn_clear.grid(row=2, column=3, pady=10)

lbl_search = tk.Label(root, text="SEARCH BY-", background="#a765a7")
lbl_search.grid(row=3, column=2, columnspan=2)
search_by_var = tk.StringVar(value="name")
search_value_var = tk.StringVar()

tk.OptionMenu(root, search_by_var, "name", "mobile", "email", "address").grid(row=4, column=2, columnspan=2, pady=10)
search_ent = tk.Entry(root, textvariable=search_value_var)
search_ent.grid(row=5, column=2, columnspan=2)

btn_search = tk.Button(root, text="SEARCH", command=search_contact, background="#f0e98a")
btn_search.grid(row=6, column=2, columnspan=2, pady=10)

contacts_list = ttk.Treeview(root, columns=("id", "name", "mobile", "email", "address"), show="headings",
                             yscrollcommand="TRUE")
contacts_list.heading("id", text="ID")
contacts_list.heading("name", text="Name")
contacts_list.heading("mobile", text="Mobile")
contacts_list.heading("email", text="Email")
contacts_list.heading("address", text="Address")
contacts_list.grid(row=8, column=0, columnspan=5)

view_contacts()
root.mainloop()
conn.close()
