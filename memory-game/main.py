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
        self.custom_font = ("Arial", 16, "bold")
        # color dictionary
        self.colors = {
            "bg": "#1a1a2e",
            "sidebar_bg": "#16213e",
            "card_bg": "#0f3469",
            "card_fg": "#e94560",
            "text": "#ffffff",
            "btn_bg": "#4caf50",
            "btn_fg": "#ffffff",
            "combox_bg": "#32374b",
            "combox_fg": "#ffffff",
            "gameover_bg": "#0f3460"
        }
        # game difficulty levels
        # grid sizes with symbols
        self.difficulty_levels = {
            "Easy": {
                "grid": (4, 4), "symbols": ["●", "✦", "✿", "★", "🍽", "◼", "▲", "𖦹"]
            },
            "Medium": {
                "grid": (4, 5), 
                "symbols": ["●", "✦", "✿", "★", "🍽", "◼", "▲", "𖦹", "⬟", "☀︎"]
            },
            "Hard": {
                "grid": (5, 6),"symbols": ["●", "✦", "✿", "★", "🍽", "◼", "▲", "𖦹", "⬟", "☀︎", "☕︎", "♛", "☮︎", "🏠︎", "✈︎",
                ],
            },
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
        self.cards_frame = None
        self.createMainElements()
        self.createGameGrid()
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
        title_label = tk.Label(self.sidebar, text="Memory Game", font=("Arial", 24, "bold"), bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        title_label.pack(pady=(30, 10))
        subtitle_label = tk.Label(self.sidebar, text="Test Your Memory", font=("Arial", 16, "bold"), bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        subtitle_label.pack(pady=(0, 30))
        difficulty_label = tk.Label(self.sidebar, text="Difficulty: ", font=self.custom_font, bg=self.colors["sidebar_bg"], fg=self.colors["text"])
        difficulty_label.pack(pady=(0, 5))
        # combo box style
        self.style = ttk.Style()
        # combo box custom theme
        self.style.theme_create("modern", parent="alt", settings = {
            "TCombobox": {
                "configure": {
                    "selectbackground": self.colors["combox_bg"],
                    "fieldbackground": self.colors["combox_bg"],
                    "background": self.colors["btn_bg"],
                    "foreground": self.colors["combox_fg"]
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
        self.newgame_btn = tk.Button(self.sidebar, text="New Game", font=self.custom_font, bg=self.colors["btn_bg"], fg=self.colors["btn_fg"], relief=tk.FLAT, command=self.newGame)
        self.newgame_btn.pack(pady=30)
        # button effects
        self.newgame_btn.bind("<Enter>", lambda e: e.widget.config(bg="red"))
        self.newgame_btn.bind("<Leave>", lambda e: e.widget.config(bg=self.colors["btn_bg"]))
    # method to create grid to hold and play with cards     
    def createGameGrid(self):
        # frame to hold cards
        self.cards_frame = tk.Frame(self.game_frame, bg=self.colors["bg"])
        self.cards_frame.pack(expand=True)
        # store cards
        self.cards = []
        # diffuclty level dimension
        rows, cols = self.difficulty_levels[self.current_difficulty]["grid"]
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
                card = tk.Canvas(self.cards_frame, width=80, height=100, bg=self.colors["card_bg"], highlightthickness=0)
                # place card i grid
                card.grid(row=i, column=j, padx=6, pady=0)
                # add click event to card
                card.bind("<Button-1>", lambda e, idx=card_index: self.onCardClick(idx))
                # visible part of card (back)
                card.create_rectangle(5, 5, 75, 95, fill=self.colors["card_bg"], outline=self.colors["card_fg"], width=2)
                card.create_text(40, 50, text="?", font=("Arial", 24, "bold"), fill=self.colors["card_fg"])
                # hidden card front
                # set state to hidden so it can be referenced and changed later
                card.create_rectangle(5, 5, 75, 95, fill=self.colors["card_fg"], outline=self.colors["card_bg"], width=2, state="hidden", tags=("front",))
                # card symbol also hidden for later reference
                card.create_text(40, 50, text=self.symbols[card_index], font=("Arial", 24, "bold"), fill=self.colors["card_bg"], state="hidden", tags=("symbol",))
                # add card to list
                self.cards.append(card)
    # method for when card is clicked
    def onCardClick(self, idx):
        # first click to start game
        if self.start_time is None:
            self.start_time = time.time()
            self.updateTime()
        # ignore invalid clicks after game completed
        if idx in self.revealed or idx in self.match_cards or len(self.revealed) == 2:
            # skip
            return
        # reveal clicked card
        self.revealCard(idx)
        # append card to revealed card list
        self.revealed.append(idx)
        # check when two cards clicked
        if len(self.revealed) == 2:
            # incremenet move counter and update label
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            self.master.after(500, self.checkMatch)
    # method to reveal card
    def revealCard(self, idx):
        # get card index 
        card = self.cards[idx]
        # show front and the symbol
        card.itemconfig("front", state="normal")
        card.itemconfig("symbol", state="normal")
    # method to hide card
    def hideCard(self, idx):
        card = self.cards[idx]
        # hide front and the symbol
        card.itemconfig("front", state="hidden")
        card.itemconfig("symbol", state="hidden")
    # method to start a new game
    def newGame(self):
        # reset all game variables
        self.game_solved = False
        self.revealed.clear()
        self.match_cards.clear()
        self.moves = 0
        self.start_time = None
        # reset game labels
        self.moves_label.config(text="Moves: 0")
        self.time_label.config(text="Time: 0:00")
        # reset game grid
        self.match_pairs = 0
        if self.cards_frame is not None:
            self.cards_frame.destroy()
        self.createGameGrid()
    # method to change game difficulty level
    def changeDifficulty(self, event):
        new_difficulty = self.difficulty_combox.get()
        # check difficulty changed
        if new_difficulty != self.current_difficulty:
            # new game with new difficulty
            self.current_difficulty = new_difficulty
            self.newGame()
    # metod to check for card match
    def checkMatch(self):
        # index of revelaed cards
        idx1, idx2 = self.revealed
        # check whether symbols match 
        if self.symbols[idx1] == self.symbols[idx2]:
            # increment match counter
            self.match_pairs += 1
            # add cards to match list
            self.match_cards.extend([idx1, idx2])
            # highlight matching cards
            for idx in [idx1, idx2]:
                card = self.cards[idx]
                # color when cards match
                card.itemconfig("front", fill="#8bc34a")
            # check whether game over
            # all pairs have been found
            if self.match_pairs == len(self.symbols) // 2:
                self.master.after(500, self.gameOver)
        # not matching
        else:
            # flip to hide both cards
            self.hideCard(idx1)
            self.hideCard(idx2)
        self.revealed.clear()
    # method to update game time
    def updateTime(self):
        # game is active
        if self.start_time and not self.game_solved:
            # elapsed seconds calculation
            time_elapsed = int(time.time() - self.start_time)
            mins, secs = divmod(time_elapsed, 60)
            # update time label
            self.time_label.config(text=f"Time: {mins}:{secs:02d}")
            # update time every second
            self.master.after(1000, self.updateTime)
    # method when game is over
    def gameOver(self):
        self.game_solved = True
        time_elapsed = int(time.time() - self.start_time)
        minutes, seconds = divmod(time_elapsed, 60)
        # game over window
        game_over_window = tk.Toplevel(self.master)
        game_over_window.title("Game Over")
        game_over_window.geometry("350x350")
        game_over_window.configure(bg=self.colors["gameover_bg"])
        game_over_window.grab_set()
        game_over_window.transient(self.master)
        # place window on center
        self.master.update_idletasks()
        x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (350 // 2)
        y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (350 // 2)
        game_over_window.geometry(f"+{x}+{y}")
        # game labels
        tk.Label(game_over_window, text="Congratulations!!", font=("Arial", 28 ,"bold"), bg=self.colors["gameover_bg"], fg=self.colors["text"]).pack(pady=(20, 30))
        # game stats frame
        stat_frame = tk.Frame(game_over_window, bg=self.colors["gameover_bg"])
        stat_frame.pack(pady=(0, 30))
        # display game stats
        self.createStatLabels(stat_frame, "Difficulty", self.current_difficulty)
        self.createStatLabels(stat_frame, "Moves", str(self.moves))
        self.createStatLabels(stat_frame, "Time", f"{minutes}:{seconds:02d}")
        # button to play game again
        play_again_btn = tk.Button(game_over_window, text="Play Again", font=self.custom_font, bg=self.colors["btn_bg"], fg=self.colors["btn_fg"], relief=tk.FLAT, command=lambda : [game_over_window.destroy(), self.newGame()])
        play_again_btn.pack(pady=20)
        # color change on hover
        play_again_btn.bind("<Enter>", lambda e: e.widget.config(bg="red"))
        play_again_btn.bind("<Leave>", lambda e: e.widget.config(bg=self.colors["btn_bg"]))
    # method to create label for stats    
    def createStatLabels(self, parent, label, value):
        frame = tk.Frame(parent, bg=self.colors["gameover_bg"])
        frame.pack(fill=tk.X, pady=5)
        tk.Label(frame, text=f"{label}", font=("Arial", 14), bg=self.colors["gameover_bg"], fg=self.colors["text"]).pack(side=tk.LEFT)
        tk.Label(frame, text=value, font=("Arial", 14, "bold"), bg=self.colors["gameover_bg"], fg=self.colors["card_fg"]).pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
    