# Simple Selection Menu Template
# Required packages: colorama
# pip install colorama
import colorama
from colorama import Fore, Style

def print_menu():
    # Ascii Art | Get some Ascii Art here: https://patorjk.com/software/taag/
    ascii_art = """       
       _____                                                                                
 ____  \    \   ____________  _____                    ___________            _____         
 \   \ /____/| /            \|\    \                  /           \         /      |_       
  |  |/_____|/|\___/\  \\\___/|\\\    \                /    _   _    \       /         \      
  |  |    ___  \|____\  \___|/ \\\    \              /    //   \\\    \     |     /\    \     
  |   \__/   \       |  |       \|    | ______     /    //     \\\    \    |    |  |    \    
 /      /\___/| __  /   / __     |    |/      \   /     \\\_____//     \   |     \/      \   
/      /| | | |/  \/   /_/  |    /            |  /       \ ___ /       \  |\      /\     \  
|_____| /\|_|/|____________/|   /_____/\_____/| /________/|   |\________\ | \_____\ \_____\ 
|     |/      |           | /  |      | |    |||        | |   | |        || |     | |     | 
|_____|       |___________|/   |______|/|____|/|________|/     \|________| \|_____|\|_____|                      
    """

    second_text = "A Python Template Repository."

    colorama.init()

    # Make Ascii Red and reset Color for Second Text
    print(Fore.RED + ascii_art + Fore.RESET + second_text + '\n\n\n')

    colorama.deinit()

    # Menupoints
    menu_items = [
        "[1] » Display Hello",
        "[2] » Exit",
        "Choice 3",
        "Choice 4",
        "Choice 5",
        "Choice 6",
        "Choice 7",
        "Choice 8",
        "Choice 9",
        "Choice 10",
        "Choice 11",
        "Choice 12"
    ]

    # Select how many Colums you want
    columns = 4

    rows = -(-len(menu_items) // columns)

    # Show Menu Points
    for row in range(rows):
        for col in range(columns):
            index = row + col * rows
            if index < len(menu_items):
                print(f"{menu_items[index]:<20}", end="") 
        print()



# Print Menu
print_menu()

# User Input
choice = input("\n" + Fore.GREEN + "menu" + Fore.WHITE + "@template$ ")

# Example for user input
if choice == "1":
    print("Hello!")
elif choice == "2":
    print("Good Bye!")
    exit()
else:
    print("Invalid choice")