from tkinter import *
from random import randint

main_menu = Tk()
main_menu.title("Character Creator")
main_menu.geometry("1920x1080")

main_menu_frame = Frame(main_menu)
main_menu_frame.grid(row=0, column=0)
character_creation_frame = Frame(main_menu)
character_creation_frame.grid_forget()
information_library_frame = Frame(main_menu)
information_library_frame.grid_forget()
load_character_frame = Frame(main_menu)
load_character_frame.grid_forget()


# Quit Program Function
def quit_program():
    quit()


# Main Menu To Information Library Function
def open_information_library():
    main_menu_frame.grid_forget()
    information_library_frame.grid(row=0, column=0)


# Main Menu To Character Creation Function
def open_character_creation():
    main_menu_frame.grid_forget()
    character_creation_frame.grid(row=0, column=0)


# Main Menu To Load Character Menu function
def open_load_character():
    main_menu_frame.grid_forget()
    load_character_frame.grid(row=0, column=0)


# Back To Main Menu From Character Creation function
def back_to_main_menu():
    character_creation_frame.grid_forget()
    information_library_frame.grid_forget()
    load_character_frame.grid_forget()
    main_menu_frame.grid(row=0, column=0)


def test_button_click():
    random_stat_val_1.set(randint(3, 18))
    random_stat_val_2.set(randint(3, 18))
    random_stat_val_3.set(randint(3, 18))
    random_stat_val_4.set(randint(3, 18))
    random_stat_val_5.set(randint(3, 18))
    random_stat_val_6.set(randint(3, 18))


def show_race():
    global chosen_race
    chosen_race = race_dropdown_variable.get()
    race_information_label.config(text=race_dictionary[chosen_race])


def show_class():
    global chosen_class
    chosen_class = class_dropdown_variable.get()
    class_information_label.config(text=class_dictionary[chosen_class])


# Main Menu Widgets Creation
menu_name = Label(main_menu_frame, text="Dungeons & Dragons", font="helvetica 40 bold")
menu_sub_name = Label(main_menu_frame, text="Character Creator", font="helvetica 15 bold")
create_character_button = Button(main_menu_frame, text="CREATE A CHARACTER", font="helvetica 20 bold",
                                 command=lambda: open_character_creation())
information_library_button = Button(main_menu_frame, text="INFORMATION LIBRARY", font="helvetica 20 bold",
                                    command=lambda: open_information_library())
load_character_button = Button(main_menu_frame, text="LOAD CHARACTER", font="helvetica 20 bold",
                               command=lambda: open_load_character())
quit_button = Button(main_menu_frame, text="QUIT", font="helvetica 20 bold",
                     command=lambda: quit_program())

# Load Character Menu Widgets Creation
back_button_lc = Button(load_character_frame, text="Back", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())

# Load Character Menu Widgets Placement
back_button_lc.grid(row=0, column=0)

# Information Library Menu Widgets Creation
race_dropdown_variable = StringVar()
race_dropdown_variable.set("Races")
race_dictionary = {"Races": "Race is a rule in Dungeons & Dragons referring to the fantasy species or ancestry of a character.\n "
                            "Popular races include human, elf, dwarf and halfling. Unlike the modern real-world use of the\n "
                            "word, 'race' in Dungeons & Dragons does not refer to a character's ethnic background."
                   , "Aarakocra": "Sequestered in high mountains atop tall trees, the aarakocra sometimes called birdfolk, evoke\n "
                                  "fear and wonder. Many aarakocra aren’t even native to the Material Plane. They hail from a \n"
                                  "world beyond—from the boundless vistas of the Elemental Plane of Air. They are immigrants, \n"
                                  "refugees, scouts, and explorers, their outposts functioning as footholds in a world both strange and alien."
                   , "Aasimar": "Aasimar are the descendants of celestial beings. These folk generally appear as glorious humans \n"
                                " with lustrous hair, flawless skin, and piercing eyes. Aasimar often attempt to pass as humans\n"
                                " in order to right wrongs and defend goodness on the Material Plane without drawing undue \n"
                                "attention to their celestial heritage. They strive to fit into society, although they usually rise to the\n"
                                " top, becoming revered leaders and honourable heroes."
                   , "Bugbear": "Bugbears are born for battle and mayhem. Surviving by raiding and hunting, they bully the weak \n"
                                "and despise being bossed around, but their love of carnage means they will fight for powerful\n "
                                "masters if bloodshed and treasure are assured. Bugbears are often found in the company of \n"
                                "their cousins, hobgoblins and goblins. Bugbears usually enslave goblins they encounter, and they bully \n"
                                "hobgoblins into giving them gold and food in return for serving as scouts and shock troops. Even when paid,\n"
                                " bugbears are at best unreliable allies, yet goblins and hobgoblins understand that no matter how much\n"
                                " bugbears might drain a tribe of resources, these creatures are a potent force."
                   , "Centaur": "Reclusive wanderers and omen-readers of the wild, centaurs avoid conflict but fight fiercely when\n"
                                " pressed. They roam the vast wilderness, keeping far from borders, laws, and the company of\n"
                                " other creatures. Centaur tribes range across lands with mild to hot climates. They are \n"
                                "hunter-gatherers and rarely build shelters or even use tents. A centaur that can't keep pace with the rest of\n"
                                " its tribe is left behind. Some such centaurs vanish into the wilderness and are never seen again. Those \n"
                                "that can bear the loss of their tribe might take up residence among other races. Frontier settlements\n"
                                " value the natural knowledge of their centaur residents. Many such communities owe their survival to the\n"
                                " insight and acumen of a centaur."
                   }
confirm_race_button = Button(information_library_frame, text="Find Info About The Race", font="helvetica 8", command=lambda: show_race())
race_information_label = Label(information_library_frame, text="Race is a rule in Dungeons & Dragons referring to the fantasy species or ancestry of a character.\n "
                            "Popular races include human, elf, dwarf and halfling. Unlike the modern real-world use of the\n"
                            "word, 'race' in Dungeons & Dragons does not refer to a character's ethnic background.", font="helvetica 10")

back_button_il = Button(information_library_frame, text="BACK", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())
information_of_race = OptionMenu(information_library_frame, race_dropdown_variable, "Races", "Aarakocra", "Aasimar", "Bugbear", "Centaur", "Changeling", "Dragonborn", "Dwarf", \
                                 "Elf", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Grung", "Half-Elf", "Halfling", "Half-Orc", "Hobgoblin", "Human", "Kalashtar", \
                                 "Kenku", "Kobold", "Lizardfolk", "Locathah", "Loxodon", "Minotaur", "Orc", "Simic Hybrid", "Shifter", "Tabaxi", "Tiefling", "Tortle", "Triton", \
                                 "Veldalken", "Verdan", "Warforged", "Yuan-Ti Pureblood")
information_of_race.configure(font="helvetica 23 bold")
confirm_class_button = Button(information_library_frame, text="Find Info About The Class", font="helvetica 8", command=lambda: show_class())
class_information_label = Label(information_library_frame, text="Your class is the primary definition of what your character can do in the extraordinary magical\n"
                               "landscape of Dungeons & Dragons. A class is more than a profession; it is your character’s calling.", font="helvetica 10")
class_dropdown_variable = StringVar()
class_dropdown_variable.set("Classes")
information_of_class = OptionMenu(information_library_frame, class_dropdown_variable, "Classes", "Artificer", "Barbarian", "Bard", "Cleric", "Druid"\
                                  , "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")
information_of_class.configure(font="helvetica 23 bold")
class_dictionary = {"Classes": "Your class is the primary definition of what your character can do in the extraordinary magical\n"
                               "landscape of Dungeons & Dragons. A class is more than a profession; it is your character’s calling."
                    ,"Artificer": "Makers of magic-infused objects, artificers are defined by their inventive nature. They see magic\n" 
                                 "as a complex system waiting to be decoded and controlled. Instead of ephemeral spells, they seek \n"
                                 "to craft durable, useful, marvelous magical items."}
heading_information = Label(information_library_frame, text="Information Library", font="helvetica 30 bold")

# Information Library Menu Widgets Placement
back_button_il.grid(row=0, column=0)
information_of_race.grid(row=3, column=1, padx=10)
race_information_label.grid(row=5, column=1)
confirm_race_button.grid(row=4, column=1)
information_of_class.grid(row=6, column=1)
class_information_label.grid(row=8, column=1)
confirm_class_button.grid(row=7, column=1)
heading_information.grid(row=0, column=2)

# Character Creation Menu Widgets Creation
back_button_cc = Button(character_creation_frame, text="BACK", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())
random_stat_button = Button(character_creation_frame, text="Roll Your Random Stat",
                            command=lambda: test_button_click())
name_input = Entry(character_creation_frame, width=30, font="helvetica 20 bold")
random_stat_val_1 = IntVar()
random_stat_val_2 = IntVar()
random_stat_val_3 = IntVar()
random_stat_val_4 = IntVar()
random_stat_val_5 = IntVar()
random_stat_val_6 = IntVar()
random_stat_label_1 = Label(character_creation_frame, textvariable=random_stat_val_1, font="helvetica 15")
random_stat_label_2 = Label(character_creation_frame, textvariable=random_stat_val_2, font="helvetica 15")
random_stat_label_3 = Label(character_creation_frame, textvariable=random_stat_val_3, font="helvetica 15")
random_stat_label_4 = Label(character_creation_frame, textvariable=random_stat_val_4, font="helvetica 15")
random_stat_label_5 = Label(character_creation_frame, textvariable=random_stat_val_5, font="helvetica 15")
random_stat_label_6 = Label(character_creation_frame, textvariable=random_stat_val_6, font="helvetica 15")
strength_stat_label_1 = Label(character_creation_frame, text="STR", font="helvetica 20 bold")
dexterity_stat_label_2 = Label(character_creation_frame, text="DEX", font="helvetica 20 bold")
constitution_stat_label_3 = Label(character_creation_frame, text="CON", font="helvetica 20 bold")
intelligence_stat_label_4 = Label(character_creation_frame, text="INT", font="helvetica 20 bold")
wisdom_stat_label_5 = Label(character_creation_frame, text="WIS", font="helvetica 20 bold")
charisma_stat_label_6 = Label(character_creation_frame, text="CHA", font="helvetica 20 bold")
strength_input = Entry(character_creation_frame, width=2, font="helvetica 15 bold")
dexterity_input = Entry(character_creation_frame, width=2, font="helvetica 15 bold")
constitution_input = Entry(character_creation_frame, width=2, font="helvetica 15 bold")
intelligence_input = Entry(character_creation_frame, width=2, font="helvetica 15 bold")
wisdom_input = Entry(character_creation_frame, width=2, font="helvetica 15 bold")
charisma_input = Entry(character_creation_frame, width=2, font="helvetica 15 bold")

# Character Creation Menu Widgets Placement
back_button_cc.grid(row=0, column=0, sticky="w")
name_input.grid(row=2, column=1, columnspan=3)
random_stat_button.grid(row=15, column=0, sticky="w")
random_stat_label_1.grid(row=3, column=0, pady=5, padx=15, sticky="w")
random_stat_label_2.grid(row=4, column=0, pady=5, padx=15, sticky="w")
random_stat_label_3.grid(row=5, column=0, pady=5, padx=15, sticky="w")
random_stat_label_4.grid(row=6, column=0, pady=5, padx=15, sticky="w")
random_stat_label_5.grid(row=7, column=0, pady=5, padx=15, sticky="w")
random_stat_label_6.grid(row=8, column=0, pady=5, padx=15, sticky="w")
strength_stat_label_1.grid(row=4, column=1, sticky="w")
dexterity_stat_label_2.grid(row=6, column=1, sticky="w")
constitution_stat_label_3.grid(row=8, column=1, sticky="w")
intelligence_stat_label_4.grid(row=10, column=1, sticky="w")
wisdom_stat_label_5.grid(row=12, column=1, sticky="w")
charisma_stat_label_6.grid(row=14, column=1, sticky="w")
strength_input.grid(row=3, column=1, sticky="w")
dexterity_input.grid(row=5, column=1, sticky="w")
constitution_input.grid(row=7, column=1, sticky="w")
intelligence_input.grid(row=9, column=1, sticky="w")
wisdom_input.grid(row=11, column=1, sticky="w")
charisma_input.grid(row=13, column=1, sticky="w")

# Main Menu Widgets Placement
menu_name.grid(row=0, column=2, padx=125, pady=15)
menu_sub_name.grid(row=1, column=2)
create_character_button.grid(row=2, column=2, pady=300)
information_library_button.grid(row=2, column=1, padx=100)
load_character_button.grid(row=2, column=3, padx=100)
quit_button.grid(row=3, column=2, padx=100)

main_menu.mainloop()
