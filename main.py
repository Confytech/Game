from ai_engine.engine import GameEngine

if __name__ == "__main__":
    game = GameEngine("story/story.json")
    game.play()