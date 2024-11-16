import tkinter as tk
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


        tk.Label(root, text="Game Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Platform").grid(row=1, column=0)
        self.platform_entry = tk.Entry(root)
        self.platform_entry.grid(row=1, column=1)

        tk.Label(root, text="Genre").grid(row=2, column=0)
        self.genre_entry = tk.Entry(root)
        self.genre_entry.grid(row=2, column=1)

        tk.Label(root, text="Status").grid(row=3, column=0)
        self.status_entry = tk.Entry(root)
        self.status_entry.grid(row=3, column=1)

        tk.Label(root, text="Rate").grid(row=4, column=0)
        self.rate_entry = tk.Entry(root)
        self.rate_entry.grid(row=4, column=1)

        tk.Label(root, text="Comment").grid(row=5, column=0)
        self.comment_entry = tk.Entry(root)
        self.comment_entry.grid(row=5, column=1)

        tk.Label(root, text="Played Time").grid(row=6, column=0)
        self.played_time_entry = tk.Entry(root)
        self.played_time_entry.grid(row=6, column=1)


        self.image_button = tk.Button(root, text="Add an image", command=self.select_image)
        self.image_button.grid(row=7, column=1, columnspan=2)

        self.add_game_button = tk.Button(root, text="Add a game", command=self.add_game)
        self.add_game_button.grid(row=8, column=1, columnspan=2)

        # Liste des jeux
        self.game_list = tk.Listbox(root, width=50)
        self.game_list.grid(row=0, column=3, rowspan=8)
        self.game_list.bind('<<ListboxSelect>>', self.display_game_info)

        self.load_game_list()

    def load_game_list(self):
        self.game_list.delete(0, tk.END)
        for game in self.library.games:
            self.game_list.insert(tk.END, game.name)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if self.image_path:
            messagebox.showinfo("Image added", f"Image added : {self.image_path}")

    def add_game(self):
        name = self.name_entry.get()
        platform = self.platform_entry.get()
        genre = self.genre_entry.get()
        status = self.status_entry.get()
        rating = self.rate_entry.get()
        comments = self.comment_entry.get()
        time_played = self.played_time_entry.get()

        if not name or not platform:
            messagebox.showwarning("Erreur", "Le nom et la plateforme sont obligatoires.")
            return
        
        game = Game(name, platform, genre, status, rating, comments, time_played, self.image_path)
        self.library.add_game(game)
        
        self.load_game_list()
        messagebox.showinfo("Succès", f"Le jeu '{name}' a été ajouté !")

    def display_game_info(self, event):
        selected_index = self.game_list.curselection()
        if not selected_index:
            return
        game = self.library.games[selected_index[0]]

        info_window = tk.Toplevel(self.root)
        info_window.title(game.name)
        
        tk.Label(info_window, text=f"Name: {game.name}").pack()
        tk.Label(info_window, text=f"Platform: {game.platform}").pack()
        tk.Label(info_window, text=f"Genre: {game.genre}").pack()
        tk.Label(info_window, text=f"Status: {game.status}").pack()
        tk.Label(info_window, text=f"Rate: {game.rating}").pack()
        tk.Label(info_window, text=f"Comments: {game.comments}").pack()
        tk.Label(info_window, text=f"Played Time: {game.time_played} hours").pack()

        if game.image_path and os.path.exists(game.image_path):
            img = Image.open(game.image_path)
            img = img.resize((150, 150))
            photo = ImageTk.PhotoImage(img)
            tk.Label(info_window, image=photo).pack()
            info_window.image = photo 
        else:
            tk.Label(info_window, text="No image available").pack()


root = tk.Tk()
app = GameApp(root)
root.mainloop()
