import os
import sys
import time
import msvcrt
import pyperclip
from fuzzywuzzy import fuzz, process

def fuzzyMatchChoice(user_input, options_dict, search_field='title', min_score=60):
    """
    Match user input to a dictionary key using fuzzy matching.
    
    Args:
        user_input: The user's input (string)
        options_dict: Dictionary of options to search through
        search_field: Field name to search in (e.g., 'title', 'name', 'Department')
        min_score: Minimum similarity score (0-100) to consider a match
    
    Returns:
        The matching key if found, None otherwise
    """
    # If input is empty, return None
    if not user_input or not user_input.strip():
        return None
    
    user_input = user_input.strip()
    
    # First, try exact key match (for backward compatibility with numbers)
    if user_input in options_dict:
        return user_input
    
    # Build a list of searchable strings with their corresponding keys
    search_items = []
    for key, value in options_dict.items():
        if isinstance(value, dict) and search_field in value:
            search_text = value[search_field]
        elif isinstance(value, str):
            search_text = value
        else:
            search_text = str(value)
        search_items.append((key, search_text))
    
    # Use process.extractOne to find the best match
    choices = [item[1] for item in search_items]
    result = process.extractOne(user_input, choices, scorer=fuzz.WRatio)
    
    if result and result[1] >= min_score:
        # Find the key corresponding to the matched text
        matched_text = result[0]
        for key, text in search_items:
            if text == matched_text:
                return key
    return None
    
def displayGuidesMenu():
    clearScreen()
    print("Guides")
    print("=" * 6)
    for k, v in guides.items():
        print(f"{k}) {v['title']}")
    print("0) Back")
    print("\n(You can enter the guide number or type part of the guide name)")
    choice = input("\nSelect a guide: ").strip()
    # Use fuzzy matching if not "0" (back)
    if choice != "0":
        matched = fuzzyMatchChoice(choice, guides, search_field='title')
        if matched:
            return matched
    return choice

def showGuide(guideID):
    clearScreen()
    guide = guides.get(guideID)
    if not guide:
        print("Invalid selection.")
        pause()
        return
    print(guide['title'])
    print("-" * len(guide['title']))
    print(guide['content'])
    print()
    pause()

guides = {
    "1": {
        "title": "How To Verify Security Stack",
        "content": "Step 1: Press the Windows button and type \"addre\" in the Windows Search bar to get to the Add or Remove Programs window.\n\nStep 2: Look for the following programs in the list: \n\t - AutoElevate\n\t - Cortex XDR\n\t - Duo (version 5.1.1)\n\t - Illumio\n\t - NinjaRMM Agent\n\t\nIf you see \"Carbon Black\", note that software should be uninstalled.\n\nStep 3: Please look at the next guide (press 0!)"
    },
    "2": {
        "title": "How To Install/Uninstall Security Stack",
        "content": "Step 1: Navigate to "
    }
}

troubleshooting = {
    "1": {
        "title": "Test",
        "content": "Test2"
    }
}

windowsKeys = {
    "1": {
        "name": "Windows 11",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "2": {
        "name": "Windows 10",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "3": {
        "name": "Windows 8.1",
        "key": "MPXWC-7CN4B-64FCB-9T69B-F9BDQ"
    },
    "4": {
        "name": "Windows 7",
        "key": "YTH8H-3VJ37-T3RVT-YH7HG-KCVPD"
    }
}

def displayTroubleshootingMenu():
    clearScreen()
    print("Troubleshooting")
    print("=" * 14)
    for k, v in troubleshooting.items():
        print(f"{k}) {v['title']}")
    print("0) Back")
    print("\n(You can enter the issue number or type part of the issue name)")
    choice = input("\nSelect an issue: ").strip()
    # Use fuzzy matching if not "0" (back)
    if choice != "0":
        matched = fuzzyMatchChoice(choice, troubleshooting, search_field='title')
        if matched:
            return matched
    return choice

def showTroubleshooting(issue_id):
    clearScreen()
    issue = troubleshooting.get(issue_id)
    if not issue:
        print("Invalid selection.")
        pause()
        return
    print(issue['title'])
    print("-" * len(issue['title']))
    print(issue['content'])
    print()
    pause()

costCenters = {
    "728": {
        "Department": "Library Services (Library)",
        "Location": "325 Avenue A NW, Winter Haven, FL 33881",
        "Contact": "Jane Martin, jmartin@mywinterhaven.com, 333-333-3333",
    },

    "923": {
        "Department": "Technology Services (Nora Mayo Hall, City Hall Annex)",
        "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881, Nora Mayo Hall - 800 Ave A NW, Winter Haven, FL 33881",
        "Contact": "Hiep Nguyen, hnguyen@mywinterhaven.com, 333-333-3333",
    },

    "618": {
        "Department": "Water Department Customer Service", 
        "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881", 
        "Contact": "Gabby Gardner, ggardner@mywinterhaven.com, 863-291-5678 x 3370",
    },

    "111": {
        "Department": "Finance Department",
        "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Coleen \"CJ\" Scott (CFO), cjscott@mywinterhaven.com, 863-291-5667 x 2500", 
    },

    "101": {
        "Department": "City Commission",
        "Location":  "City Manager's Office/Commision - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Bradley T. Dantzler (Mayor), btdantzler@mywinterhaven.com, 863-291-5600 x 224", #Check this again
    },
    "102": {
        "Department": "Legal",
        "Location": "City Attorney's Office - 245 South Central Ave, Bartow, FL 33830", 
        "Contact": "Frederick John Murlphy, Jr., Esquire (City Attorney), @fjmurphy.com, 863-294-3363", 
    },

    "103": {
        "Department": "City Manager",
        "Location": "City Hall - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "T.Michael Stavres (City Manager), mstavres@mywinterhaven.com, 863-291-5600 x 221",
    },

    "105": {
        "Department": "City Clerk",
        "Location": "City Hall - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Vanessa Castillo (City Clerk N), vcastillo@mywinterhaven.com, 863-291-5600 x 224",
    },

    "217": {
        "Department": "Code Compliance",
        "Location": "Fire Station 4 - 1254 Fairfax St NE Winter Haven, FL 33881",
        "Contact": "Ayers Tanya (Code Compliance Supervisor), tayers@mywinterhaven.com, 863-291-5697", #mainline?
    },

    "200": {
        "Department": "Public Safety - Police",
        "Location": "Police Department - 125 North Lake Silver Drive NW, Winter Haven, FL 33881",
        "Contact": "Vance Monroe (Police Chief), vmonroe@mywinterhaven.com, 863-291-5858", #mainline?
    },

    "204": {
        "Department": "PAL",
        "Location": "N/A",
        "Contact": "N/A",

    },

    "206": {
        "Department": "Police Grants",
        "Location": "N/A",
        "Contact": "N/A",
    },

    "213": {
        "Department": "Public Safety - Fire Stations",
        "Location": "Fire Station 1 - 301 Avenue G, Winter Haven, FL 33880\n\t\t       Fire Station 2 - 4700 Lucerne Park Rd, Winter Haven, FL 33881\n\t\t       Fire Station 3 - 6975 Eloise Loop Rd, Winter Haven, FL 33884\n\t\t       Fire Station 4 - 1254 Fairfax St NE, Winter Haven, FL 33881\n\t\t       Fire Station 5 - 1803 Havendale Blvd., Winter Haven, FL 33881",
        "Contact": "Fire Station 1 - Non-Emergency Number - 863-291-5665\n\t\t       Fire Station 2 - Non-Emergency Number - 863-298-5212\n\t\t       Fire Station 3 - Non-Emergency Number - 863-298-5212\n\t\t       Fire Station 4 - Non-Emergency Number - 863-282-8034\n\t\t       Fire Station 5 - Non-Emergency Number - 863-282-8035",
    },
    
    "312": {
        "Department": "Parks & Grounds", # Have this information
        "Location": "N/A:",
        "Contact": "N/A",

    },

    "700": {
        "Department": "Parks & Recreation Administration",
        "Location": "Nora Mayor Hall - 500 Third Street NW, Winter Haven, FL 33880",
        "Contact": "N/A" #Need this information
    },

    "705": {
        "Department": "Fieldhouse & Conference Center",
        "Location": "AdventHealth FieldHouse & Conference Center - 210 Cypress Gardens Blvd, Winter Haven, FL 33880",
        "Contact": "N/A" #Mainline?
    
    },

    "306": {
        "Department": "Commercial Refuse",
        "Location": "2501 Motor Pool Road, 33881",
        "Contact": "Brittany Hart (Public Works Director), bhart@mywinterhaven.com, 863-291-5756",
    },
    "709": {
        "Department": "W.H. Rec. & Cultural Center",
        "Location": "WH Recreation and Cultural Center -  801 Martin Luther King Blvd NE, Winter Haven, FL 33881",
        "Contact": "Demetrius Sanders (Recreation Superviso I), dsanders@mywinterhaven.com, 863-291-5675",

    },
    "711": {
        "Department": "Acivity Fields",
        "Location": "AdventHealth Fieldhouse and Conference Center - 210 Cypress Gardens Blvd, Winter Haven, FL 33880",
        "Contact": "Neal Kris (Crew Leader II), kneal@mywinterhaven.com, 863-291-5745",

    },
    "400": {
        "Department": "Public Svc Bldgs/ Nora Mayor Hall",
        "Location": "Nora Mayor Hall - 500 3rd St NW, Winter Haven, FL 33881",
        "Contact": "N/A" #Requires multiple?

    },
    "401": {
        "Department": "Streets",
        "Location": "2745 Motor Pool Road, 33881",
        "Contact" : "Mike Campbell (Streets & Drainage Superintendent), mcampbell@mywinterhaven.com, 863-291-5852", #Mike Campbell doesn't pop up on outlook

    },
    "218": {
        "Department": "Growth Management/Planning", #Unsure which planning, will use AICP 
        "Location":"City Hall - 451 3rd Street NW, Winter Haven, FL 33881",
        "Contact": "Eric Labbe (Department Director), elabbe@mywinterhaven.com, 863-291-5600 x 241",

    },

    "301": {
        "Department": "Water Plants/Utility Services",
        "Location" : "1334 Fairfax Drive",
        "Contact" : "Steven Warder (Water Plant Manager), swarder@mywinterhaven.com, 863-291-5767",

    },
    "304": {
        "Department": "Wastewater Treatment Plant #2",
        "Location": "2746 Motor Pool Road, Winter Haven, FL 33881",
        "Contact": "David Nicholson (Wastewater Treament Plants Manager), 863-514-0438 " #Address from city directory

    },
    "310": {
        "Department": "Utility Services Administration",
        "Location": "" #Ask about this department

    },
    "316": {
        "Department": "", #Ask about this department
        "Location": "", 
        "Contact": "",

    },
    "322": {
        "Department": "", # Ask about this department
        "Location": "", 
        "Contact": "",
    },
    "323": {
        "Department": "", # Ask about this department
        "Location": "", 
        "Contact": "",

    },
    "905": {
        "Department": "City Hall",
        "Location": "City Hall - 451 3rd St NW, Winter Haven, FL 33881", 
        "Contact": "Heather Pellegrino (Communication Staff Assistant), hpellegrino@mywinterhaven.com, 863-291-5678",
    },
    "907": {
        "Department": "Fleet Maintenance", 
        "Location": "2501 Motor Pool Road, Winter Haven, FL 33881",  #Need the location name
        "Contact": "Aaron Russel (Fleet Maintenance Manager), ", 
        }
}

windowsKeys = {
    "1": {
        "name": "Windows 11",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "2": {
        "name": "Windows 10",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "3": {
        "name": "Windows 8.1",
        "key": "MPXWC-7CN4B-64FCB-9T69B-F9BDQ"
    },
    "4": {
        "name": "Windows 7",
        "key": "YTH8H-3VJ37-T3RVT-YH7HG-KCVPD"
    },
    "5": {
        "name": "Microsoft Office 2024",
        "key": "GWNJM-H6FRF-39GGY-KHD9Y-MY883"
    }
}

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#wait for keypress
def pause(msg="Press any key to continue..."):
    print(msg, end='', flush=True)
    msvcrt.getch()
    print()

def displayHome():
    clearScreen()
    banner = r"""
 _____ _                _    _                _ _       
/  ___| |              | |  (_)              | (_)      
\ `--.| | ___   _ _ __ | | ___ _ __   ___  __| |_  __ _ 
 `--. \ |/ / | | | '_ \| |/ / | '_ \ / _ \/ _` | |/ _` |
/\__/ /   <| |_| | | | |   <| | |_) |  __/ (_| | | (_| |
\____/|_|\_\\__,_|_| |_|_|\_\_| .__/ \___|\__,_|_|\__,_|
                              | |                       
                              |_|                       
    """
    bigfoot = r"""
       _...._
     .-.     /
    /o.o\ ):.\
    \   / `- .`--._
    // /            `-.
   '...\     .         `.
    `--''.    '          `.
        .'   .'            `-.
     .-'    /`-.._            \
   .'    _.'      :      .-'"'/
  | _,--`       .'     .'    /
  \ \          /     .'     /
   \///        |    ' |    /
               \   (  `.   ``-.
                \   \   `._    \
              _.-`   )    .'    )
              `.__.-'  .-' _-.-'
                       `.__,'
    """
    print(banner)
    print("Welcome to SKUNKIPEDIA!")
    print("\nA quick-reference IT dictionary.\n")
    print(bigfoot)
    print()
    pause()

def displayMainMenu():
    #main menu options
    clearScreen()
    print("SKUNKIPEDIA - Main Menu")
    print("=" * 26)
    print("1) Cost Centers")
    print("2) Windows Activation Key")
    print("3) Guides")
    print("4) Troubleshooting")
    print("0) Exit")
    print("\n(You can enter the option number or type part of the menu name)")
    choice = input("\nSelect an option: ").strip()
    # Use fuzzy matching for main menu
    main_menu_options = {
        "1": {"name": "Cost Centers"},
        "2": {"name": "Windows Activation Key"},
        "3": {"name": "Guides"},
        "4": {"name": "Troubleshooting"},
        "0": {"name": "Exit"}
    }
    if choice != "0":
        matched = fuzzyMatchChoice(choice, main_menu_options, search_field='name')
        if matched:
            return matched
    return choice

def displayCostCenters():
    clearScreen()
    print("Cost Centers")
    print("=" * 12)
    for cc in costCenters:
        dept = costCenters[cc]["Department"]
        print(f"{cc}) {dept}")
    print("0) Back")
    print("\n(You can enter the cost center number or type part of the department name)")
    choice = input("\nEnter cost center number: ").strip()
    # Use fuzzy matching if not "0" (back)
    if choice != "0":
        matched = fuzzyMatchChoice(choice, costCenters, search_field='Department')
        if matched:
            return matched
    return choice
def showCostCenter(ccNumber):
    clearScreen()
    data = costCenters.get(ccNumber)
    if not data:
        print("Invalid cost center number.")
        pause()
        return
    print(f"Cost Center: {ccNumber}")
    print("-" * 30)
    print(f"Department           : {data['Department']}\nLocation             : {data['Location']}\nPrimary Contact      : {data['Contact']}")
    print()
    pause()

def displayActivationKeyMenu():
    clearScreen()
    print("Windows Activation Keys")
    print("=" * 23)
    for k, v in windowsKeys.items():
        print(f"{k}) {v['name']}")
    print("0) Back")
    print("\n(You can enter the option number or type part of the Windows version name)")
    choice = input("\nSelect an option: ").strip()
    # Use fuzzy matching if not "0" (back)
    if choice != "0":
        matched = fuzzyMatchChoice(choice, windowsKeys, search_field='name')
        if matched:
            return matched
    return choice

def showActivationKey(version):
    clearScreen()
    key_info = windowsKeys.get(version)
    if not key_info:
        print("Invalid selection.")
        pause()
        return
    print(f"{key_info['name']} Activation Key")
    print("=" * (len(key_info['name']) + 16))
    print(key_info['key'])
    pyperclip.copy(key_info['key'])
    print(f"\n[{key_info['name']} key has been copied to the clipboard.]\n")
    print()
    pause()

def main():
    displayHome()
    while True:
        choice = displayMainMenu()
        if choice == "1":
            while True:
                costCenterChoice = displayCostCenters()
                if costCenterChoice  == "0":
                    break
                showCostCenter(costCenterChoice)
        elif choice == "2":
            while True:
                version = displayActivationKeyMenu()
                if version == "0":
                    break
                showActivationKey(version)
        elif choice == "3":
            # Guides submenu
            while True:
                guideChoice = displayGuidesMenu()
                if guideChoice == "0":
                    break
                showGuide(guideChoice)
        elif choice == "4":
            # Troubleshooting submenu
            while True:
                troubleshootChoice = displayTroubleshootingMenu()
                if troubleshootChoice == "0":
                    break
                showTroubleshooting(troubleshootChoice)
        elif choice == "0":
            clearScreen()
            print("Goodbye!")
            time.sleep(0.5)
            sys.exit(0)
        else:
            print("Invalid selection. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()

# how to build?
# do it in howard -
#  pyinstaller --onefile skunkipedia.py --distpath "\\\\howard\\01 - Technology Services\\11 - Training"

# do it in the github folder
# pyinstaller --onefile skunkipedia.py (can't already be open)


