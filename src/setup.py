import urllib.request
from time import sleep
from http.client import IncompleteRead

from config import *

URL = "http://cube.rider.biz/visualcube.php"

def replace_at_index(string, index, letter):
    return string[:index] + letter + string[index + 1:]

vcube_skel = {
    'outer': "wwwwwwtttwwtttwwtttwwwwww"*3 + "sssssstttsstttsstttssssss"*3,
    'inner': "ttttttwwwttwwwttwwwtttttt"*3 + "ttttttsssttsssttssstttttt"*3,
    'full': "w"*75 + "s"*75
}

skel_idxs = {
    'c': {
        'UBL': [0], 'UBR': [4], 'UFL': [20], 'UFR': [24], 
        'LUB': [100], 'LUF': [104], 'LDB': [120], 'LDF': [124],
        'FUL': [50], 'FUR': [54], 'FDL': [70], 'FDR': [74], 
        'RUF': [25], 'RUB': [29], 'RDF': [45], 'RDB': [49],
        'BUL': [129], 'BUR': [125], 'BDL': [149], 'BDR': [145], 
        'DBL': [95], 'DBR': [99], 'DFL': [75], 'DFR': [79],
    },
    'e': {
        'UB': [2], 'UL': [10], 'UR': [14], 'UF': [22],
        'LU': [102], 'LB': [110], 'LF': [114], 'LD': [122],
        'FU': [52], 'FL': [60], 'FR': [64], 'FD': [72],
        'RU': [27], 'RF': [35], 'RB': [39], 'RD': [47],
        'BU': [127], 'BL': [139], 'BR': [135], 'BD': [147],
        'DB': [97], 'DL': [85], 'DR': [89], 'DF': [77],
    },
    'x': {
        'Ubl': [6], 'Ubr': [8], 'Ufl': [16], 'Ufr': [18],
        'Lub': [106], 'Luf': [108], 'Ldb': [116], 'Ldf': [118],
        'Ful': [56], 'Fur': [58], 'Fdl': [66], 'Fdr': [68],
        'Ruf': [31], 'Rub': [33], 'Rdf': [41], 'Rdb': [43],
        'Bul': [133], 'Bur': [131], 'Bdl': [143], 'Bdr': [141],
        'Dbl': [91], 'Dbr': [93], 'Dfl': [81], 'Dfr': [83], 
    },
    't': {
        'Ub': [7], 'Ul': [11], 'Ur': [13], 'Uf': [17],
        'Lu': [107], 'Lb': [111], 'Lf': [113], 'Ld': [117],
        'Fu': [57], 'Fl': [61], 'Fr': [63], 'Fd': [67],
        'Ru': [32], 'Rf': [36], 'Rb': [38], 'Rd': [42],
        'Bu': [132], 'Bl': [138], 'Br': [136], 'Bd': [142],
        'Db': [92], 'Dl': [86], 'Dr': [88], 'Df': [82],
    },
    'w': {
        'UBl': [1,128], 'ULf': [15,103], 'URb': [9,28], 'UFr': [23,53], 
        'LUb': [5,101], 'LBd': [115,144], 'LFu': [55,109], 'LDf': [80,123],
        'FUl': [21,51], 'FLd': [65,119], 'FRu': [30,59], 'FDr': [73,78], 
        'RUf': [19,26], 'RFd': [40,69], 'RBu': [34,130], 'RDb': [48,94],
        'BUr': [3,126], 'BLu': [105,134], 'BRd': [44,140], 'BDl': [96,148], 
        'DBr': [98,146], 'DLb': [90,121], 'DRf': [46,84], 'DFl': [71,76],
    },
}

arrow_idxs = {
    'c': {
        'UBL': 'U0', 'UBR': 'U4', 'UFL': 'U20', 'UFR': 'U24', 
        'LUB': 'L0', 'LUF': 'L4', 'LDB': 'L20', 'LDF': 'L24',
        'FUL': 'F0', 'FUR': 'F4', 'FDL': 'F20', 'FDR': 'F24', 
        'RUF': 'R0', 'RUB': 'R4', 'RDF': 'R20', 'RDB': 'R24',
        'BUL': 'B4', 'BUR': 'B0', 'BDL': 'B24', 'BDR': 'B20', 
        'DBL': 'D20', 'DBR': 'D24', 'DFL': 'D0', 'DFR': 'D4',
    },
    'e': {
        'UB': 'U2', 'UL': 'U10', 'UR': 'U14', 'UF': 'U22',
        'LU': 'L2', 'LB': 'L10', 'LF': 'L14', 'LD': 'L22',
        'FU': 'F2', 'FL': 'F10', 'FR': 'F14', 'FD': 'F22',
        'RU': 'R2', 'RF': 'R10', 'RB': 'R14', 'RD': 'R22',
        'BU': 'B2', 'BL': 'B14', 'BR': 'B10', 'BD': 'B22',
        'DB': 'D22', 'DL': 'D10', 'DR': 'D14', 'DF': 'D2',
    },
    'x': {
        'Ubl': 'U6', 'Ubr': 'U8', 'Ufl': 'U16', 'Ufr': 'U18',
        'Lub': 'L6', 'Luf': 'L8', 'Ldb': 'L16', 'Ldf': 'L18',
        'Ful': 'F6', 'Fur': 'F8', 'Fdl': 'F16', 'Fdr': 'F18',
        'Ruf': 'R6', 'Rub': 'R8', 'Rdf': 'R16', 'Rdb': 'R18',
        'Bul': 'B8', 'Bur': 'B6', 'Bdl': 'B18', 'Bdr': 'B16',
        'Dbl': 'D16', 'Dbr': 'D18', 'Dfl': 'D6', 'Dfr': 'D8', 
    },
    't': {
        'Ub': 'U7', 'Ul': 'U11', 'Ur': 'U13', 'Uf': 'U17',
        'Lu': 'L7', 'Lb': 'L11', 'Lf': 'L13', 'Ld': 'L17',
        'Fu': 'F7', 'Fl': 'F11', 'Fr': 'F13', 'Fd': 'F17',
        'Ru': 'R7', 'Rf': 'R11', 'Rb': 'R13', 'Rd': 'R17',
        'Bu': 'B7', 'Bl': 'B13', 'Br': 'B11', 'Bd': 'B17',
        'Db': 'D17', 'Dl': 'D11', 'Dr': 'D13', 'Df': 'D7',
    },
    'w': {
        'UBl': 'U1', 'ULf': 'U15', 'URb': 'U9', 'UFr': 'U23', 
        'LUb': 'L1', 'LBd': 'L15', 'LFu': 'L9', 'LDf': 'L23',
        'FUl': 'F1', 'FLd': 'F15', 'FRu': 'F9', 'FDr': 'F23', 
        'RUf': 'R1', 'RFd': 'R15', 'RBu': 'R9', 'RDb': 'R23',
        'BUr': 'B1', 'BLu': 'B9', 'BRd': 'B15', 'BDl': 'B23', 
        'DBr': 'D23', 'DLb': 'D15', 'DRf': 'D9', 'DFl': 'D1',
    },
}

def arrow_cycle(pce_type, p1, p2):
    arrow = "-s8-d,"
    return (arrow_idxs[pce_type][buffers[pce_type]] + arrow_idxs[pce_type][p1] + arrow 
    + arrow_idxs[pce_type][p1] + arrow_idxs[pce_type][p2] + arrow 
    + arrow_idxs[pce_type][p2] + arrow_idxs[pce_type][buffers[pce_type]] + arrow)

def generate_url(pce_type, p1, p2):
    skel = "w"*75 + "s"*75
    targets = (buffers[pce_type], p1, p2)
    target_clrs = ('r','m','m')
    for i in range(3):
        for idx in skel_idxs[pce_type][targets[i]]:
            skel = replace_at_index(skel, idx, target_clrs[i])

    params = [
        "fmt=png",
        "pzl=5",
        "size=400",
        "r=y25x-34",
        "cc=l",
        "bg=t",
        "fo=80",
        "co=15",
        "fc=" + skel,
        "arw=" + arrow_cycle(pce_type, p1, p2)
    ]
    return f"{URL}?{'&'.join(params)}"

def buffer_idx(pce_type):
    i = 0
    while i < len(pieces[pce_type]):
        if buffers[pce_type] in pieces[pce_type][i]:
            break
        i += 1
    return i

def download_imgs():
    for pce_type in ['e']:
        counter = 0
        pces = pieces[pce_type]
        for i in range(len(pces)):
            for j in range(len(pces)):
                if i == j:
                    continue
                for k in range(len(pces[i])):
                    for l in range(len(pces[j])):
                        p1 = pces[i][k]
                        p2 = pces[j][l]
                        if pce_type in ('x','t','w') and (p1 == buffers[pce_type] or p2 == buffers[pce_type]):
                            continue
                        elif pce_type in ('c','e') and (p1 in pces[buffer_idx(pce_type)] or p2 in pces[buffer_idx(pce_type)]):
                            continue
                        url = generate_url(pce_type, p1, p2)
                        filepath = f"images/{pce_type}/{buffers[pce_type]} {p1} {p2}.png"
                        try:
                            urllib.request.urlretrieve(url, filepath)
                            counter += 1
                            print(f"saved ({buffers[pce_type]} {p1} {p2}) to images/{pce_type} [{counter}]")
                        except ConnectionResetError:
                            sleep(5)
                        except IncompleteRead:
                            continue


if __name__ == "__main__":
    """
    pce_type = input("piece type: ")
    p1, p2 = input("targets: ").split()
    print(generate_url(pce_type, p1, p2))
    """
    download_imgs()
