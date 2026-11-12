import random

class GAME_STAGES():
    PLAYER_TURN = 0
    ENEMIE_TURN = 1
    UPKEEP = 2

    PLAYER_WIN = 3
    PLAYER_LOSS = 4
game_stage = GAME_STAGES.PLAYER_TURN

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


enemie_last_action = ""

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
def p_o(line): #Se s() metoden. Står för panel option
    global selected_action
    option = panel_option(line)

    if line == selected_action:
        return f"{option} <---"
    else:
        return f"{option}"

def s_hp(): #Se s() metoden. Står för stad hp
    return round(städer[selected_city].hp, 0)

def side_panel(line):
    global side_panel_state

    if side_panel_state != SIDE_PANEL_STATE.IDLE:
        match line:
            case 0: return f"|  HP: {s_hp()} "
            case 1: return f"|               "
            case 2: return f"|{p_o(0)}        "
            case 3: return f"|{p_o(1)}        "
            case 4: return f"|{p_o(2)}        "
            case 5: return f"|               |"
            case 6: return f"|               |"

    else:
        match line:
            case 0: return f"|                "
            case 1: return f"|   {enemie_last_action}             "
            case 2: return f"|                "
            case 3: return f"|                "
            case 4: return f"|                "
            case 5: return f"|               |"
            case 6: return f"|               |"
def show_scene():
    #Anledningen till att det görs på det här viset är att städerna aldrig rör sig, 
    #och det här ger mig möjlighet att designa ett spelets utseende enkelt, 
    #+ att städerna inte är placerade på en grid, det är lite huller om buller
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
                        handle_command(selected_city,panel_option(selected_action))
                        side_panel_state = SIDE_PANEL_STATE.IDLE
                        selected_action = 0
        case "d":
            enemie_logic_MK1()

    if selected_city > len(städer)-1:
        selected_city = len(städer)-1
    elif selected_city < 0:
        selected_city = 0
    if selected_action > 2: #3 actions minus 1
        selected_action = 2
    elif selected_action < 0:
        selected_action = 0            
def handle_command(target_city:int, command:str):
    global spelare_attackstyrka, spelare_attackstyrka, fiende_attackstyrka, spelare_pengar
    print(target_city, command)

    #Build commands
    match command:
        case "BUILD FACTORY":
            städer[target_city].stads_typ = STADS_TYPER.FABRIK
        case "BUILD MORTAR":
            städer[target_city].stads_typ = STADS_TYPER.MORTAR

        case "PROPAGANDA":
            spelare_attackstyrka *= 1.2
            spelare_pengar *= 1.2


        case "ATTACK":
            städer[target_city].hp -= spelare_attackstyrka
            if städer[target_city].hp <= 0:
                städer[target_city].stads_typ = STADS_TYPER.RUIN
        case "ENEMIE_ATTACK":
            städer[target_city].hp -= fiende_attackstyrka
            if städer[target_city].hp <= 0:
                städer[target_city].stads_typ = STADS_TYPER.RUIN

        case "SPY":
            städer[target_city].visas = True

    next_game_stage()
        


def enemie_logic_MK1():
    global enemie_last_action
    target_city = random.randint(0,len(städer)-1)
    enemie_last_action = "Enemie worked in secrecy"

    if target_city < antal_fiendestäder: #Staden är en fiendestad
        if städer[target_city].stads_typ != STADS_TYPER.TOM:
            target_city = random.randint(antal_fiendestäder, len(städer)-1)
        else:
            handle_command(target_city, random.choice(["BUILD FACTORY","BUILD MORTAR"]))

    else: #Spelarstad
        handle_command(target_city, "ENEMIE_ATTACK")
        enemie_last_action = f"city {target_city+1}, ATTACKED"
        

    print(target_city)
    print(städer[target_city].stads_typ)
    



def next_game_stage():
    global game_stage
    if game_stage == GAME_STAGES.PLAYER_TURN:
        game_stage = GAME_STAGES.ENEMIE_TURN
        for stad_i in range(antal_fiendestäder, len(städer)):
            if städer[stad_i].stads_typ != STADS_TYPER.RUIN:
                break

            if stad_i == len(städer)-1: #Alla städer är ruiner, spelare förlorar
                game_stage = GAME_STAGES.PLAYER_LOSS

    if game_stage == GAME_STAGES.ENEMIE_TURN:
        game_stage = GAME_STAGES.UPKEEP
    if game_stage == GAME_STAGES.UPKEEP:
        game_stage = GAME_STAGES.PLAYER_TURN

while True:
    print("\033c",end="")
    if game_stage == GAME_STAGES.PLAYER_TURN:
        show_scene()
        handle_input()
    elif game_stage == GAME_STAGES.ENEMIE_TURN:
        enemie_logic_MK1()
    elif game_stage == GAME_STAGES.UPKEEP:
        pass

    elif game_stage == GAME_STAGES.PLAYER_LOSS:
        print("YOU LOST")
        quit()
