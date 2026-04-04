import json

class GameEngine:
    def __init__(self, story_file):
        with open(story_file, "r") as file:
            self.story = json.load(file)
        self.current_scene = "start"

    def play(self):
        while True:
            scene = self.story[self.current_scene]
            print("\n" + scene["text"])

            if not scene["choices"]:
                print("\n=== END ===")
                break

            for key, choice in scene["choices"].items():
                print(f"{key}. {choice}")

            user_input = input("Choose: ").strip()
            if user_input in scene["next"]:
                self.current_scene = scene["next"][user_input]
            else:
                print("Invalid choice.")
