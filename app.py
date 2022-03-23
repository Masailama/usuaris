import tkinter as tk
from users import Users


if __name__ == "__main__":
    app = tk.Tk()
    users = Users(app)
    app.mainloop()