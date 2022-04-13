from dcc_character import *

from tkinter import *
from tkinter import font
from tkinter.ttk import *

generated_character_list = []

dcc_file = "DCC 0-Level Characters.txt"

# region GUI_ELEMENTS

tk_root = Tk()
frm_main_buttons = Frame(master=tk_root)
frm_character_buttons = Frame(master=frm_main_buttons)
ui_font = font.Font(family="Sylfaen")

info_label_list = []

# endregion


# region CHARACTER_FILE_CALLBACKS

def generate_character(char_file, name_id):
    char_name = "Character #" + str(name_id)
    new_character = CharacterSheet(char_name, True, "")
    
    char_file.write(new_character.get_character_details())

    print(f"{new_character.name} successfully generated!")

    return new_character


def read_generated_characters():
    is_empty = False

    try:
        character_file = open(dcc_file, 'r')

    except FileNotFoundError:
        open(dcc_file, 'x')
        is_empty = True
        character_file = open(dcc_file, 'r')

    if not is_empty:
        existing_characters = character_file.readlines()
        convert_character_file(existing_characters)

    character_file.close()


def convert_character_file(lines):
    line_index = 1
    full_character_list = []

    for i in range(20):
        new_character_list = []

        read_lines = True

        while read_lines:
            if line_index > len(lines) - 1 or lines[line_index] == "\n":
                read_lines = False

            else:
                new_character_list.append(lines[line_index])

            line_index += 1

        full_character_list.append(new_character_list)

    for i in full_character_list:
        generated_character_list.append(CharacterSheet('', False, i))

# endregion


# region UI_CALLBACKS

def create_gui():
    tk_root.geometry('880x470')
    tk_root.minsize(width=880, height=470)
    tk_root.maxsize(width=880, height=470)
    tk_root.title("DCC Character Generator")

    create_buttons_frame()
    create_info_frame()


def create_buttons_frame():
    frm_options_buttons = Frame(master=frm_main_buttons)
    gen = Button(master=frm_options_buttons, text="Generate All", command=on_button_generate)
    quit_btn = Button(master=frm_options_buttons, text="Exit", command=tk_root.destroy)

    frm_main_buttons.grid(row=0, column=0, padx=5, pady=5)
    frm_character_buttons.pack(padx=5, pady=5)
    frm_options_buttons.pack(padx=5, pady=5)
    gen.pack(padx=5, pady=5)
    quit_btn.pack(padx=5, pady=5)


def create_info_frame():
    frm_main_info = Frame(master=tk_root, relief=RIDGE, padding=10)

    lbl_name_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Name:"
    )
    lbl_hp_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="HP:"
    )
    lbl_occupation_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Occupation:"
    )
    lbl_alignment_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Alignment:"
    )
    lbl_strength_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Strength",
        background="black",
        foreground="white"
    )
    lbl_agility_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Agility",
        background="black",
        foreground="white"
    )
    lbl_stamina_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Stamina",
        background="black",
        foreground="white"
    )
    lbl_personality_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Personality",
        background="black",
        foreground="white"
    )
    lbl_intelligence_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Intelligence",
        background="black",
        foreground="white"
    )
    lbl_luck_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Luck",
        background="black",
        foreground="white"
    )
    lbl_lucky_roll_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Lucky Roll:"
    )
    lbl_weapon_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Weapon:"
    )
    lbl_equipment_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Equipment:"
    )
    lbl_trade_goods_title = Label(
        master=frm_main_info,
        font=ui_font,
        text="Trade Goods:"
    )

    lbl_name = Label(master=frm_main_info, text="", relief=SUNKEN, width=30)
    lbl_hp = Label(master=frm_main_info, text="", width=6)
    lbl_occupation = Label(master=frm_main_info, text="", relief=SUNKEN, width=30)
    lbl_alignment = Label(master=frm_main_info, text="", relief=SUNKEN, width=30)
    lbl_strength = Label(master=frm_main_info, text="", relief=SUNKEN, width=6)
    lbl_strength_mod = Label(master=frm_main_info, text="")
    lbl_agility = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_agility_mod = Label(master=frm_main_info, text="")
    lbl_stamina = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_stamina_mod = Label(master=frm_main_info, text="")
    lbl_personality = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_personality_mod = Label(master=frm_main_info, text="")
    lbl_intelligence = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_intelligence_mod = Label(master=frm_main_info, text="")
    lbl_luck = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_luck_mod = Label(master=frm_main_info, text="")
    lbl_lucky_roll = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_weapon = Label(master=frm_main_info, text="", relief=SUNKEN, width=25)
    lbl_equipment = Label(master=frm_main_info, text="", relief=SUNKEN)
    lbl_trade_goods = Label(master=frm_main_info, text="", relief=SUNKEN)

    info_label_list.append(lbl_name)
    info_label_list.append(lbl_hp)
    info_label_list.append(lbl_occupation)
    info_label_list.append(lbl_alignment)
    info_label_list.append(lbl_strength)
    info_label_list.append(lbl_strength_mod)
    info_label_list.append(lbl_agility)
    info_label_list.append(lbl_agility_mod)
    info_label_list.append(lbl_stamina)
    info_label_list.append(lbl_stamina_mod)
    info_label_list.append(lbl_personality)
    info_label_list.append(lbl_personality_mod)
    info_label_list.append(lbl_intelligence)
    info_label_list.append(lbl_intelligence_mod)
    info_label_list.append(lbl_luck)
    info_label_list.append(lbl_luck_mod)
    info_label_list.append(lbl_lucky_roll)
    info_label_list.append(lbl_weapon)
    info_label_list.append(lbl_equipment)
    info_label_list.append(lbl_trade_goods)

    frm_main_info.grid(row=0, column=1)

    lbl_name_title.grid(row=0, column=0, sticky="nsew")
    lbl_hp_title.grid(row=4, column=8, columnspan=2, sticky="nsew")
    lbl_occupation_title.grid(row=2, column=0, columnspan=2, sticky="nsew")
    lbl_alignment_title.grid(row=2, column=7, columnspan=2, sticky="nsew")
    lbl_strength_title.grid(row=5, column=0, columnspan=2, sticky="nsew")
    lbl_agility_title.grid(row=7, column=0, columnspan=2, sticky="nsew")
    lbl_stamina_title.grid(row=9, column=0, columnspan=2, sticky="nsew")
    lbl_personality_title.grid(row=11, column=0, columnspan=2, sticky="nsew")
    lbl_intelligence_title.grid(row=13, column=0, columnspan=2, sticky="nsew")
    lbl_luck_title.grid(row=15, column=0, columnspan=2, sticky="nsew")
    lbl_lucky_roll_title.grid(row=17, column=0, columnspan=2, sticky="nsew")
    lbl_weapon_title.grid(row=11, column=8, columnspan=2, sticky="nsew")
    lbl_equipment_title.grid(row=13, column=5, columnspan=2, sticky="nsew")
    lbl_trade_goods_title.grid(row=15, column=5, columnspan=2, sticky="nsew")

    lbl_name.grid(row=1, column=0, columnspan=6, sticky="nsew")
    lbl_hp.grid(row=5, column=8, columnspan=2, rowspan=2)
    lbl_occupation.grid(row=3, column=0, columnspan=6, sticky="nsew")
    lbl_alignment.grid(row=3, column=7, columnspan=2, sticky="nsew")
    lbl_strength.grid(row=5, column=2, columnspan=2, rowspan=2, sticky="nsew")
    lbl_strength_mod.grid(row=6, column=0, columnspan=2)
    lbl_agility.grid(row=7, column=2, columnspan=2, rowspan=2, sticky="nsew")
    lbl_agility_mod.grid(row=8, column=0, columnspan=2)
    lbl_stamina.grid(row=9, column=2, columnspan=2, rowspan=2, sticky="nsew")
    lbl_stamina_mod.grid(row=10, column=0, columnspan=2)
    lbl_personality.grid(row=11, column=2, columnspan=2, rowspan=2, sticky="nsew")
    lbl_personality_mod.grid(row=12, column=0, columnspan=2)
    lbl_intelligence.grid(row=13, column=2, columnspan=2, rowspan=2, sticky="nsew")
    lbl_intelligence_mod.grid(row=14, column=0, columnspan=2)
    lbl_luck.grid(row=15, column=2, columnspan=2, rowspan=2, sticky="nsew")
    lbl_luck_mod.grid(row=16, column=0, columnspan=2)
    lbl_lucky_roll.grid(row=18, column=0, columnspan=13, sticky="nsew")
    lbl_weapon.grid(row=12, column=8, columnspan=5, sticky="nsew")
    lbl_equipment.grid(row=14, column=5, columnspan=8, sticky="nsew")
    lbl_trade_goods.grid(row=16, column=5, columnspan=8, sticky="nsew")


def display_character_buttons():
    index = 1

    for i in range(4):
        frm_character_buttons.columnconfigure(i, weight=1, minsize=50)
        frm_character_buttons.rowconfigure(i, weight=1, minsize=20)

        for j in range(5):
            new_button = Button(
                master=frm_character_buttons,
                text=f"# {index}",
                command=lambda index=index: on_button_character(index)
            )

            new_button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
            index += 1


def on_button_generate():
    character_file = open(dcc_file, 'a')
    character_file.truncate(0)
    generated_character_list.clear()

    for i in range(1, 21):
        generated_character_list.append(generate_character(character_file, i))

    character_file.close()

    display_character_buttons()
    clear_character_sheet()


def on_button_character(character_number):
    for i in range(20):
        info_label_list[i]["text"] = generated_character_list[character_number - 1].get_character_info(i)


def clear_character_sheet():
    for i in range(20):
        info_label_list[i]["text"] = ""

# endregion


# region MAIN

def start_generator():
    print(f"\n\n{separator}")
    print("\n" + "Dungeon Crawl Classics".center(80))
    print("0-Level Character Creator".center(80))
    print(f"\n{separator}")

    read_generated_characters()

    if generated_character_list:
        display_character_buttons()

    create_gui()
    mainloop()

# endregion


# region MAIN_THREAD

start_generator()

print(f"\n{separator}")
print("\n" + "Thank you for playing!".center(80))
print("Good luck with the funneling!".center(80) + "\n")
print(f"{separator}\n")

# endregion
