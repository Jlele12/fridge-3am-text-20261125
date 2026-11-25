import os

LINE = "It's 3am. I know you're not hungry. But I'm lonely and cold, so let's just open me, look at the cheese, and move on."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
