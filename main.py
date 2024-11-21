import tkinter as tk
import customtkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from classes.game import Game
from classes.game_library import Game_Library


class GameApp:
    def __init__(self, root):
        self.root = root
        self.library = Game_Library()
        self.root.title("Game App")
        self.image_path = None
        self.current_frame = None

        # Root layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Side menu
        self.side_menu = customtkinter.CTkFrame(root, width=200)
        self.side_menu.grid(row=0, column=0, sticky="ns")
        self.side_menu.grid_rowconfigure(0, weight=1)

        customtkinter.CTkButton(self.side_menu, text="Games", command=self.show_games_page).pack(fill="x", pady=10, padx=5)
        customtkinter.CTkButton(self.side_menu, text="Add New Game", command=self.show_add_game_page).pack(fill="x", pady=10, padx=5)

        # Main area
        self.main_frame = customtkinter.CTkFrame(root)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Initialize with the games page
        self.show_games_page()

    def show_frame(self, frame_class):
        """Switch to a new frame."""
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.main_frame, self)
        self.current_frame.pack(fill="both", expand=True)

    def show_games_page(self):
        """Display the list of games."""
        self.show_frame(GamesPage)

    def show_add_game_page(self):
        """Display the add game page."""
        self.show_frame(AddGamePage)


class GamesPage(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        customtkinter.CTkLabel(self, text="Games Library", font=("Arial", 20)).pack(pady=10)

        self.game_list = tk.Listbox(self, width=50)
        self.game_list.pack(pady=20)
        self.game_list.bind('<<ListboxSelect>>', self.display_game_info)

        self.load_game_list()

    def load_game_list(self):
        self.game_list.delete(0, tk.END)
        for game in self.app.library.games:
            self.game_list.insert(tk.END, game.name)

    def display_game_info(self, event):
        selected_index = self.game_list.curselection()
        if not selected_index:
            return
        game = self.app.library.games[selected_index[0]]

        info_window = tk.Toplevel(self)
        info_window.title(game.name)

        customtkinter.CTkLabel(info_window, text=f"Name: {game.name}",text_color="black").pack()
        customtkinter.CTkLabel(info_window, text=f"Platform: {game.platform}",text_color="black").pack()
        customtkinter.CTkLabel(info_window, text=f"Genre: {game.genre}",text_color="black").pack()
        customtkinter.CTkLabel(info_window, text=f"Status: {game.status}",text_color="black").pack()
        customtkinter.CTkLabel(info_window, text=f"Rate: {game.rating}",text_color="black").pack()
        customtkinter.CTkLabel(info_window, text=f"Comments: {game.comments}",text_color="black").pack()
        customtkinter.CTkLabel(info_window, text=f"Played Time: {game.time_played} hours",text_color="black").pack()

        if game.image_path and os.path.exists(game.image_path):
            img = Image.open(game.image_path)
            img = img.resize((150, 150))
            photo = ImageTk.PhotoImage(img)
            customtkinter.CTkLabel(info_window, image=photo).pack()
            info_window.image = photo
        else:
            customtkinter.CTkLabel(info_window, text="No image available").pack()


class AddGamePage(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.image_path = None

        customtkinter.CTkLabel(self, text="Add New Game", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)

        customtkinter.CTkLabel(self, text="Game Name").grid(row=1, column=0)
        self.name_entry = customtkinter.CTkEntry(self)
        self.name_entry.grid(row=1, column=1)

        customtkinter.CTkLabel(self, text="Platform").grid(row=2, column=0)
        self.platform_entry = customtkinter.CTkEntry(self)
        self.platform_entry.grid(row=2, column=1)

        customtkinter.CTkLabel(self, text="Genre").grid(row=3, column=0)
        self.genre_entry = customtkinter.CTkEntry(self)
        self.genre_entry.grid(row=3, column=1)

        customtkinter.CTkLabel(self, text="Status").grid(row=4, column=0)
        self.status_entry = customtkinter.CTkEntry(self)
        self.status_entry.grid(row=4, column=1)

        customtkinter.CTkLabel(self, text="Rate").grid(row=5, column=0)
        self.rate_entry = customtkinter.CTkEntry(self)
        self.rate_entry.grid(row=5, column=1)

        customtkinter.CTkLabel(self, text="Comment").grid(row=6, column=0)
        self.comment_entry = customtkinter.CTkEntry(self)
        self.comment_entry.grid(row=6, column=1)

        customtkinter.CTkLabel(self, text="Played Time").grid(row=7, column=0)
        self.played_time_entry = customtkinter.CTkEntry(self)
        self.played_time_entry.grid(row=7, column=1)

        self.image_button = customtkinter.CTkButton(self, text="Add an image", command=self.select_image)
        self.image_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.add_game_button = customtkinter.CTkButton(self, text="Add Game", command=self.add_game)
        self.add_game_button.grid(row=9, column=0, columnspan=2, pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if self.image_path:
            messagebox.showinfo("Image added", f"Image added: {self.image_path}")

    def add_game(self):
        name = self.name_entry.get()
        platform = self.platform_entry.get()
        genre = self.genre_entry.get()
        status = self.status_entry.get()
        rating = self.rate_entry.get()
        comments = self.comment_entry.get()
        time_played = self.played_time_entry.get()

        if not name or not platform:
            messagebox.showwarning("Error", "Name and Platform are mandatory.")
            return

        game = Game(name, platform, genre, status, rating, comments, time_played, self.image_path)
        self.app.library.add_game(game)
        self.app.show_games_page()
        messagebox.showinfo("Success", f"The game '{name}' has been added!")


root = customtkinter.CTk()
app = GameApp(root)
root.mainloop()
