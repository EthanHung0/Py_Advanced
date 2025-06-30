from Classes import MP3Player,VideoPlayer,StreamingPlayer

def system():
    print("""
    ----------------------------
    |       MEDIA PLAYER       |
    ----------------------------""")
    file_name = input("Input file (mp3/mp4 suffix or https:// prefix): ")
    exit_ = True
    while exit_:
        exit_ = file_subsys(file_name)
def file_subsys(file_name):
    if file_name.endswith(".mp3"):
        FILE = MP3Player(file_name)
        print(f"""
    MP3 PLAYER. file: {file_name}
1.play
2.pause
3.stop
4.exit""")
        choice = input("Input command (1-2-3-4): ")
        choice = choice.strip()
        if choice == "1":
            print(FILE.play())
        elif choice == "2":
            print(FILE.pause())
        elif choice == "3":
            print(FILE.stop())
        elif choice == "4":
            return False
        else:
            print("Invalid Input.")

    elif file_name.endswith(".mp4"):
        FILE = VideoPlayer(file_name)
        print(f"""
    VIDEO PLAYER. file: {file_name}
1.play
2.pause
3.stop
4.exit""")
        choice = input("Input command (1-2-3-4): ")
        choice = choice.strip()
        if choice == "1":
            print(FILE.play())
        elif choice == "2":
            print(FILE.pause())
        elif choice == "3":
            print(FILE.stop())
        elif choice == "4":
            return False
        else:
            print("Invalid Input.")

    elif file_name.startswith("https://"):
        FILE = StreamingPlayer(file_name)
        print(f"""
    STREAMING PLAYER. file: {file_name}
1.play
2.pause
3.stop
4.exit""")
        choice = input("Input command (1-2-3-4): ")
        choice = choice.strip()
        if choice == "1":
            print(FILE.play())
        elif choice == "2":
            print(FILE.pause())
        elif choice == "3":
            print(FILE.stop())
        elif choice == "4":
            return False
        else:
            print("Invalid Input.")

    else:
        print("Invalid Input.")
        return False

    return True

while True:
    system()