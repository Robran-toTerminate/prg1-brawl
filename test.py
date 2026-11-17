text = "012345"

effects = [0,0,[1,3],0,1,0]



def handle_effect(string):
    result = ""
    for i in range(len(string)):
        assigned_char = ""
        if type(effects[i]) == int:
            match effects[i]:
                case 0: assigned_char = string[i]
                case 1: assigned_char = " "; effects[i] = 0
        elif type(effects[i]) == list:
            match effects[i][0]:
                case 1:
                    if effects[i][1] > 0:
                        assigned_char = "-"
                        effects[i][1] -= 1
                    else: assigned_char = string[i]; effects[i] = 0
        else:
            assigned_char = "*"
            effects[i] = 0
        result += assigned_char
    return result




for i in range(6):
    print(handle_effect(text))



