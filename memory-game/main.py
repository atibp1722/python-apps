import tkinter as tk
from tkinter import ttk
import random
import time

class MemoryGame:
    def __init__(self, master):
        # game window
        self.master = master
        self.master.title("Memory Game")
        self.master.geometry("800x600")
        self.master.configure(bg="#1a1a2e")
        self.custom_font("Arial", 16, "Bold")
        # color dictionary
        self.colors = {
            "bg": "#1a1a2e",
            "sidebar_bg": "#16213e",
            "card_bg": "#0f3469",
            "card_fg": "#e94560",
            "text": "#ffffff",
            "btn_bg": "#4caf50",
            "btn_fg": "ffffff",
            "combox_bg": "#32374b",
            "combox_fg": "#ffffff",
            "gameover_bg": "#0f3460"
        }
        # game difficulty levels
        # grid sizes with symbols
        self.difficulty_levels = {
            "Easy": {
                "grid": (4, 4), "symbols": ["●", "✦", "✿", "★", "❤︎", "◼", "▲", "𖦹"]
            }
            "Medium": {
                "grid": (4, 5), "symbols": ["●", "✦", "✿", "★", "❤︎", "◼", "▲", "𖦹", "⬟", "☀︎"]
            }
            "Hard": {
            "grid": (5, 6), "symbols": ["●", "✦", "✿", "★", "❤︎", "◼", "▲", "𖦹", "⬟", "☀︎", "☕︎", "♛", "☮︎", "🏠︎", "✈︎"]
            }
        }
        # intial game state varaibles
        self.current_difficulty = "Easy"
        self.revealed = []
        self.match_pairs = 0
        self.match_cards = []
        self.moves = 0
        self.start_time = None
        self.game_solved = False
        # method call to create game main elements
        self.createMainElements()
    # method to create game elements    
    def createMainElements(self):
        # game frame window
        self.main_frame = tk.Frame(self.master, bg=self.colors["bg"])
        # frame occupies entire window
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        # sidebar for game controls
        self.sidebar = tk.Frame(self.main_frame, bg=self.colors["sidebar_bg"], width=250)
        # vertically left position on game window
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        # actual game cards
        self.game_frame = tk.Frame(self.main_frame, bg=self.colors["bg"])
        # game card frame position
        self.game_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        # method call to add elements to sidebar
        self.createSidebar()
    def createSidebar(self):
        # create title label
        title_label = tk.Label(self.sidebar, text="Memory Game", font=("Arial", 24, "Bold"), bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        title_label.pack(pady=(30, 10))
        subtitle_label = tk.Label(self.sidebar, text="Test Your Memory", font=("Arial", 16, "Regular"), bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        subtitle_label.pack(pady=(0, 30))
        difficulty_label = tk.Label(self.sidebar, text="Difficulty: ", font=self.custom_font, bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        difficulty_label.pack(pady=(0, 5))
        # combo box style
        self.style = ttk.Style()
        # combo box custom theme
        self.style.theme_create("modern", parent="alt", settings = {
            "ICombobox": {
                "configure": {
                    "selectbackground": self.colors["combox_bg"],
                    "fieldbackground": self.colors["combox_bg"],
                    "background": self.colors["btn_bg"],
                    "forekground": self.colors["btn_fg"]
                }
            }
        })
        # apply theme
        self.style.theme_use("modern")
        # difficulty combo box
        self.difficulty_combox = ttk.Combobox(self.sidebar, values=list(self.difficulty_levels.keys()), state="readonly", font=self.custom_font, width=10)
        self.difficulty_combox.set(self.current_difficulty)
        self.difficulty_combox.pack(pady=(0, 20))
        self.difficulty_combox.bind("<<ComboboxSelected>>", self.changeDifficulty)
        # game satistics
        self.moves_label = tk.Label(self.sidebar, text="Moves: 0", font=self.custom_font, bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        self.moves_label.pack(pady=10)
        self.time_label = tk.Label(self.sidebar, text="Time: 0:00", font=self.custom_font, bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        self.time_label.pack(pady=10)
        # new game button
        self.newgame_btn = tk.Label(self.sidebar, text="New Game", font=self.custom_font, bg=self.colors["btn_bg"], fg=self.colors["btn_fg"], relief=tk.FLAT, command=self.newGame)
        self.newgame_btn.pack(pady=30)
        # button effects
        self.newgame_btn.bind("<Enter>", lambda e: e.widget.config("red"))
        self.newgame_btn.bind("<Leave>", lambda e: e.widget.config(bg=self.colors["btn_bg"]))
    # method to create grid to hold and play with cards     
    def createGameGrid(self):
        # frame to hold cards
        self.cards_frame = tk.Frame(self.game_frame, bg=self.colors["bg"])
        self.cards_frame.pack(expand=True)
        # store cards
        self.cards = []
        # diffuclty level dimension
        row, cols = self.difficulty_levels[self.current_difficulty]["grid"]
        # double symbols to generate pairs
        symbols = self.difficulty_levels[self.current_difficulty]["symbols"] * 2
        random.shuffle(symbols)
        self.symbols = symbols
        # create grid of cards
        for i in range(rows):
            for j in range(cols):
                # index from row and column
                card_index = i * cols + j
                # create individual card
                card = tk.canvas(self.cards_frame, width=80, height=100, bg=self.colors["card_bg"], highlightthickness=0)
                # place card i grid
                card.grid(row=i, column=j, padx=6, pady=0)
                # add click event to card
                card.bind("<Button-1>", lambda e, idx=card_index, self.onCardClick(idx))
                # visible part of card (back)
                card.create_rectangle(5, 5, 75, 95, fill=self.colors["card_bg"], outline=self.colors["card_fg"], width=2)
                card.create_text(40, 50, text="?", font=("Arial", 24, "Bold"), fill=self.colors["card_fg"])
                # hidden card front
                # set state to hidden so it can be referenced and changed later
                card.create_rectangle(5, 5, 75, 95, fill=self.colors["card_fg"], outline=self.colors["card_bg"], width=2, state="hidden", tags=("front",))
                # card symbol also hidden for later reference
                card.create_text(40, 50, text=self.symbols[card_index], font=("Arial", 24, "Bold"), fill=self.colors["card_bg"], state="hidden", tags=("symbol",))
                # add card to list
                self.cards.append(card)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()