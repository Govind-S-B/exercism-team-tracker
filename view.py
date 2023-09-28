import sys
import subprocess
import webbrowser

USERNAMES = ["govind-s-b","officiallyaninja","sibycr18","jydv402","aminafayaz","emielsa","definitelyarjun","vb-123"]
CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Get the exercise name from command line arguments
if len(sys.argv) > 1:
    exercise_name = sys.argv[1]
else:
    print("Please provide an exercise name as a command line argument.")
    sys.exit(1)

my_chrome_process   = subprocess.Popen(CHROME_PATH, shell=False)

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(CHROME_PATH))

for username in USERNAMES :
    webbrowser.get('chrome').open_new_tab(f"https://exercism.org/tracks/python/exercises/{exercise_name}/solutions/{username}")

my_chrome_process.terminate()