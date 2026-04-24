import tkinter as tk
from tkinter import messagebox

# Story Data
story = {
    "start": {
        "text": "You wake up in a dark forest. Two paths lie ahead.",
        "choices": {
            "Go Left": "wolf",
            "Go Right": "river"
        }
    },
    "wolf": {
        "text": "You encounter a wild wolf!",
        "choices": {
            "Fight": "lose",
            "Run": "start"
        }
    },
    "river": {
        "text": "You arrive at a river. A boat is nearby.",
        "choices": {
            "Take Boat": "win",
            "Swim": "lose"
        }
    },
    "win": {
        "text": "You escaped safely. You Win!",
        "choices": {}
    },
    "lose": {
        "text": "You lost. Game Over.",
        "choices": {}
    }
}


class StoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Story Game")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        self.current_scene = "start"

        self.title_label = tk.Label(
            root,
            text="AI Story Adventure",
            font=("Arial", 24, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.title_label.pack(pady=20)

        self.story_text = tk.Label(
            root,
            text="",
            wraplength=600,
            justify="center",
            font=("Arial", 16),
            bg="#1e1e1e",
            fg="#dcdcdc"
        )
        self.story_text.pack(pady=30)

        self.button_frame = tk.Frame(root, bg="#1e1e1e")
        self.button_frame.pack(pady=20)

        self.restart_button = tk.Button(
            root,
            text="Restart Game",
            command=self.restart_game,
            bg="#4caf50",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5
        )

        self.load_scene()

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def load_scene(self):
        self.clear_buttons()

        scene = story[self.current_scene]
        self.story_text.config(text=scene["text"])

        if not scene["choices"]:
            self.restart_button.pack(pady=20)
            return

        self.restart_button.pack_forget()

        for choice_text, next_scene in scene["choices"].items():
            button = tk.Button(
                self.button_frame,
                text=choice_text,
                command=lambda ns=next_scene: self.make_choice(ns),
                bg="#333",
                fg="white",
                font=("Arial", 14),
                width=20,
                pady=8
            )
            button.pack(pady=8)

    def make_choice(self, next_scene):
        self.current_scene = next_scene
        self.load_scene()

    def restart_game(self):
        self.current_scene = "start"
        self.load_scene()


if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGame(root)
    root.mainloop()

