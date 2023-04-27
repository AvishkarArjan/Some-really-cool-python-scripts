import webbrowser

def mark_1():
    print("""
                      _                    
  __ _ ___  ___  __ _| |___   __ ___ _ __  
 / _` / _ \/ _ \/ _` | / -_)_/ _/ _ \ '  \ 
 \__, \___/\___/\__, |_\___(_)__\___/_|_|_|
 |___/          |___/                      
    """)
    while True:
        mySearch = input("What to search today\n")
        print("opening now")
        chrome_path="https://google.com/search?q="
        webbrowser.open(chrome_path+mySearch,new=1)

mark_1()

