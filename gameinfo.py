class GameInfo():
    __author = "Thomas"
    __game_title = "The Haunted Maze"
    __game_title_ascii = '''                         _           _                           
  /\  /\__ _ _   _ _ __ | |_ ___  __| |  _ __ ___   __ _ _______ 
 / /_/ / _` | | | | '_ \| __/ _ \/ _` | | '_ ` _ \ / _` |_  / _ \\
/ __  / (_| | |_| | | | | ||  __/ (_| | | | | | | | (_| |/ /  __/
\/ /_/ \__,_|\__,_|_| |_|\__\___|\__,_| |_| |_| |_|\__,_/___\___|
                                                                 '''

    @classmethod
    def credits(cls):
        print("\nThank you for playing the:")
        print(cls.__game_title_ascii)
        print(f"Created by {cls.__author}")

    @classmethod
    def welcome(cls):
        print(cls.__game_title_ascii)
        print(f"Created by {cls.__author}")
        
    @classmethod
    def help(cls):
        print("\nCommands:")
        print(" - north, east, south, west")
        print(" - take")
        print(" - bribe")
        print(" - talk")
        print(" - fight")
        print(" - help or ?")
        print(" - quit")
        print()