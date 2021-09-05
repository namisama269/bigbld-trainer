"""
Cube Settings
"""
# Enter orientation colours in the format "ULFRBD".
orientation = "YBRGOW"

# Enter pieces 
pieces = {
    'c': [
        ['UFR','RUF','FUR'], ['UFL','FUL','LUF'], ['UBL','LUB','BUL'], ['UBR','BUR','RUB'],
        ['DFR','FDR','RDF'], ['DBR','RDB','BDR'], ['DBL','BDL','LDB'], ['DFL','LDF','FDL'], 
    ],
    'e': [
        ['UB','BU'], ['UL','LU'], ['UR','RU'], ['UF','FU'],
        ['FL','LF'], ['FR','RF'], ['LB','BL'], ['RB','BR'],
        ['DB','BD'], ['DL','LD'], ['DR','RD'], ['DF','FD'],
    ],
    'x': [
        ['Ubl', 'Ubr', 'Ufl', 'Ufr'], ['Lub', 'Luf', 'Ldb', 'Ldf'],
        ['Ful', 'Fur', 'Fdl', 'Fdr'], ['Ruf', 'Rub', 'Rdf', 'Rdb'],
        ['Bul', 'Bur', 'Bdl', 'Bdr'], ['Dbl', 'Dbr', 'Dfl', 'Dfr'],
    ],
    't': [
        ['Ub', 'Ul', 'Ur', 'Uf'], ['Lu', 'Lb', 'Lf', 'Ld'], ['Fu', 'Fl', 'Fr', 'Fd'],
        ['Ru', 'Rf', 'Rb', 'Rd'], ['Bu', 'Bl', 'Br', 'Bd'], ['Db', 'Dl', 'Dr', 'Df'],
    ],
    'w': [
        ['UBl'], ['ULf'], ['URb'], ['UFr'], ['LUb'], ['LBd'], ['LFu'], ['LDf'],
        ['FUl'], ['FLd'], ['FRu'], ['FDr'], ['RUf'], ['RFd'], ['RBu'], ['RDb'],
        ['BUr'], ['BLu'], ['BRd'], ['BDl'], ['DBr'], ['DLb'], ['DRf'], ['DFl'],
    ],
}

# Piece types to train
pce_types = ['c','e','x','t','w']
pce_names = {
    'c': 'corners',
    'e': 'edges',
    'x': 'x-centres',
    't': 't-centres',
    'w': 'wings',
}


# Buffers
buffers = {
    'c': 'UFR',
    'e': 'UF',
    'x': 'Ufr',
    't': 'Uf',
    'w': 'UFr'
}

letter_scheme = {
    # corners
    'UBL': 'A',
    'UBR': 'B',
    'UFL': 'C',
    'UFR': 'D',
    'LUB': 'E',
    'LUF': 'F',
    'LDB': 'G',
    'LDF': 'H',
    'FUL': 'I',
    'FUR': 'J',
    'FDL': 'K',
    'FDR': 'L',
    'RUF': 'M',
    'RUB': 'N',
    'RDF': 'O',
    'RDB': 'P',
    'BUL': 'Q',
    'BUR': 'R',
    'BDL': 'S',
    'BDR': 'T',
    'DBL': 'U',
    'DBR': 'V',
    'DFL': 'W',
    'DFR': 'X',

    # edges
    'UB': 'A',
    'UL': 'B',
    'UR': 'C',
    'UF': 'D',
    'LU': 'E',
    'LB': 'F',
    'LF': 'G',
    'LD': 'H',
    'FU': 'I',
    'FL': 'J',
    'FR': 'K',
    'FD': 'L',
    'RU': 'M',
    'RF': 'N',
    'RB': 'O',
    'RD': 'P',
    'BU': 'Q',
    'BL': 'R',
    'BR': 'S',
    'BD': 'T',
    'DB': 'U',
    'DL': 'V',
    'DR': 'W',
    'DF': 'X',

    # x-centres
    'Ubl': 'A',
    'Ubr': 'B',
    'Ufl': 'C',
    'Ufr': 'D',
    'Lub': 'E',
    'Luf': 'F',
    'Ldb': 'G',
    'Ldf': 'H',
    'Ful': 'I',
    'Fur': 'J',
    'Fdl': 'K',
    'Fdr': 'L',
    'Ruf': 'M',
    'Rub': 'N',
    'Rdf': 'O',
    'Rdb': 'P',
    'Bul': 'Q',
    'Bur': 'R',
    'Bdl': 'S',
    'Bdr': 'T',
    'Dbl': 'U',
    'Dbr': 'V',
    'Dfl': 'W',
    'Dfr': 'X',

    # t-centres
    'Ub': 'A',
    'Ul': 'B',
    'Ue': 'C',
    'Uf': 'D',
    'Lu': 'E',
    'Lb': 'F',
    'Lf': 'G',
    'Ld': 'H',
    'Fu': 'I',
    'Fl': 'J',
    'Fr': 'K',
    'Fd': 'L',
    'Ru': 'M',
    'Rf': 'N',
    'Rb': 'O',
    'Rd': 'P',
    'Bu': 'Q',
    'Bl': 'R',
    'Br': 'S',
    'Bd': 'T',
    'Db': 'U',
    'Dl': 'V',
    'Dr': 'W',
    'Df': 'X',

    # wings
    'UBl': 'A',
    'ULf': 'B', 
    'URb': 'C',
    'UFr': 'D', 
    'LUb': 'E',
    'LBd': 'F', 
    'LFu': 'G',
    'LDf': 'H',
    'FUl': 'I',
    'FLd': 'J', 
    'FRu': 'K',
    'FDr': 'L', 
    'RUf': 'M',
    'RFd': 'N', 
    'RBu': 'O',
    'RDb': 'P',
    'BUr': 'Q',
    'BLu': 'R',
    'BRd': 'S', 
    'BDl': 'T', 
    'DBr': 'U', 
    'DLb': 'V', 
    'DRf': 'W',
    'DFl': 'X',
}

"""
GUI Settings
"""
# Enter the following colours in (R, G, B) format. 

# Background colour
bg_colour = (255,250,205)#(238,255,204)

# Face colours
face_colours = {
    'W': (255,255,255),
    'Y': (240,255,0),
    'B': (32,85,255),
    'G': (102,255,51),
    'R': (232,18,10),
    'O': (251,140,0),
}

# BLD mode colours
buffer_clr = (255,0,0)
target_clr1 = (204,153,255)
target_clr2 = (153,51,255)
highlight_clr = (245,245,245)
fill_clr = (224,224,224)

# Button colours
button_clr = (255,187,187)#(190,190,190)
hover_clr = (255,221,221)#(211,211,211)
