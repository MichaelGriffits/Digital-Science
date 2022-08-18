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
back_button_il = Button(information_library_frame, text="BACK", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())

# Information Library Menu Widgets Placement
back_button_il.grid(row=0, column=0)

# Character Creation Menu Widgets Creation
back_button_cc = Button(character_creation_frame, text="BACK", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())
random_stat_button = Button(character_creation_frame, text="Roll Your Random Stat",
                            command=lambda: test_button_click())
random_stat_val_1 = IntVar()
random_stat_val_2 = IntVar()
random_stat_val_3 = IntVar()
random_stat_val_4 = IntVar()
random_stat_val_5 = IntVar()
random_stat_val_6 = IntVar()
random_stat_label_1 = Label(character_creation_frame, textvariable=random_stat_val_1)
random_stat_label_2 = Label(character_creation_frame, textvariable=random_stat_val_2)
random_stat_label_3 = Label(character_creation_frame, textvariable=random_stat_val_3)
random_stat_label_4 = Label(character_creation_frame, textvariable=random_stat_val_4)
random_stat_label_5 = Label(character_creation_frame, textvariable=random_stat_val_5)
random_stat_label_6 = Label(character_creation_frame, textvariable=random_stat_val_6)


# Character Creation Menu Widgets Placement
back_button_cc.grid(row=0, column=0)
random_stat_button.grid(row=3, column=2)
random_stat_label_1.grid(row=3, column=0)
random_stat_label_2.grid(row=4, column=0)
random_stat_label_3.grid(row=5, column=0)
random_stat_label_4.grid(row=6, column=0)
random_stat_label_5.grid(row=7, column=0)
random_stat_label_6.grid(row=8, column=0)


# Main Menu Widgets Placement
menu_name.grid(row=0, column=2, padx=125, pady=15)
menu_sub_name.grid(row=1, column=2)
create_character_button.grid(row=2, column=2, pady=300)
information_library_button.grid(row=2, column=1, padx=100)
load_character_button.grid(row=2, column=3, padx=100)
quit_button.grid(row=3, column=2, padx=100)
main_menu.mainloop()
