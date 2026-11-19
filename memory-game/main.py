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
        # method call to create elements
        self.create_elements()
    # method to create game elements    
    def create_elements(self):
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

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()