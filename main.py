import pyodbc
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("200x300")
app.title("CREATE-CONNECT MS DATABASE")

entry_database = customtkinter.CTkEntry(app, placeholder_text="Database Name")
entry_database.place(relx=0.1, rely=0.1)


def create_db():
    try:
        connection = pyodbc.connect(
            "DRIVER={SQL Server};"
            + "Server=HP\\SQLEXPRESS;"
            + f"Database=master;"
            + "Trusted_Connection=True"
        )
        connection.autocommit = True
        connection.execute(f"create database{entry_database.get()}")
        info_lable.configure(text="Database Created")

    except pyodbc.Error as ex:
        print("Connection failed", ex)
        info_lable.configure(text="Database Creating Failed")


create_button = customtkinter.CTkButton(
    app, text="Create", command=create_db, fg_color="green"
)
create_button.place(relx=0.1, rely=0.2)


def connect_db():
    try:
        connection = pyodbc.connect(
            "DRIVER={SQL Server};"
            + "Server=HP\\SQLEXPRESS;"
            + f"Database={entry_database.get()};"
            + "Trusted_Connection=True"
        )
        info_lable.configure(text="Connection Successful")
        # connection.autocommit = True
        # connection.execute(f"Create database {database_name} ")

    except pyodbc.Error as ex:
        print("Connection failed", ex)
        info_lable.configure(text="Connection Failed")


connect_button = customtkinter.CTkButton(
    app, text="Connect", command=connect_db, fg_color="blue"
)
connect_button.place(relx=0.1, rely=0.3)
info_lable = customtkinter.CTkLabel(app, text="Data_db")
info_lable.place(relx=0.1, rely=0.4)
app.mainloop()


"""try:
    database_name = input("Enter a database name to create:")

    connection = pyodbc.connect(
        "DRIVER={SQL Server};"
        + "Server=HP\\SQLEXPRESS;"
        + "Database=master;"
        + "Trusted_Connection=True"
    )

    connection.autocommit = True
    connection.execute(f"Create database {database_name} ")
    print("Database Created")

except pyodbc.Error as ex:
    print("Connection failed", ex)"""
