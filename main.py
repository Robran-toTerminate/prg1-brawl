import random

class STADS_TYPER():
    TOM = 0
    FABRIK = 1
    MORTAR = 2

    RUIN = -1
class Stad():
    def __init__(self, visas:bool):
        self.stads_typ = STADS_TYPER.TOM
        self.hp = 10
        self.visas = visas

class SIDE_PANEL_STATE():
    IDLE = 0
    SELECTION = 1
    BUILD = 2
side_panel_state = SIDE_PANEL_STATE.IDLE

antal_fiendestäder = 1
städer = [Stad(False),Stad(True), Stad(True)]

spelare_pengar = 100
fiende_pengar = 100

spelare_attackstyrka = 2
fiende_attackstyrka = 1


selected_city = 0
selected_action = 0

sp_friendly_actions = ["BUILD", "PROPAGANDA", "RETURN"]
sp_enemie_actions   = ["ATTACK", "SPY", "RETURN"]

build_options = ["BUILD FACTORY", "BUILD MORTAR", "RETURN"]

def get_city_ascii(stad): #Byt ut mot asciin
    if stad.visas != True:
        return "HID"

    match stad.stads_typ:
        case STADS_TYPER.TOM:
            return "TOM"
        case STADS_TYPER.FABRIK:
            return "FAB"
        case STADS_TYPER.MORTAR:
            return "MOR"
        case STADS_TYPER.RUIN:
            return "RUI"
def s(stad): #Dåligt namn men de ä ba för att show_scene ska va läsbart
    ascii = get_city_ascii(städer[stad])
    if stad == selected_city:
        return f"[{ascii}] "
    else:
        return f" {ascii}  "

def panel_option(line):
    sc_status_friend = selected_city>antal_fiendestäder-1

    try:
        if side_panel_state == SIDE_PANEL_STATE.SELECTION:
            if sc_status_friend:
                return sp_friendly_actions[line]
            else:
                return sp_enemie_actions[line]
        else:
            return build_options[line]
    except IndexError:
        return ""
def p_o(line):
    global selected_action
    option = panel_option(line)

    if line == selected_action:
        return f"{option} <---"
    else:
        return f"{option}"


def side_panel(line):
    global side_panel_state

    if side_panel_state != SIDE_PANEL_STATE.IDLE:
        match line:
            case 0: return f"|               |"
            case 1: return f"|               |"
            case 2: return f"|{p_o(0)}        "
            case 3: return f"|{p_o(1)}        "
            case 4: return f"|{p_o(2)}        "
            case 5: return f"|               |"
            case 6: return f"|               |"

    else:
        match line:
            case 0: return f"|               |"
            case 1: return f"|               |"
            case 2: return f"|                "
            case 3: return f"|                "
            case 4: return f"|                "
            case 5: return f"|               |"
            case 6: return f"|               |"
def show_scene():
    print(f'''
                        {side_panel(0)}
    {s(0)}              {side_panel(1)}
                {s(1)}  {side_panel(2)}
             {s(2)}     {side_panel(3)}
                        {side_panel(4)}
''')


def handle_input():
    global selected_city, selected_action, side_panel_state
    print(selected_action)
    command = input("").lower()

    match command:
        case "w":
            if side_panel_state == SIDE_PANEL_STATE.IDLE:
                selected_city -=1
            else:
                selected_action -=1
        case "s":
            if side_panel_state == SIDE_PANEL_STATE.IDLE:
                selected_city +=1
            else:
                selected_action +=1

        case "":
            if side_panel_state == SIDE_PANEL_STATE.IDLE:
                side_panel_state = SIDE_PANEL_STATE.SELECTION
            else:
                if panel_option(selected_action) == "RETURN":
                    side_panel_state = SIDE_PANEL_STATE.IDLE
                    selected_action = 0
                else:
                    if panel_option(selected_action) == "BUILD":
                        side_panel_state = SIDE_PANEL_STATE.BUILD
                    else:
                        print(selected_city, panel_option(selected_action))
                        quit()

    if selected_city > len(städer)-1:
        selected_city = len(städer)-1
    elif selected_city < 0:
        selected_city = 0
    if selected_action > 2: #3 actions minus 1
        selected_action = 2
    elif selected_action < 0:
        selected_action = 0            



while True:
    print("\033c",end="")
    show_scene()
    handle_input()
