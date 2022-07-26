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
users_correct_input = StringVar()
users_input = StringVar()
amount_of_characters = 0

# Quit Program Function
## Main Menu Changes 2
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

#Rolls the user random stats if they wish to use them
def random_stat_roll():
    random_stat_val_1.set(randint(3, 18))
    random_stat_val_2.set(randint(3, 18))
    random_stat_val_3.set(randint(3, 18))
    random_stat_val_4.set(randint(3, 18))
    random_stat_val_5.set(randint(3, 18))
    random_stat_val_6.set(randint(3, 18))


#Displays information about chosen race in the information library
def show_race():
##Error Window Change 2 - Opens an error message
    global chosen_race
    chosen_race = race_dropdown_variable.get()
    if chosen_race not in race_dictionary:
        open_error_pop_up()
    else:
        race_information_label.config(text=race_dictionary[chosen_race])


#Displays information about chosen class in the information library
def show_class():
##Error Window Change 1 - Opens an error message
    global chosen_class
    chosen_class = class_dropdown_variable.get()
    if chosen_class not in class_dictionary:
        open_error_pop_up()
    else:
        class_information_label.config(text=class_dictionary[chosen_class])


#Displays the information about the selected race when the user chose waht race they want to play in the character creation menu
##Error Window Change 3 - Opens an error message
def confirm_race_():
    global confirmed_race
    confirmed_race = race_selection_var.get()
    if confirmed_race not in race_walking_speed_dictionary and race_language_dictionary and race_size_dictionary and race_weight_dictionary and race_age_dictionary and race_extra_features_dictionary and race_alignment_dictionary and race_special_ability_dictionary:
        open_error_pop_up()
    else:
        race_walking_speed_display.config(text=race_walking_speed_dictionary[confirmed_race])
        race_language_display.config(text=race_language_dictionary[confirmed_race])
        race_size_display.config(text=race_size_dictionary[confirmed_race])
        race_weight_display.config(text=race_weight_dictionary[confirmed_race])
        race_age_display.config(text=race_age_dictionary[confirmed_race])
        race_extra_features_display.config(text=race_extra_features_dictionary[confirmed_race])
        race_alignment_display.config(text=race_alignment_dictionary[confirmed_race])
        race_special_ability_display.config(text=race_special_ability_dictionary[confirmed_race])
        race_strength_modifier.config(text=race_strength_modifier_dictionary[confirmed_race])
        race_dexterity_modifier.config(text=race_dexterity_modifier_dictionary[confirmed_race])
        race_constitution_modifier.config(text=race_constitution_modifier_dictionary[confirmed_race])
        race_intelligence_modifier.config(text=race_intelligence_modifier_dictionary[confirmed_race])
        race_wisdom_modifier.config(text=race_wisdom_modifier_dictionary[confirmed_race])
        race_charisma_modifier.config(text=race_charisma_modifier_dictionary[confirmed_race])


#Error loading screen
##Error Window Change 1 - Opens an error message
def open_error_pop_up():
    error_pop_up = Toplevel(main_menu)
    error_pop_up.title("Error Occurred")
    error_pop_up.geometry("630x30")
    error_pop_up.config(background="Red")
    error = Label(error_pop_up, text ="There is currently no information regarding your current selection", font="helvetica 14 bold")
    error.config(background="Red")
    error.grid(row=2, column=2)


def save_character(*args):
    global nameing_input, naming_pop_up
    naming_pop_up = Toplevel(main_menu)
    naming_pop_up.title("Name you character")
    naming_pop_up.geometry("630x150")
    nameing_input = Entry(naming_pop_up, font="helvetica 15 bold", width= "50")
    nameing_input.insert(0, "Please name your character: ")
    nameing_input.bind("<Button-1>", temp_text_in_entry_place)
    nameing_input.bind("<Button-3>", temp_text_in_entry_delete)
    nameing_input.grid(row=0, column=1, pady=30, padx=40)
    confirm_save = Button(naming_pop_up, text="Confirm", font="helvetica 10 bold", command=lambda: collecting_entry())
    confirm_save.grid(row=1, column=1)

def temp_text_in_entry_place(*args):
    global nameing_input, naming_pop_up
    nameing_input.delete(0, "end")


def temp_text_in_entry_delete(*args):
    global nameing_input, naming_pop_up
    nameing_input.delete(0, "end")
    nameing_input.insert(0, "Please name your character: ")
    naming_pop_up.focus()


def collecting_entry():
    global  users_correct_input, amount_of_characters, confirmed_race
    users_input = nameing_input.get()
    if users_input == "Please name your character: ":
        error_pop_up = Toplevel(main_menu)
        error_pop_up.title("Error Occurred")
        error_pop_up.geometry("630x30")
        error_pop_up.config(background="Red")
        error = Label(error_pop_up, text="Please name your character", font="helvetica 14 bold")
        error.config(background="Red")
        error.grid(row=2, column=2)
    else:
        amount_of_characters += 1
        users_correct_input = users_input
        if amount_of_characters == 1:
            select_character_1.config(text="1. {}".format(users_correct_input))
            race_walking_speed_1 = race_walking_speed_display.cget("text")
            race_language_1 = race_language_display.cget("text")
            race_size_1 = race_size_display.cget("text")
            race_weight_1 = race_weight_display.cget("text")
            race_age_1 = race_age_display.cget("text")
            race_extra_features_1 = race_extra_features_display.cget("text")
            race_alignment_1 = race_alignment_display.cget("text")
            race_special_ability_1 = race_special_ability_display.cget("text")
            race_strength_modifier_1 = race_strength_modifier.cget("text")
            race_dexterity_modifier_1 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_1 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_1 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_1 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_1 = race_charisma_modifier.cget("text")
            strength_stat_1 = strength_input.get()
            dexterity_stat_1 = dexterity_input.get()
            constitution_stat_1 = constitution_input.get()
            intelligence_stat_1 = intelligence_input.get()
            wisdom_stat_1 = wisdom_input.get()
            charisma_stat_1 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 2:
            select_character_2.config(text="2. {}".format(users_correct_input))
            race_walking_speed_2 = race_walking_speed_display.cget("text")
            race_language_2 = race_language_display.cget("text")
            race_size_2 = race_size_display.cget("text")
            race_weight_2 = race_weight_display.cget("text")
            race_age_2 = race_age_display.cget("text")
            race_extra_features_2 = race_extra_features_display.cget("text")
            race_alignment_2 = race_alignment_display.cget("text")
            race_special_ability_2 = race_special_ability_display.cget("text")
            race_strength_modifier_2 = race_strength_modifier.cget("text")
            race_dexterity_modifier_2 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_2 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_2 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_2 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_2 = race_charisma_modifier.cget("text")
            strength_stat_2 = strength_input.get()
            dexterity_stat_2 = dexterity_input.get()
            constitution_stat_2 = constitution_input.get()
            intelligence_stat_2 = intelligence_input.get()
            wisdom_stat_2 = wisdom_input.get()
            charisma_stat_2 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 3:
            select_character_3.config(text="3. {}".format(users_correct_input))
            race_walking_speed_3 = race_walking_speed_display.cget("text")
            race_language_3 = race_language_display.cget("text")
            race_size_3 = race_size_display.cget("text")
            race_weight_3 = race_weight_display.cget("text")
            race_age_3 = race_age_display.cget("text")
            race_extra_features_3 = race_extra_features_display.cget("text")
            race_alignment_3 = race_alignment_display.cget("text")
            race_special_ability_3 = race_special_ability_display.cget("text")
            race_strength_modifier_3 = race_strength_modifier.cget("text")
            race_dexterity_modifier_3 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_3 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_3 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_3 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_3 = race_charisma_modifier.cget("text")
            strength_stat_3 = strength_input.get()
            dexterity_stat_3 = dexterity_input.get()
            constitution_stat_3 = constitution_input.get()
            intelligence_stat_3 = intelligence_input.get()
            wisdom_stat_3 = wisdom_input.get()
            charisma_stat_3 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 4:
            select_character_4.config(text="4. {}".format(users_correct_input))
            race_walking_speed_4 = race_walking_speed_display.cget("text")
            race_language_4 = race_language_display.cget("text")
            race_size_4 = race_size_display.cget("text")
            race_weight_4 = race_weight_display.cget("text")
            race_age_4 = race_age_display.cget("text")
            race_extra_features_4 = race_extra_features_display.cget("text")
            race_alignment_4 = race_alignment_display.cget("text")
            race_special_ability_4 = race_special_ability_display.cget("text")
            race_strength_modifier_4 = race_strength_modifier.cget("text")
            race_dexterity_modifier_4 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_4 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_4 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_4 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_4 = race_charisma_modifier.cget("text")
            strength_stat_4 = strength_input.get()
            dexterity_stat_4 = dexterity_input.get()
            constitution_stat_4 = constitution_input.get()
            intelligence_stat_4 = intelligence_input.get()
            wisdom_stat_4 = wisdom_input.get()
            charisma_stat_4 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 5:
            select_character_5.config(text="5. {}".format(users_correct_input))
            race_walking_speed_5 = race_walking_speed_display.cget("text")
            race_language_5 = race_language_display.cget("text")
            race_size_5 = race_size_display.cget("text")
            race_weight_5 = race_weight_display.cget("text")
            race_age_5 = race_age_display.cget("text")
            race_extra_features_5 = race_extra_features_display.cget("text")
            race_alignment_5 = race_alignment_display.cget("text")
            race_special_ability_5 = race_special_ability_display.cget("text")
            race_strength_modifier_5 = race_strength_modifier.cget("text")
            race_dexterity_modifier_5 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_5 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_5 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_5 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_5 = race_charisma_modifier.cget("text")
            strength_stat_5 = strength_input.get()
            dexterity_stat_5 = dexterity_input.get()
            constitution_stat_5 = constitution_input.get()
            intelligence_stat_5 = intelligence_input.get()
            wisdom_stat_5 = wisdom_input.get()
            charisma_stat_5 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 6:
            select_character_6.config(text="6. {}".format(users_correct_input))
            race_walking_speed_6 = race_walking_speed_display.cget("text")
            race_language_6 = race_language_display.cget("text")
            race_size_6 = race_size_display.cget("text")
            race_weight_6 = race_weight_display.cget("text")
            race_age_6 = race_age_display.cget("text")
            race_extra_features_6 = race_extra_features_display.cget("text")
            race_alignment_6 = race_alignment_display.cget("text")
            race_special_ability_6 = race_special_ability_display.cget("text")
            race_strength_modifier_6 = race_strength_modifier.cget("text")
            race_dexterity_modifier_6 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_6 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_6 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_6 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_6 = race_charisma_modifier.cget("text")
            strength_stat_6 = strength_input.get()
            dexterity_stat_6 = dexterity_input.get()
            constitution_stat_6 = constitution_input.get()
            intelligence_stat_6 = intelligence_input.get()
            wisdom_stat_6 = wisdom_input.get()
            charisma_stat_6 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 7:
            select_character_7.config(text="7. {}".format(users_correct_input))
            race_walking_speed_7 = race_walking_speed_display.cget("text")
            race_language_7 = race_language_display.cget("text")
            race_size_7 = race_size_display.cget("text")
            race_weight_7 = race_weight_display.cget("text")
            race_age_7 = race_age_display.cget("text")
            race_extra_features_7 = race_extra_features_display.cget("text")
            race_alignment_7 = race_alignment_display.cget("text")
            race_special_ability_7 = race_special_ability_display.cget("text")
            race_strength_modifier_7 = race_strength_modifier.cget("text")
            race_dexterity_modifier_7 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_7 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_7 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_7 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_7 = race_charisma_modifier.cget("text")
            strength_stat_7 = strength_input.get()
            dexterity_stat_7 = dexterity_input.get()
            constitution_stat_7 = constitution_input.get()
            intelligence_stat_7 = intelligence_input.get()
            wisdom_stat_7 = wisdom_input.get()
            charisma_stat_7 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 8:
            select_character_8.config(text="8. {}".format(users_correct_input))
            race_walking_speed_8 = race_walking_speed_display.cget("text")
            race_language_8 = race_language_display.cget("text")
            race_size_8 = race_size_display.cget("text")
            race_weight_8 = race_weight_display.cget("text")
            race_age_8 = race_age_display.cget("text")
            race_extra_features_8 = race_extra_features_display.cget("text")
            race_alignment_8 = race_alignment_display.cget("text")
            race_special_ability_8 = race_special_ability_display.cget("text")
            race_strength_modifier_8 = race_strength_modifier.cget("text")
            race_dexterity_modifier_8 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_8 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_8 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_8 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_8 = race_charisma_modifier.cget("text")
            strength_stat_8 = strength_input.get()
            dexterity_stat_8 = dexterity_input.get()
            constitution_stat_8 = constitution_input.get()
            intelligence_stat_8 = intelligence_input.get()
            wisdom_stat_8 = wisdom_input.get()
            charisma_stat_8 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 9:
            select_character_9.config(text="9. {}".format(users_correct_input))
            race_walking_speed_9 = race_walking_speed_display.cget("text")
            race_language_9 = race_language_display.cget("text")
            race_size_9 = race_size_display.cget("text")
            race_weight_9 = race_weight_display.cget("text")
            race_age_9 = race_age_display.cget("text")
            race_extra_features_9 = race_extra_features_display.cget("text")
            race_alignment_9 = race_alignment_display.cget("text")
            race_special_ability_9 = race_special_ability_display.cget("text")
            race_strength_modifier_9 = race_strength_modifier.cget("text")
            race_dexterity_modifier_9 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_9 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_9 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_9 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_9 = race_charisma_modifier.cget("text")
            strength_stat_9 = strength_input.get()
            dexterity_stat_9 = dexterity_input.get()
            constitution_stat_9 = constitution_input.get()
            intelligence_stat_9 = intelligence_input.get()
            wisdom_stat_9 = wisdom_input.get()
            charisma_stat_9 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters == 10:
            select_character_10.config(text="10. {}".format(users_correct_input))
            race_walking_speed_10 = race_walking_speed_display.cget("text")
            race_language_10 = race_language_display.cget("text")
            race_size_10 = race_size_display.cget("text")
            race_weight_10 = race_weight_display.cget("text")
            race_age_10 = race_age_display.cget("text")
            race_extra_features_10 = race_extra_features_display.cget("text")
            race_alignment_10 = race_alignment_display.cget("text")
            race_special_ability_10 = race_special_ability_display.cget("text")
            race_strength_modifier_10 = race_strength_modifier.cget("text")
            race_dexterity_modifier_10 = race_dexterity_modifier.cget("text")
            race_constitution_modifier_10 = race_constitution_modifier.cget("text")
            race_intelligence_modifier_10 = race_intelligence_modifier.cget("text")
            race_wisdom_modifier_10 = race_wisdom_modifier.cget("text")
            race_charisma_modifier_10 = race_charisma_modifier.cget("text")
            strength_stat_10 = strength_input.get()
            dexterity_stat_10 = dexterity_input.get()
            constitution_stat_10 = constitution_input.get()
            intelligence_stat_10 = intelligence_input.get()
            wisdom_stat_10 = wisdom_input.get()
            charisma_stat_10 = charisma_input.get()
            naming_pop_up.destroy()
        elif amount_of_characters > 10:
            error_pop_up = Toplevel(main_menu)
            error_pop_up.title("Error Occurred")
            error_pop_up.geometry("630x60")
            error_pop_up.config(background="Red")
            error = Label(error_pop_up, text="You have reached the max of ten characters, if you wish to countiue\n you must delete a character", font="helvetica 14 bold")
            error.config(background="Red")
            error.grid(row=2, column=2)


def open_or_delete_character():
    open_or_delete = Toplevel(main_menu)
    open_or_delete.title("Open/Delete")
    open_or_delete.geometry("370x60")
    open_or_delete.config(background="white")
    open = Button(open_or_delete, text="OPEN", font="helvetica 14 bold")
    open.config(background="green")
    open.grid(row=1, column=1, padx=50, pady=10)
    delete = Button(open_or_delete, text="DELETE", font="helvetica 14 bold")
    delete.config(background="red")
    delete.grid(row=1, column=2, padx=50)



# Main Menu Widgets Creation
menu_name = Label(main_menu_frame, text="Dungeons & Dragons", font="helvetica 50 bold")
menu_sub_name = Label(main_menu_frame, text="Character Creator", font="helvetica 25 bold")
create_character_button = Button(main_menu_frame, text="CREATE A CHARACTER", font="helvetica 30 bold",
                                 command=lambda: open_character_creation())
information_library_button = Button(main_menu_frame, text="INFORMATION LIBRARY", font="helvetica 30 bold",
                                    command=lambda: open_information_library())
load_character_button = Button(main_menu_frame, text="LOAD CHARACTER", font="helvetica 30 bold",
                               command=lambda: open_load_character())
quit_button = Button(main_menu_frame, text="QUIT", font="helvetica 30 bold",
                     command=lambda: quit_program())


# Load Character Menu Widgets Creation
back_button_lc = Button(load_character_frame, text="Back", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())
select_character_1 = Button(load_character_frame, text="1.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_2 = Button(load_character_frame, text="2.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_3 = Button(load_character_frame, text="3.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_4 = Button(load_character_frame, text="4.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_5 = Button(load_character_frame, text="5.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_6 = Button(load_character_frame, text="6.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_7 = Button(load_character_frame, text="7.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_8 = Button(load_character_frame, text="8.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_9 = Button(load_character_frame, text="9.", font="helvetica 20 bold", command=lambda: open_or_delete_character())
select_character_10 = Button(load_character_frame, text="10.", font="helvetica 20 bold", command=lambda: open_or_delete_character())

# Load Character Menu Widgets Placement
back_button_lc.grid(row=0, column=0)
select_character_1.grid(row=1, column=1, padx=150, sticky="w")
select_character_2.grid(row=1, column=2, padx=150, sticky="w")
select_character_3.grid(row=1, column=3, padx=150, sticky="w")
select_character_4.grid(row=1, column=4, padx=150, sticky="w")
select_character_5.grid(row=1, column=5, padx=150, pady=200, sticky="w")
select_character_6.grid(row=2, column=1, padx=150, sticky="w")
select_character_7.grid(row=2, column=2, padx=150, sticky="w")
select_character_8.grid(row=2, column=3, padx=150, sticky="w")
select_character_9.grid(row=2, column=4, padx=150, sticky="w")
select_character_10.grid(row=2, column=5, padx=150, pady=200, sticky="w")

## Information Library Menu Widgets Creation
#Line 138 - 178 Brief information that will be displayed in relation to races and the conformation button
#line 181 - 216 Brief information that will be displayed in relation to class and the conformation button
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
## Information Library Change 1 - Increased font size
race_information_label = Label(information_library_frame, text="Race is a rule in Dungeons & Dragons referring to the fantasy species or ancestry of a character.\n "
                            "Popular races include human, elf, dwarf and halfling. Unlike the modern real-world use of the\n"
                            "word, 'race' in Dungeons & Dragons does not refer to a character's ethnic background.", font="helvetica 12")

back_button_il = Button(information_library_frame, text="BACK", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())
information_of_race = OptionMenu(information_library_frame, race_dropdown_variable, "Races", "Aarakocra", "Aasimar", "Bugbear", "Centaur", "Changeling", "Dragonborn", "Dwarf", \
                                 "Elf", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Grung", "Half-Elf", "Halfling", "Half-Orc", "Hobgoblin", "Human", "Kalashtar", \
                                 "Kenku", "Kobold", "Lizardfolk", "Locathah", "Loxodon", "Minotaur", "Orc", "Simic Hybrid", "Shifter", "Tabaxi", "Tiefling", "Tortle", "Triton", \
                                 "Veldalken", "Verdan", "Warforged", "Yuan-Ti Pureblood")
information_of_race.configure(font="helvetica 23 bold")
confirm_class_button = Button(information_library_frame, text="Find Info About The Class", font="helvetica 8", command=lambda: show_class())
## Information Library Change 1 - Increased font size
class_information_label = Label(information_library_frame, text="Your class is the primary definition of what your character can do in the extraordinary magical\n"
                               "landscape of Dungeons & Dragons. A class is more than a profession; it is your character’s calling.", font="helvetica 12")
class_dropdown_variable = StringVar()
class_dropdown_variable.set("Classes")
information_of_class = OptionMenu(information_library_frame, class_dropdown_variable, "Classes", "Artificer", "Barbarian", "Bard", "Cleric", "Druid"\
                                  , "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")
information_of_class.configure(font="helvetica 23 bold")
class_dictionary = {"Classes": "Your class is the primary definition of what your character can do in the extraordinary magical\n"
                               "landscape of Dungeons & Dragons. A class is more than a profession; it is your character’s calling."
                    ,"Artificer": "Makers of magic-infused objects, artificers are defined by their inventive nature. They see magic\n" 
                                 "as a complex system waiting to be decoded and controlled. Instead of ephemeral spells, they seek \n"
                                 "to craft durable, useful, marvelous magical items.",
                    "Barbarian": "For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling\n"
                                 "reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just \n"
                                 " a battle frenzy but also uncanny reflexes, resilience, and feats of strength.",
                    "Bard": "Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize\n"
                            "foes, manipulate minds, create illusions, and even heal wounds. The bard is a master of song, speech, and the \n"
                            "magic they contain.",
                    "Cleric":"Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods\n"
                             " they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued\n"
                             " with divine magic.",
                    "Druid": "Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are\n"
                              " an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves\n"
                              " as extensions of nature's indomitable will.",
                    "Fighter": "Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat.\n"
                               " They are well acquainted with death, both meting it out and staring it defiantly in the face.",
                    "Monk": "Monks are united in their ability to magically harness the energy that flows in their bodies. Whether channeled as a\n"
                            " striking display of combat prowess or a subtler focus of defensive ability and speed, this energy infuses all that a \n"
                            "monk does."}
heading_information = Label(information_library_frame, text="Information Library", font="helvetica 30 bold")


## Character Creation Menu Widgets Creation
#Line 225 - 238 Logic for the random stat roller
#Line 240 - 252 Creation of where the user can inpout there selected stats
#Line 256 - 314 Dictionarys and labels for the race dependent statisstic/skills
back_button_cc = Button(character_creation_frame, text="BACK", font="helvetica 20 bold",
                        command=lambda: back_to_main_menu())
random_stat_button = Button(character_creation_frame, text="Roll Your Random Stat",
                            command=lambda: random_stat_roll())
random_stat_val_1 = IntVar()
random_stat_val_2 = IntVar()
random_stat_val_3 = IntVar()
random_stat_val_4 = IntVar()
random_stat_val_5 = IntVar()
random_stat_val_6 = IntVar()
random_stat_label_1 = Label(character_creation_frame, textvariable=random_stat_val_1, font="helvetica 15 bold")
random_stat_label_2 = Label(character_creation_frame, textvariable=random_stat_val_2, font="helvetica 15 bold")
random_stat_label_3 = Label(character_creation_frame, textvariable=random_stat_val_3, font="helvetica 15 bold")
random_stat_label_4 = Label(character_creation_frame, textvariable=random_stat_val_4, font="helvetica 15 bold")
random_stat_label_5 = Label(character_creation_frame, textvariable=random_stat_val_5, font="helvetica 15 bold")
random_stat_label_6 = Label(character_creation_frame, textvariable=random_stat_val_6, font="helvetica 15 bold")

strength_stat_label_1 = Label(character_creation_frame, text="STR", font="helvetica 20 bold")
dexterity_stat_label_2 = Label(character_creation_frame, text="DEX", font="helvetica 20 bold")
constitution_stat_label_3 = Label(character_creation_frame, text="CON", font="helvetica 20 bold")
intelligence_stat_label_4 = Label(character_creation_frame, text="INT", font="helvetica 20 bold")
wisdom_stat_label_5 = Label(character_creation_frame, text="WIS", font="helvetica 20 bold")
charisma_stat_label_6 = Label(character_creation_frame, text="CHA", font="helvetica 20 bold")
strength_input = Entry(character_creation_frame, width=3, font="helvetica 15 bold")
dexterity_input = Entry(character_creation_frame, width=3, font="helvetica 15 bold")
constitution_input = Entry(character_creation_frame, width=3, font="helvetica 15 bold")
intelligence_input = Entry(character_creation_frame, width=3, font="helvetica 15 bold")
wisdom_input = Entry(character_creation_frame, width=3, font="helvetica 15 bold")
charisma_input = Entry(character_creation_frame, width=3, font="helvetica 15 bold")

confirm_button = Button(character_creation_frame, text="Confirm", font="helvetica 13 bold", command= lambda: confirm_race_())

race_selection_var = StringVar()
class_selection_var = StringVar()
class_selection_var.set("Class")
race_selection_var.set("Race")
race_selection = OptionMenu(character_creation_frame, race_selection_var, "Aarakocra", "Aasimar", "Bugbear", "Centaur", "Changeling", "Dragonborn", "Dwarf", \
                                 "Elf", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Grung", "Half-Elf", "Halfling", "Half-Orc", "Hobgoblin", "Human", "Kalashtar", \
                                 "Kenku", "Kobold", "Lizardfolk", "Locathah", "Loxodon", "Minotaur", "Orc", "Simic Hybrid", "Shifter", "Tabaxi", "Tiefling", "Tortle", "Triton", \
                                 "Veldalken", "Verdan", "Warforged", "Yuan-Ti Pureblood")
race_walking_speed_dictionary = {"Aarakocra": "25", "Aasimar": "30", "Bugbear": "30", "Centaur": "40" ,"Changeling": "30", "Dragonborn": "30", "Dwarf": "25",\
                                 "Elf": "30", "Firbolg": "30", "Genasi": "35", "Gith": "30", "Gnome": "25", "Goblin": "30", "Goliath": "30", "Grung": "25", "Half-Elf": "30", "Halfling": "25", "Half-Orc": "30", "Hobgoblin": "30", "Human": "30", "Kalashtar": "30", \
                                 "Kenku": "30", "Kobold": "30", "Lizardfolk": "30", "Locathah": "30", "Loxodon": "30", "Minotaur": "30", "Orc": "30", "Simic Hybrid": "30", "Shifter": "30", "Tabaxi": "30", "Tiefling": "30", "Tortle": "30", "Triton": "30", \
                                 "Veldalken": "30", "Verdan": "30", "Warforged": "30"}
race_language_dictionary = {"Aarakocra": "Aarakocran, Auran, Common", "Aasimar": "Common, celestial + one of Draconic, Dwarven, Elven, Gnome, Halfing, Sylvan", "Bugbear" : "Common, Goblin", "Centaur" : "Common, Sylvan",\
                            "Changeling" : "Common + any two languages"}
race_size_dictionary = {"Aarakocra": "5-6 feet", "Aasimar": "5-6 feet", "Bugbear": "6-8 feet", "Centaur": "6-7 feet" ,"Changeling": "5-6 feet", "Dragonborn": "6-7 feet", "Dwarf": "4-5 feet",\
                                 "Elf": "30", "Firbolg": "30", "Genasi": "35", "Gith": "30", "Gnome": "25", "Goblin": "30", "Goliath": "30", "Grung": "25", "Half-Elf": "30", "Halfling": "25", "Half-Orc": "30", "Hobgoblin": "30", "Human": "30", "Kalashtar": "30", \
                                 "Kenku": "30", "Kobold": "30", "Lizardfolk": "30", "Locathah": "30", "Loxodon": "30", "Minotaur": "30", "Orc": "30", "Simic Hybrid": "30", "Shifter": "30", "Tabaxi": "30", "Tiefling": "30", "Tortle": "30", "Triton": "30", \
                                 "Veldalken": "30", "Verdan": "30", "Warforged": "30", }
race_weight_dictionary = {"Aarakocra": "80-100 pounds", "Aasimar" : "89-245lb", "Bugbear" : "250-350 lb", "Centaur" :  "2,100 lb", "Changeling" : "60-500lb"}
race_age_dictionary = {"Aarakocra": "Mature: 3 Average: 30", "Aasimar": "Mature: 20 Average: 160"}
race_extra_features_dictionary = {"Aarakocra": "Flight: 50 feet, Talons: Proficient with your unarmed strikes (1d4 slashing)", "Aasimar": "Darkvision 60ft"}
race_alignment_dictionary = {"Aarakocra": "Tend to be good", "Aasimar": "Tend to be good"}
race_special_ability_dictionary = {"Aarakocra": "None", "Aasimar": "Celestial Resistance: Resistance to necrotic damage and radiant damage,\n"
                                                               "Healing Hands: Action, touched creature regains hit points equal to your level. Once every long rest\n"
                                                               "Light Bearer: You know the Light cantrip. Charisma is your spellcasting ability for it"}


race_walking_speed_display = Label(character_creation_frame, text="0", font="helvetica 15")
race_language_display = Label(character_creation_frame, text="none", font="helvetica 15")
race_size_display = Label(character_creation_frame, text="0", font="helvetica 15")
race_weight_display = Label(character_creation_frame, text="0", font="helvetica 15")
race_age_display = Label(character_creation_frame, text="0", font="helvetica 15")
race_extra_features_display = Label(character_creation_frame, text="none", font="helvetica 15")
race_alignment_display = Label(character_creation_frame, text="none", font="helvetica 15")
race_special_ability_display = Label(character_creation_frame, text="none", font="helvetica 15")
walking_speed_label = Label(character_creation_frame, text="Walking Speed", font="helvetica 20 bold")
language_label = Label(character_creation_frame, text="Language(s)", font="helvetica 20 bold")
size_label = Label(character_creation_frame, text="Size", font="helvetica 20 bold")
weight_label = Label(character_creation_frame, text="Weight", font="helvetica 20 bold")
age_label = Label(character_creation_frame, text="Age", font="helvetica 20 bold")
extra_features_label = Label(character_creation_frame, text="Extra Features", font="helvetica 20 bold")
alignment_label = Label(character_creation_frame, text="Alignment", font="helvetica 20 bold")
special_ability_label = Label(character_creation_frame, text="Special Ability", font="helvetica 20 bold")

race_strength_modifier = Label(character_creation_frame, text="0", font="helvetica 15 bold")
race_dexterity_modifier = Label(character_creation_frame, text="0", font="helvetica 15 bold")
race_constitution_modifier = Label(character_creation_frame, text="0", font="helvetica 15 bold")
race_intelligence_modifier = Label(character_creation_frame, text="0", font="helvetica 15 bold")
race_wisdom_modifier = Label(character_creation_frame, text="0", font="helvetica 15 bold")
race_charisma_modifier = Label(character_creation_frame, text="0", font="helvetica 15 bold")

race_strength_modifier_dictionary = {"Aarakocra": "0", "Aasimar": "0"}
race_dexterity_modifier_dictionary = {"Aarakocra": "+2", "Aasimar": "0"}
race_constitution_modifier_dictionary = {"Aarakocra": "0", "Aasimar": "0"}
race_intelligence_modifier_dictionary = {"Aarakocra": "0", "Aasimar": "0"}
race_wisdom_modifier_dictionary = {"Aarakocra": "+1", "Aasimar": "0"}
race_charisma_modifier_dictionary = {"Aarakocra": "0", "Aasimar": "+2"}

race_selection.config(font="helvetica 15 bold")

class_selection_var = StringVar()
class_selection_var.set("Class")
class_selection = OptionMenu(character_creation_frame, class_selection_var, "Artificer", "Barbarian", "Bard", "Cleric", "Druid"\
                                  , "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")
class_selection.config(font="helvetica 15 bold")
save_character_button = Button(character_creation_frame, text="SAVE", font="helvetica 20 bold", command=lambda: save_character())

## Information Library Menu Widgets Placement
## Information Library Change 2 - Changed placement of widgets to create ideal asethetics
back_button_il.grid(row=0, column=0)
information_of_race.grid(row=3, column=1)
race_information_label.grid(row=5, column=1, sticky="N", pady=25)
confirm_race_button.grid(row=4, column=1)
information_of_class.grid(row=3, column=3)
class_information_label.grid(row=5, column=3, sticky="N", pady=25)
confirm_class_button.grid(row=4, column=3)
heading_information.grid(row=2, column=2, sticky="N", pady=25)

# Character Creation Menu Widgets Placement
back_button_cc.grid(row=0, column=0, sticky="w")
random_stat_button.grid(row=16, column=0, sticky="w")
random_stat_label_1.grid(row=3, column=0, pady=5, padx=15, sticky="w")
random_stat_label_2.grid(row=4, column=0, pady=5, padx=15, sticky="w")
random_stat_label_3.grid(row=5, column=0, pady=5, padx=15, sticky="w")
random_stat_label_4.grid(row=6, column=0, pady=5, padx=15, sticky="w")
random_stat_label_5.grid(row=7, column=0, pady=5, padx=15, sticky="w")
random_stat_label_6.grid(row=8, column=0, pady=5, padx=15, sticky="w")
strength_stat_label_1.grid(row=4, column=2, sticky="w")
dexterity_stat_label_2.grid(row=6, column=2, sticky="w")
constitution_stat_label_3.grid(row=8, column=2, sticky="w")
intelligence_stat_label_4.grid(row=10, column=2, sticky="w")
wisdom_stat_label_5.grid(row=12, column=2, sticky="w")
charisma_stat_label_6.grid(row=14, column=2, sticky="w")
strength_input.grid(row=3, column=2, sticky="w")
dexterity_input.grid(row=5, column=2, sticky="w")
constitution_input.grid(row=7, column=2, sticky="w")
intelligence_input.grid(row=9, column=2, sticky="w")
wisdom_input.grid(row=11, column=2, sticky="w")
charisma_input.grid(row=13, column=2, sticky="w")
race_selection.grid(row=2, column=3, sticky="w")
class_selection.grid(row=2, column=4, sticky="w")
confirm_button.grid(row=2, column=5, sticky="w")
race_walking_speed_display.grid(row=4, column=6, sticky="w", pady=10)
race_language_display.grid(row=5, column=6, sticky="w", pady=10)
race_size_display.grid(row=6, column=6, sticky="w", pady=10)
race_weight_display.grid(row=7, column=6, sticky="w", pady=10)
race_age_display.grid(row=8, column=6, sticky="w", pady=10)
race_extra_features_display.grid(row=9, column=6, sticky="w", pady=10)
race_alignment_display.grid(row=10, column=6, sticky="w", pady=10)
race_special_ability_display.grid(row=11, column=6, sticky="w", pady=10)
walking_speed_label.grid(row=4, column=5, sticky="w", pady=10)
language_label.grid(row=5, column=5, sticky="w", pady=10)
size_label.grid(row=6, column=5, sticky="w", pady=10)
weight_label.grid(row=7, column=5, sticky="w", pady=10)
age_label.grid(row=8, column=5, sticky="w", pady=10)
extra_features_label.grid(row=9, column=5, sticky="w", pady=10)
alignment_label.grid(row=10, column=5, sticky="w", pady=10)
special_ability_label.grid(row=11, column=5, sticky="w", pady=10)
race_strength_modifier.grid(row=10, column=0, pady=10, padx=15, sticky="w")
race_dexterity_modifier.grid(row=11, column=0, pady=10, padx=15, sticky="w")
race_constitution_modifier.grid(row=12, column=0, pady=10, padx=15, sticky="w")
race_intelligence_modifier.grid(row=13, column=0, pady=10, padx=15, sticky="w")
race_wisdom_modifier.grid(row=14, column=0, pady=10, padx=15, sticky="w")
race_charisma_modifier.grid(row=15, column=0, pady=10, padx=15, sticky="w")
save_character_button.grid(row=0, column=1)

# Main Menu Widgets Placement
## Main Menu Changes 1 - Changed placement of widgets to create ideal asethetics
menu_name.grid(row=0, column=2, padx=125, pady=15)
menu_sub_name.grid(row=1, column=2)
create_character_button.grid(row=2, column=2, pady=300)
information_library_button.grid(row=2, column=1, padx=15)
load_character_button.grid(row=2, column=3, padx=15)
quit_button.grid(row=3, column=2,)

main_menu.mainloop()
