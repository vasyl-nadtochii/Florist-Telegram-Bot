from datetime import datetime

def on_bot_started():
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print(f"BOT: Bot started successfully at { time }")