import string
import random
import time

"""ABOUT THE PROGRAMME"""
# This program has more than 15 modes. All details are given in the first 150 lines after executing the program.
'''First of all, this program encrypts text in all possible ways that I thought of. My major and important encryption
 type is the first one, which was easy to write code for, but the encrypted message is not easy to crack because it
 produces a new encrypted message for the same input each time. The second one is Morse code, the third one is custom 
 encryption, and the fourth one is common encryption, the easiest one. The fifth one is the same as the third one but 
 only encrypts in the form of "tehsn". My decryption program can easily identify the type of encryption and decrypt 
 according to it.
 All other details will be given to the user while executing this program.'''
# >>> SOME FEATURES <<<
# 1. The program can encrypt all alphabets, all numbers, and all types of special characters.
# 2. The first encryption has the option to add a password. After adding a password, that message can only be accessed using that password.
# 3. If we want to decrypt all the messages at the same time, then we have to give input in the form of "1 : 2 : 4 : 3".
# >>>> ALL TYPES OF ENCRYPTION AND DECRYPTION DATA <<<<
# >>>> To select a random letter which will be replaced <<<<

alpha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
r_alpha = random.choice(alpha)
# DATA START____________________________________________________________________________________________________________
# >>> replacement dictionary <<<
replace_dic = {'a': chr(ord('a') - r_alpha), 'b': chr(ord('b') + r_alpha), 'c': chr(ord('c') - r_alpha),
               'd': chr(ord('d') + r_alpha),
               'e': chr(ord('e') - r_alpha), 'f': chr(ord('f') + r_alpha), 'g': chr(ord('g') - r_alpha),
               'h': chr(ord('h') + r_alpha),
               'i': chr(ord('i') - r_alpha), 'j': chr(ord('j') + r_alpha), 'k': chr(ord('k') - r_alpha),
               'l': chr(ord('l') + r_alpha),
               'm': chr(ord('m') - r_alpha), 'n': chr(ord('n') + r_alpha), 'o': chr(ord('o') - r_alpha),
               'p': chr(ord('p') + r_alpha),
               'q': chr(ord('q') - r_alpha), 'r': chr(ord('r') + r_alpha), 's': chr(ord('s') - r_alpha),
               't': chr(ord('t') + r_alpha),
               'u': chr(ord('u') - r_alpha), 'v': chr(ord('v') + r_alpha), 'w': chr(ord('w') - r_alpha),
               'x': chr(ord('x') + r_alpha),
               'y': chr(ord('y') - r_alpha), 'z': chr(ord('z') + r_alpha), 'A': chr(ord('A') - r_alpha),
               'B': chr(ord('B') + r_alpha),
               'C': chr(ord('C') - r_alpha), 'D': chr(ord('D') + r_alpha), 'E': chr(ord('E') - r_alpha),
               'F': chr(ord('F') + r_alpha),
               'G': chr(ord('G') - r_alpha), 'H': chr(ord('H') + r_alpha), 'I': chr(ord('I') - r_alpha),
               'J': chr(ord('J') + r_alpha),
               'K': chr(ord('K') - r_alpha), 'L': chr(ord('L') + r_alpha), 'M': chr(ord('M') - r_alpha),
               'N': chr(ord('N') + r_alpha),
               'O': chr(ord('O') - r_alpha), 'P': chr(ord('P') + r_alpha), 'Q': chr(ord('Q') - r_alpha),
               'R': chr(ord('R') + r_alpha),
               'S': chr(ord('S') - r_alpha), 'T': chr(ord('T') + r_alpha), 'U': chr(ord('U') - r_alpha),
               'V': chr(ord('V') + r_alpha),
               'W': chr(ord('W') - r_alpha), 'X': chr(ord('X') + r_alpha), 'Y': chr(ord('Y') - r_alpha),
               'Z': chr(ord('Z') + r_alpha),
               '1': chr(ord('1') - r_alpha), '2': chr(ord('2') + r_alpha), '3': chr(ord('3') - r_alpha),
               '4': chr(ord('4') + r_alpha),
               '5': chr(ord('5') - r_alpha), '6': chr(ord('6') + r_alpha), '7': chr(ord('7') - r_alpha),
               '8': chr(ord('8') + r_alpha),
               '9': chr(ord('9') - r_alpha), '0': chr(ord('0') + r_alpha), '!': chr(ord('!') - r_alpha),
               '.': chr(ord('.') + r_alpha)}
# >>>reverse dictionary<<<
reverse_dic = {}
# >>>random letters(including special characters) list replaced on 1st and last three indexes
r_letter = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
            '@',
            '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
            'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

r_letter_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v'
    , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# >>>>> MOST COMMON METHOD DICTIONARY ENCRYPTION<<<<
m_com = {'0': '2', '1': '1', '2': '5', '3': '7', '4': '0', '5': '6', '6': '3', '7': '4', '8': '9', '9': '8', 'a': 'h',
         'b': 't', 'c': 'd', 'd': 'g', 'e': 'a', 'f': 'i', 'g': 'n', 'h': 'j', 'i': 'f', 'j': 'q', 'k': 'r', 'l': 'b',
         'm': 'e', 'n': 'k', 'o': 'x', 'p': 'o', 'q': 'y', 'r': 'p', 's': 'v', 't': 'c', 'u': 'm', 'v': 's', 'w': 'l',
         'x': 'z', 'y': 'u', 'z': 'w', 'A': 'N', 'B': 'X', 'C': 'O', 'D': 'Y', 'E': 'M', 'F': 'H', 'G': 'P', 'H': 'S',
         'I': 'Z', 'J': 'B', 'K': 'W', 'L': 'K', 'M': 'R', 'N': 'G', 'O': 'A', 'P': 'C', 'Q': 'I', 'R': 'L', 'S': 'J',
         'T': 'D', 'U': 'V', 'V': 'U', 'W': 'Q', 'X': 'T', 'Y': 'E', 'Z': 'F', '!': '$', '"': '+', '#': '^', '$': '&',
         '%': '!', '&': '%', "'": '-', '(': '}', ')': '~', '*': '"', '+': '[', ',': '.', '-': '#', '.': ')', '/': '|',
         ':': ']', ';': '_', '<': '=', '=': '`', '>': '*', '?': '>', '@': '{', '[': '(', '\\': '@', ']': '\\', '^': '/',
         '_': ';', '`': ':', '{': '?', '|': '<', '}': "'", '~': ',', '¬': '£', '£': '¬'}  # ,'¯':'¯','—':'—'
# >>>>> MOST COMMON METHOD DICTIONARY DECRYPTION<<<<
m_com_r = {'2': '0', '1': '1', '5': '2', '7': '3', '0': '4', '6': '5', '3': '6', '4': '7', '9': '8', '8': '9', 'h': 'a',
           't': 'b', 'd': 'c', 'g': 'd', 'a': 'e', 'i': 'f', 'n': 'g', 'j': 'h', 'f': 'i', 'q': 'j', 'r': 'k', 'b': 'l',
           'e': 'm', 'k': 'n', 'x': 'o', 'o': 'p', 'y': 'q', 'p': 'r', 'v': 's', 'c': 't', 'm': 'u', 's': 'v', 'l': 'w',
           'z': 'x', 'u': 'y', 'w': 'z', 'N': 'A', 'X': 'B', 'O': 'C', 'Y': 'D', 'M': 'E', 'H': 'F', 'P': 'G', 'S': 'H',
           'Z': 'I', 'B': 'J', 'W': 'K', 'K': 'L', 'R': 'M', 'G': 'N', 'A': 'O', 'C': 'P', 'I': 'Q', 'L': 'R', 'J': 'S',
           'D': 'T', 'V': 'U', 'U': 'V', 'Q': 'W', 'T': 'X', 'E': 'Y', 'F': 'Z', '$': '!', '+': '"', '^': '#', '&': '$',
           '!': '%', '%': '&', '-': "'", '}': '(', '~': ')', '"': '*', '[': '+', '.': ',', '#': '-', ')': '.', '|': '/',
           ']': ':', '_': ';', '=': '<', '`': '=', '*': '>', '>': '?', '{': '@', '(': '[', '@': '\\', '\\': ']',
           '/': '^', ';': '_', ':': '`', '?': '{', '<': '|', "'": '}', ',': '~', '¬': '£', '£': '¬'}
# >>>>> MORSE CODE <<<<
# >>>>> To DECRYPT AUTOMATICALLY <<<<<
r_morse = ['___', '__-', '__.', '__—', '__¯', '_-_', '_--']
# >>>>> MAIN LISTS <<<<<
b_morse = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!',
           '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
           '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '£', '¬', ' ']
d_morse = ['___', '__-', '__.', '__—', '__¯', '_-_', '_--', '_-.', '_-—', '_-¯', '_._', '_.-', '_..', '_.—', '_.¯',
           '_—_', '_—-', '_—.', '_——', '_—¯', '_¯_', '_¯-', '_¯.', '_¯—', '_¯¯', '-__', '-_-', '-_.', '-_—', '-_¯',
           '--_', '---', '--.', '--—', '--¯', '-._', '-.-', '-..', '-.—', '-.¯', '-—_', '-—-', '-—.', '-——', '-—¯',
           '-¯_', '-¯-', '-¯.', '-¯—', '-¯¯', '.__', '._-', '._.', '._—', '._¯', '.-_', '.--', '.-.', '.-—', '.-¯',
           '.._', '..-', '...', '..—', '..¯', '.—_', '.—-', '.—.', '.——', '.—¯', '.¯_', '.¯-', '.¯.', '.¯—', '.¯¯',
           '—__', '—_-', '—_.', '—_—', '—_¯', '—-_', '—--', '—-.', '—-—', '—-¯', '—._', '—.-', '—..', '—.—', '—.¯',
           '——_', '——-', '——.', '———', "¯¯—", "¯¯¯", '–.¯']
# >>>>> Morse DICTIONARY <<<<<
b_morse_dic = {'0': '___', '1': '__-', '2': '__.', '3': '__—', '4': '__¯', '5': '_-_', '6': '_--', '7': '_-.',
               '8': '_-—',
               '9': '_-¯', 'a': '_._', 'b': '_.-', 'c': '_..', 'd': '_.—', 'e': '_.¯', 'f': '_—_', 'g': '_—-',
               'h': '_—.',
               'i': '_——', 'j': '_—¯', 'k': '_¯_', 'l': '_¯-', 'm': '_¯.', 'n': '_¯—', 'o': '_¯¯', 'p': '-__',
               'q': '-_-',
               'r': '-_.', 's': '-_—', 't': '-_¯', 'u': '--_', 'v': '---', 'w': '--.', 'x': '--—', 'y': '--¯',
               'z': '-._',
               'A': '-.-', 'B': '-..', 'C': '-.—', 'D': '-.¯', 'E': '-—_', 'F': '-—-', 'G': '-—.', 'H': '-——',
               'I': '-—¯',
               'J': '-¯_', 'K': '-¯-', 'L': '-¯.', 'M': '-¯—', 'N': '-¯¯', 'O': '.__', 'P': '._-', 'Q': '._.',
               'R': '._—',
               'S': '._¯', 'T': '.-_', 'U': '.--', 'V': '.-.', 'W': '.-—', 'X': '.-¯', 'Y': '.._', 'Z': '..-',
               '!': '...',
               '"': '..—', '#': '..¯', '$': '.—_', '%': '.—-', '&': '.—.', "'": '.——', '(': '.—¯', ')': '.¯_',
               '*': '.¯-',
               '+': '.¯.', ',': '.¯—', '-': '.¯¯', '.': '—__', '/': '—_-', ':': '—_.', ';': '—_—', '<': '—_¯',
               '=': '—-_',
               '>': '—--', '?': '—-.', '@': '—-—', '[': '—-¯', '\\': '—._', ']': '—.-', '^': '—..', '_': '—.—',
               '`': '—.¯',
               '{': '——_', '|': '——-', '}': '——.', '~': '———', '£': '¯¯—', '¬': '¯¯¯', ' ': '–.¯'}
d_morse_dic = {'___': '0', '__-': '1', '__.': '2', '__—': '3', '__¯': '4', '_-_': '5', '_--': '6', '_-.': '7',
               '_-—': '8',
               '_-¯': '9', '_._': 'a', '_.-': 'b', '_..': 'c', '_.—': 'd', '_.¯': 'e', '_—_': 'f', '_—-': 'g',
               '_—.': 'h',
               '_——': 'i', '_—¯': 'j', '_¯_': 'k', '_¯-': 'l', '_¯.': 'm', '_¯—': 'n', '_¯¯': 'o', '-__': 'p',
               '-_-': 'q',
               '-_.': 'r', '-_—': 's', '-_¯': 't', '--_': 'u', '---': 'v', '--.': 'w', '--—': 'x', '--¯': 'y',
               '-._': 'z',
               '-.-': 'A', '-..': 'B', '-.—': 'C', '-.¯': 'D', '-—_': 'E', '-—-': 'F', '-—.': 'G', '-——': 'H',
               '-—¯': 'I',
               '-¯_': 'J', '-¯-': 'K', '-¯.': 'L', '-¯—': 'M', '-¯¯': 'N', '.__': 'O', '._-': 'P', '._.': 'Q',
               '._—': 'R',
               '._¯': 'S', '.-_': 'T', '.--': 'U', '.-.': 'V', '.-—': 'W', '.-¯': 'X', '.._': 'Y', '..-': 'Z',
               '...': '!',
               '..—': '"', '..¯': '#', '.—_': '$', '.—-': '%', '.—.': '&', '.——': "'", '.—¯': '(', '.¯_': ')',
               '.¯-': '*',
               '.¯.': '+', '.¯—': ',', '.¯¯': '-', '—__': '.', '—_-': '/', '—_.': ':', '—_—': ';', '—_¯': '<',
               '—-_': '=',
               '—--': '>', '—-.': '?', '—-—': '@', '—-¯': '[', '—._': '\\', '—.-': ']', '—..': '^', '—.—': '_',
               '—.¯': '`',
               '——_': '{', '——-': '|', '——.': '}', '———': '~', '¯¯—': '£', '¯¯¯': '¬', '–.¯': ' '}
# >>>>> Custom Encryption Data <<<<<
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'",
     '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
     '}', '~', '£', '¬', '', ' ']
d = ["tehs", "tehn", "tesh", "tesn", "tenh", "tens", "then", "thes", "thsn", "thse", "thns", "thne", "tseh", "tsen",
     "tshe", "tshn", "tsne", "tsnh", "tnes", "tneh", "tnhs", "tnhe", "tnsh", "tnse", "etnh", "etns", "ethn", "eths",
     "etsn", "etsh", "ehns", "ehnt", "ehts", "ehtn", "ehst", "ehsn", "esnt", "esnh", "estn", "esth", "eshn", "esht",
     "ensh", "enst", "enth", "ents", "enht", "enhs", "htsn", "htse", "htns", "htne", "htes", "hten", "hest", "hesn",
     "hent", "hens", "hetn", "hets", "hsen", "hset", "hsne", "hsnt", "hste", "hstn", "hnet", "hnes", "hnst", "hnse",
     "hnts", "hnte", "steh", "sten", "sthe", "sthn", "stne", "stnh", "setn", "seth", "sehn", "seht", "senh", "sent",
     "shte", "shtn", "shet", "shen", "shnt", "shne", "snth", "snte", "sneh", "snet", "snhe", "snht", "tehsn", "ntse"]
''', "ntsh","ntes", "nteh", "nths", "nthe", "nesh", "nest", "neth", "nets", "neht", "nehs", "nhst", "nhse", "nhts",
    "nhte","nhes", "nhet", "nshe", "nsht", "nste", "nsth", "nset","tehsn", "ntse"]'''
df = ['tehs', 'tehn', 'tesh', 'tesn', 'tenh', 'tens', 'then', 'thes', 'thsn', 'thse', 'thns', 'thne', 'tseh', 'tsen',
      'tshe', 'tshn', 'tsne', 'tsnh', 'tnes', 'tneh', 'tnhs', 'tnhe', 'tnsh', 'tnse', 'etnh', 'etns', 'ethn', 'eths',
      'etsn', 'etsh', 'ehns', 'ehnt', 'ehts', 'ehtn', 'ehst', 'ehsn', 'esnt', 'esnh', 'estn', 'esth', 'eshn', 'esht',
      'ensh', 'enst', 'enth', 'ents', 'enht', 'enhs', 'htsn', 'htse', 'htns', 'htne', 'htes', 'hten', 'hest', 'hesn',
      'hent', 'hens', 'hetn', 'hets', 'hsen', 'hset', 'hsne', 'hsnt', 'hste', 'hstn', 'hnet', 'hnes', 'hnst', 'hnse',
      'hnts', 'hnte', 'steh', 'sten', 'sthe', 'sthn', 'stne', 'stnh', 'setn', 'seth', 'sehn', 'seht', 'senh', 'sent',
      'shte', 'shtn', 'shet', 'shen', 'shnt', 'shne', 'snth', 'snte', 'sneh', 'snet', 'snhe', 'snht', 'tehsn', 'ntse']
ds_cus = 'tehs,tehn,tesh,tesn,tenh,tens,then,thes,thsn,thse,thns,thne,tseh,tsen,tshe,tshn,tsne,tsnh,tnes,tneh,tnhs,' \
         'tnhe,tnsh,tnse,etnh,etns,ethn,eths,etsn,etsh,ehns,ehnt,ehts,ehtn,ehst,ehsn,esnt,esnh,estn,esth,eshn,esht,' \
         'ensh,enst,enth,ents,enht,enhs,htsn,htse,htns,htne,htes,hten,hest,hesn,hent,hens,hetn,hets,hsen,hset,hsne,' \
         'hsnt,hste,hstn,hnet,hnes,hnst,hnse,hnts,hnte,steh,sten,sthe,sthn,stne,stnh,setn,seth,sehn,seht,senh,sent,' \
         'shte,shtn,shet,shen,shnt,shne,snth,snte,sneh,snet,snhe,snht,tehsn,ntse'
# >>>>> Some Variables <<<<<
# >>>>> Binary Encryption data <<<<<
# Dictionaries
b_bin_dic = {'0': '0000000', '1': '0000001', '2': '0000010', '3': '0000011', '4': '0000100', '5': '0000101',
             '6': '0000110', '7': '0000111', '8': '0001000', '9': '0001001', 'a': '0001010', 'b': '0001011',
             'c': '0001100', 'd': '0001101', 'e': '0001110', 'f': '0001111', 'g': '0010000', 'h': '0010001',
             'i': '0010010', 'j': '0010011', 'k': '0010100', 'l': '0010101', 'm': '0010110', 'n': '0010111',
             'o': '0011000', 'p': '0011001', 'q': '0011010', 'r': '0011011', 's': '0011100', 't': '0011101',
             'u': '0011110', 'v': '0011111', 'w': '0100000', 'x': '0100001', 'y': '0100010', 'z': '0100011',
             'A': '0100100', 'B': '0100101', 'C': '0100110', 'D': '0100111', 'E': '0101000', 'F': '0101001',
             'G': '0101010', 'H': '0101011', 'I': '0101100', 'J': '0101101', 'K': '0101110', 'L': '0101111',
             'M': '0110000', 'N': '0110001', 'O': '0110010', 'P': '0110011', 'Q': '0110100', 'R': '0110101',
             'S': '0110110', 'T': '0110111', 'U': '0111000', 'V': '0111001', 'W': '0111010', 'X': '0111011',
             'Y': '0111100', 'Z': '0111101', '!': '0111110', '"': '0111111', '#': '1000000', '$': '1000001',
             '%': '1000010', '&': '1000011', "'": '1000100', '(': '1000101', ')': '1000110', '*': '1000111',
             '+': '1001000', ',': '1001001', '-': '1001010', '.': '1001011', '/': '1001100', ':': '1001101',
             ';': '1001110', '<': '1001111', '=': '1010000', '>': '1010001', '?': '1010010', '@': '1010011',
             '[': '1010100', '\\': '1010101', ']': '1010110', '^': '1010111', '_': '1011000', '`': '1011001',
             '{': '1011010', '|': '1011011', '}': '1011100', '~': '1011101', '£': '1011110', '¬': '1011111',
             '': '1100000', ' ': '1100001'}
d_bin_dic = {'0000000': '0', '0000001': '1', '0000010': '2', '0000011': '3', '0000100': '4', '0000101': '5',
             '0000110': '6', '0000111': '7', '0001000': '8', '0001001': '9', '0001010': 'a', '0001011': 'b',
             '0001100': 'c', '0001101': 'd', '0001110': 'e', '0001111': 'f', '0010000': 'g', '0010001': 'h',
             '0010010': 'i', '0010011': 'j', '0010100': 'k', '0010101': 'l', '0010110': 'm', '0010111': 'n',
             '0011000': 'o', '0011001': 'p', '0011010': 'q', '0011011': 'r', '0011100': 's', '0011101': 't',
             '0011110': 'u', '0011111': 'v', '0100000': 'w', '0100001': 'x', '0100010': 'y', '0100011': 'z',
             '0100100': 'A', '0100101': 'B', '0100110': 'C', '0100111': 'D', '0101000': 'E', '0101001': 'F',
             '0101010': 'G', '0101011': 'H', '0101100': 'I', '0101101': 'J', '0101110': 'K', '0101111': 'L',
             '0110000': 'M', '0110001': 'N', '0110010': 'O', '0110011': 'P', '0110100': 'Q', '0110101': 'R',
             '0110110': 'S', '0110111': 'T', '0111000': 'U', '0111001': 'V', '0111010': 'W', '0111011': 'X',
             '0111100': 'Y', '0111101': 'Z', '0111110': '!', '0111111': '"', '1000000': '#', '1000001': '$',
             '1000010': '%', '1000011': '&', '1000100': "'", '1000101': '(', '1000110': ')', '1000111': '*',
             '1001000': '+', '1001001': ',', '1001010': '-', '1001011': '.', '1001100': '/', '1001101': ':',
             '1001110': ';', '1001111': '<', '1010000': '=', '1010001': '>', '1010010': '?', '1010011': '@',
             '1010100': '[', '1010101': '\\', '1010110': ']', '1010111': '^', '1011000': '_', '1011001': '`',
             '1011010': '{', '1011011': '|', '1011100': '}', '1011101': '~', '1011110': '£', '1011111': '¬',
             '1100000': '', '1100001': ' '}
# lists
d_bin = ['0000000', '0000001', '0000010', '0000011', '0000100', '0000101', '0000110', '0000111', '0001000', '0001001',
         '0001010',
         '0001011', '0001100', '0001101', '0001110', '0001111', '0010000', '0010001', '0010010', '0010011', '0010100',
         '0010101',
         '0010110', '0010111', '0011000', '0011001', '0011010', '0011011', '0011100', '0011101', '0011110', '0011111',
         '0100000', '0100001',
         '0100010', '0100011', '0100100', '0100101', '0100110', '0100111', '0101000', '0101001', '0101010', '0101011',
         '0101100',
         '0101101', '0101110', '0101111', '0110000', '0110001', '0110010', '0110011', '0110100', '0110101', '0110110',
         '0110111',
         '0111000', '0111001', '0111010', '0111011', '0111100', '0111101', '0111110', '0111111', '1000000', '1000001',
         '1000010',
         '1000011', '1000100', '1000101', '1000110', '1000111', '1001000', '1001001', '1001010', '1001011', '1001100',
         '1001101',
         '1001110', '1001111', '1010000', '1010001', '1010010', '1010011', '1010100', '1010101', '1010110', '1010111',
         '1011000',
         '1011001', '1011010', '1011011', '1011100', '1011101', '1011110', '1011111', '1100000', '1100001']
# Some other data
# >>>> Heart encryption data <<<<
h_list = ["💜💙💚💛", "💜💙💚🖤", "💜💙💛💚", "💜💙💛🖤", "💜💙🖤💚", "💜💙🖤💛", "💜💚💙🖤", "💜💚💙💛", "💜💚💛🖤",
          "💜💚💛💙", "💜💚🖤💛", "💜💚🖤💙", "💜💛💙💚", "💜💛💙🖤", "💜💛💚💙", "💜💛💚🖤", "💜💛🖤💙", "💜💛🖤💚",
          "💜🖤💙💛", "💜🖤💙💚", "💜🖤💚💛", "💜🖤💚💙", "💜🖤💛💚", "💜🖤💛💙", "💙💜🖤💚", "💙💜🖤💛", "💙💜💚🖤",
          "💙💜💚💛", "💙💜💛🖤", "💙💜💛💚", "💙💚🖤💛", "💙💚🖤💜", "💙💚💜💛", "💙💚💜🖤", "💙💚💛💜", "💙💚💛🖤",
          "💙💛🖤💜", "💙💛🖤💚", "💙💛💜🖤", "💙💛💜💚", "💙💛💚🖤", "💙💛💚💜", "💙🖤💛💚", "💙🖤💛💜", "💙🖤💜💚",
          "💙🖤💜💛", "💙🖤💚💜", "💙🖤💚💛", "💚💜💛🖤", "💚💜💛💙", "💚💜🖤💛", "💚💜🖤💙", "💚💜💙💛", "💚💜💙🖤",
          "💚💙💛💜", "💚💙💛🖤", "💚💙🖤💜", "💚💙🖤💛", "💚💙💜🖤", "💚💙💜💛", "💚💛💙🖤", "💚💛💙💜", "💚💛🖤💙",
          "💚💛🖤💜", "💚💛💜💙", "💚💛💜🖤", "💚🖤💙💜", "💚🖤💙💛", "💚🖤💛💜", "💚🖤💛💙", "💚🖤💜💛", "💚🖤💜💙",
          "💛💜💙💚", "💛💜💙🖤", "💛💜💚💙", "💛💜💚🖤", "💛💜🖤💙", "💛💜🖤💚", "💛💙💜🖤", "💛💙💜💚", "💛💙💚🖤",
          "💛💙💚💜", "💛💙🖤💚", "💛💙🖤💜", "💛💚💜💙", "💛💚💜🖤", "💛💚💙💜",
          "🖤💜💙💚", "🖤💜💚💛", "🖤💜💚💙", "🖤💙💛💚", "🖤💙💛💜", "🖤💙💜💚", "🖤💙💜💛", "🖤💙💚💜",
          "🖤💛💜💚", "🖤💛💙💜🤎", "🖤💛💙💚"]
# >>>> Book Encryption Data <<<<
bk_list = ["📕📗📘📙", "📕📗📘📔", "📕📗📙📘", "📕📗📙📔", "📕📗📔📘", "📕📗📔📙", "📕📘📗📔", "📕📘📗📙", "📕📘📙📔", "📕📘📙📗",
           "📕📘📔📙", "📕📘📔📗", "📕📙📗📘", "📕📙📗📔", "📕📙📘📗", "📕📙📘📔", "📕📙📔📗", "📕📙📔📘", "📕📔📗📙", "📕📔📗📘",
           "📕📔📘📙", "📕📔📘📗", "📕📔📙📘", "📕📔📙📗", "📗📕📔📘", "📗📕📔📙", "📗📕📘📔", "📗📕📘📙", "📗📕📙📔", "📗📕📙📘",
           "📗📘📔📙", "📗📘📔📕", "📗📘📕📙", "📗📘📕📔", "📗📘📙📕", "📗📘📙📔", "📗📙📔📕", "📗📙📔📘", "📗📙📕📔", "📗📙📕📘",
           "📗📙📘📔", "📗📙📘📕", "📗📔📙📘", "📗📔📙📕", "📗📔📕📘", "📗📔📕📙", "📗📔📘📕", "📗📔📘📙", "📘📕📙📔", "📘📕📙📗",
           "📘📕📔📙", "📘📕📔📗", "📘📕📗📙", "📘📕📗📔", "📘📗📙📕", "📘📗📙📔", "📘📗📔📕", "📘📗📔📙", "📘📗📕📔", "📘📗📕📙",
           "📘📙📗📔", "📘📙📗📕", "📘📙📔📗", "📘📙📔📕", "📘📙📕📗", "📘📙📕📔", "📘📔📗📕", "📘📔📗📙", "📘📔📙📕", "📘📔📙📗",
           "📘📔📕📙", "📘📔📕📗", "📙📕📗📘", "📙📕📗📔", "📙📕📘📗", "📙📕📘📔", "📙📕📔📗", "📙📕📔📘", "📙📗📕📔", "📙📗📕📘",
           "📙📗📘📔", "📙📗📘📕", "📙📗📔📘", "📙📗📔📕", "📙📘📕📗", "📙📘📕📔", "📙📘📗📕", "📙📘📗📔",
           "📔📘📕📙", "📔📘📕📗", "📔📘📗📙", "📔📘📗📕", "📔📙📘📗", "📔📙📘📕", "📔📙📕📗", "📔📙📕📘", "📔📙📗📕📒", "📔📙📗📘"]
# >>>> Colon Encryption DATA <<<<
co_list = [":::::::", "::::::;", ":::::;:", ":::::;;", "::::;::", "::::;:;", "::::;;:", "::::;;;", ":::;:::", ":::;::;",
           ":::;:;:",
           ":::;:;;", ":::;;::", ":::;;:;", ":::;;;:", ":::;;;;", "::;::::", "::;:::;", "::;::;:", "::;::;;", "::;:;::",
           "::;:;:;",
           "::;:;;:", "::;:;;;", "::;;:::", "::;;::;", "::;;:;:", "::;;:;;", "::;;;::", "::;;;:;", "::;;;;:", "::;;;;;",
           ":;:::::",
           ":;::::;", ":;:::;:", ":;:::;;", ":;::;::", ":;::;:;", ":;::;;:", ":;::;;;", ":;:;:::", ":;:;::;", ":;:;:;:",
           ":;:;:;;",
           ":;:;;::", ":;:;;:;", ":;:;;;:", ":;:;;;;", ":;;::::", ":;;:::;", ":;;::;:", ":;;::;;", ":;;:;::", ":;;:;:;",
           ":;;:;;:",
           ":;;:;;;", ":;;;:::", ":;;;::;", ":;;;:;:", ":;;;:;;", ":;;;;::", ":;;;;:;", ":;;;;;:", ":;;;;;;", ";::::::",
           ";:::::;",
           ";::::;:", ";::::;;", ";:::;::", ";:::;:;", ";:::;;:", ";:::;;;", ";::;:::", ";::;::;", ";::;:;:", ";::;:;;",
           ";::;;::",
           ";::;;:;", ";::;;;:", ";::;;;;", ";:;::::", ";:;:::;", ";:;::;:", ";:;::;;", ";:;:;::", ";:;:;:;", ";:;:;;:",
           ";:;:;;;",
           ";:;;:::", ";:;;::;", ";:;;:;:",
           ";;;;::;", ";;;;:;:", ";;;;:;;", ";;;;;::", ";;;;;:;", ";;;;;;:", ";;;;;;;"]
# >>>> Clock Encryption DAta <<<<
cl_list = ["🕒🕕🕘🕛", "🕒🕕🕘🕧", "🕒🕕🕛🕘", "🕒🕕🕛🕧", "🕒🕕🕧🕘", "🕒🕕🕧🕛", "🕒🕘🕕🕧", "🕒🕘🕕🕛", "🕒🕘🕛🕧",
           "🕒🕘🕛🕕", "🕒🕘🕧🕛", "🕒🕘🕧🕕", "🕒🕛🕕🕘", "🕒🕛🕕🕧", "🕒🕛🕘🕕", "🕒🕛🕘🕧", "🕒🕛🕧🕕", "🕒🕛🕧🕘",
           "🕒🕧🕕🕛", "🕒🕧🕕🕘", "🕒🕧🕘🕛", "🕒🕧🕘🕕", "🕒🕧🕛🕘", "🕒🕧🕛🕕", "🕕🕒🕧🕘", "🕕🕒🕧🕛", "🕕🕒🕘🕧",
           "🕕🕒🕘🕛", "🕕🕒🕛🕧", "🕕🕒🕛🕘", "🕕🕘🕧🕛", "🕕🕘🕧🕒", "🕕🕘🕒🕛", "🕕🕘🕒🕧", "🕕🕘🕛🕒", "🕕🕘🕛🕧",
           "🕕🕛🕧🕒", "🕕🕛🕧🕘", "🕕🕛🕒🕧", "🕕🕛🕒🕘", "🕕🕛🕘🕧", "🕕🕛🕘🕒", "🕕🕧🕛🕘", "🕕🕧🕛🕒", "🕕🕧🕒🕘",
           "🕕🕧🕒🕛", "🕕🕧🕘🕒", "🕕🕧🕘🕛", "🕘🕒🕛🕧", "🕘🕒🕛🕕", "🕘🕒🕧🕛", "🕘🕒🕧🕕", "🕘🕒🕕🕛", "🕘🕒🕕🕧",
           "🕘🕕🕛🕒", "🕘🕕🕛🕧", "🕘🕕🕧🕒", "🕘🕕🕧🕛", "🕘🕕🕒🕧", "🕘🕕🕒🕛", "🕘🕛🕕🕧", "🕘🕛🕕🕒", "🕘🕛🕧🕕",
           "🕘🕛🕧🕒", "🕘🕛🕒🕕", "🕘🕛🕒🕧", "🕘🕧🕕🕒", "🕘🕧🕕🕛", "🕘🕧🕛🕒", "🕘🕧🕛🕕", "🕘🕧🕒🕛", "🕘🕧🕒🕕",
           "🕛🕒🕕🕘", "🕛🕒🕕🕧", "🕛🕒🕘🕕", "🕛🕒🕘🕧", "🕛🕒🕧🕕", "🕛🕒🕧🕘", "🕛🕕🕒🕧", "🕛🕕🕒🕘", "🕛🕕🕘🕧",
           "🕛🕕🕘🕒", "🕛🕕🕧🕘", "🕛🕕🕧🕒", "🕛🕘🕒🕕", "🕛🕘🕒🕧", "🕛🕘🕕🕒", "🕛🕘🕕🕧", "🕛🕘🕧🕒", "🕛🕘🕧🕕",
           "🕛🕧🕒🕘", "🕛🕧🕒🕕", "🕛🕧🕕🕘", "🕛🕧🕕🕒", "🕛🕧🕘🕕",
           "🕧🕛🕒🕘", "🕧🕛🕕🕒", "🕧🕛🕕🕘"]
# >>>> YNK Encryption DAtA <<<<
ynk_list = ["you never know.you never know.", "you never know.You Never Know.", "you never know.YOU NEVER KNOW.",
            "you never know.you Never know.", "you never know.you never Know.", "you never know.You never know.",
            "you never know.You never Know.", "you never know.you NEVER know.", "you never know.YOU Never Know.",
            "you never know.YOU NEVER know.", "You Never Know.you never know.", "You Never Know.You Never Know.",
            "You Never Know.YOU NEVER KNOW.", "You Never Know.you Never know.", "You Never Know.you never Know.",
            "You Never Know.You never know.", "You Never Know.You never Know.", "You Never Know.you NEVER know.",
            "You Never Know.YOU Never Know.", "You Never Know.YOU NEVER know.", "YOU NEVER KNOW.you never know.",
            "YOU NEVER KNOW.You Never Know.", "YOU NEVER KNOW.YOU NEVER KNOW.", "YOU NEVER KNOW.you Never know.",
            "YOU NEVER KNOW.you never Know.", "YOU NEVER KNOW.You never know.", "YOU NEVER KNOW.You never Know.",
            "YOU NEVER KNOW.you NEVER know.", "YOU NEVER KNOW.YOU Never Know.", "YOU NEVER KNOW.YOU NEVER know.",
            "you Never know.you never know.", "you Never know.You Never Know.", "you Never know.YOU NEVER KNOW.",
            "you Never know.you Never know.", "you Never know.you never Know.", "you Never know.You never know.",
            "you Never know.You never Know.", "you Never know.you NEVER know.", "you Never know.YOU Never Know.",
            "you Never know.YOU NEVER know.", "you never Know.you never know.", "you never Know.You Never Know.",
            "you never Know.YOU NEVER KNOW.", "you never Know.you Never know.", "you never Know.you never Know.",
            "you never Know.You never know.", "you never Know.You never Know.", "you never Know.you NEVER know.",
            "you never Know.YOU Never Know.", "you never Know.YOU NEVER know.", "You never know.you never know.",
            "You never know.You Never Know.", "You never know.YOU NEVER KNOW.", "You never know.you Never know.",
            "You never know.you never Know.", "You never know.You never know.", "You never know.You never Know.",
            "You never know.you NEVER know.", "You never know.YOU Never Know.", "You never know.YOU NEVER know.",
            "You never Know.you never know.", "You never Know.You Never Know.", "You never Know.YOU NEVER KNOW.",
            "You never Know.you Never know.", "You never Know.you never Know.", "You never Know.You never know.",
            "You never Know.You never Know.", "You never Know.you NEVER know.", "You never Know.YOU Never Know.",
            "You never Know.YOU NEVER know.", "you NEVER know.you never know.", "you NEVER know.You Never Know.",
            "you NEVER know.YOU NEVER KNOW.", "you NEVER know.you Never know.", "you NEVER know.you never Know.",
            "you NEVER know.You never know.", "you NEVER know.You never Know.", "you NEVER know.you NEVER know.",
            "you NEVER know.YOU Never Know.", "you NEVER know.YOU NEVER know.", "YOU Never Know.you never know.",
            "YOU Never Know.You Never Know.", "YOU Never Know.YOU NEVER KNOW.", "YOU Never Know.you Never know.",
            "YOU Never Know.you never Know.", "YOU Never Know.You never know.", "YOU Never Know.You never Know.",
            "YOU Never Know.you NEVER know.", "YOU Never Know.YOU Never Know.", "YOU Never Know.YOU NEVER know.",
            "YOU NEVER know.you never know.", "YOU NEVER know.You Never Know.", "YOU NEVER know.YOU NEVER KNOW.",
            "YOU NEVER know.you Never know.", "YOU NEVER know.you never Know.", "YOU NEVER know.You never know.",
            "YOU NEVER know.You never Know.", "YOU NEVER know.you NEVER know."]  # "YOU NEVER know.YOU Never Know.",
# "YOU NEVER know.YOU NEVER know."]
# >>>> Encrypted type data <<<<
en_list = ["Encrypted.Encrypted.", "Encrypted.EnCrypted.", "Encrypted.encrypted.", "Encrypted.ENcrypTED.",
           "Encrypted.enCRYpted.", "Encrypted.ENCRYPted.", "Encrypted.encrypTED.", "Encrypted.eNcRyPtEd.",
           "Encrypted.EnCrYpTeD.", "Encrypted.EncrypteD.", "EnCrypted.Encrypted.", "EnCrypted.EnCrypted.",
           "EnCrypted.encrypted.", "EnCrypted.ENcrypTED.", "EnCrypted.enCRYpted.", "EnCrypted.ENCRYPted.",
           "EnCrypted.encrypTED.", "EnCrypted.eNcRyPtEd.", "EnCrypted.EnCrYpTeD.", "EnCrypted.EncrypteD.",
           "encrypted.Encrypted.", "encrypted.EnCrypted.", "encrypted.encrypted.", "encrypted.ENcrypTED.",
           "encrypted.enCRYpted.", "encrypted.ENCRYPted.", "encrypted.encrypTED.", "encrypted.eNcRyPtEd.",
           "encrypted.EnCrYpTeD.", "encrypted.EncrypteD.", "ENcrypTED.Encrypted.", "ENcrypTED.EnCrypted.",
           "ENcrypTED.encrypted.", "ENcrypTED.ENcrypTED.", "ENcrypTED.enCRYpted.", "ENcrypTED.ENCRYPted.",
           "ENcrypTED.encrypTED.", "ENcrypTED.eNcRyPtEd.", "ENcrypTED.EnCrYpTeD.", "ENcrypTED.EncrypteD.",
           "enCRYpted.Encrypted.", "enCRYpted.EnCrypted.", "enCRYpted.encrypted.", "enCRYpted.ENcrypTED.",
           "enCRYpted.enCRYpted.", "enCRYpted.ENCRYPted.", "enCRYpted.encrypTED.", "enCRYpted.eNcRyPtEd.",
           "enCRYpted.EnCrYpTeD.", "enCRYpted.EncrypteD.", "ENCRYPted.Encrypted.", "ENCRYPted.EnCrypted.",
           "ENCRYPted.encrypted.", "ENCRYPted.ENcrypTED.", "ENCRYPted.enCRYpted.", "ENCRYPted.ENCRYPted.",
           "ENCRYPted.encrypTED.", "ENCRYPted.eNcRyPtEd.", "ENCRYPted.EnCrYpTeD.", "ENCRYPted.EncrypteD.",
           "encrypTED.Encrypted.", "encrypTED.EnCrypted.", "encrypTED.encrypted.", "encrypTED.ENcrypTED.",
           "encrypTED.enCRYpted.", "encrypTED.ENCRYPted.", "encrypTED.encrypTED.", "encrypTED.eNcRyPtEd.",
           "encrypTED.EnCrYpTeD.", "encrypTED.EncrypteD.", "eNcRyPtEd.Encrypted.", "eNcRyPtEd.EnCrypted.",
           "eNcRyPtEd.encrypted.", "eNcRyPtEd.ENcrypTED.", "eNcRyPtEd.enCRYpted.", "eNcRyPtEd.ENCRYPted.",
           "eNcRyPtEd.encrypTED.", "eNcRyPtEd.eNcRyPtEd.", "eNcRyPtEd.EnCrYpTeD.", "eNcRyPtEd.EncrypteD.",
           "EnCrYpTeD.Encrypted.", "EnCrYpTeD.EnCrypted.", "EnCrYpTeD.encrypted.", "EnCrYpTeD.ENcrypTED.",
           "EnCrYpTeD.enCRYpted.", "EnCrYpTeD.ENCRYPted.", "EnCrYpTeD.encrypTED.", "EnCrYpTeD.eNcRyPtEd.",
           "EnCrYpTeD.EnCrYpTeD.", "EnCrYpTeD.EncrypteD.", "EncrypteD.Encrypted.", "EncrypteD.EnCrypted.",
           "EncrypteD.encrypted.", "EncrypteD.ENcrypTED.", "EncrypteD.enCRYpted.", "EncrypteD.ENCRYPted.",
           "EncrypteD.encrypTED.", "EncrypteD.eNcRyPtEd."]  # ,"EncrypteD.EnCrYpTeD.","EncrypteD.EncrypteD."]
# >>>> Emoji Data <<<<
# Encryption
d_emoji = {'0': '😀', '1': '😁', '2': '😂', '3': '🤣', '4': '😃', '5': '😄', '6': '😅', '7': '😆', '8': '😉', '9': '😊',
           'a': '😋', 'b': '😎', 'c': '😍', 'd': '😘', 'e': '🥰', 'f': '😗', 'g': '😙', 'h': '😚', 'i': '🙂', 'j': '🤗',
           'k': '🤩', 'l': '🤔', 'm': '🤨', 'n': '😐', 'o': '😑', 'p': '😶', 'q': '🙄', 'r': '😏', 's': '😣', 't': '😥',
           'u': '😮', 'v': '🤐', 'w': '😯', 'x': '😪', 'y': '😫', 'z': '🥱', 'A': '😴', 'B': '😌', 'C': '😛', 'D': '😜',
           'E': '😝', 'F': '🤤', 'G': '😒', 'H': '😓', 'I': '😔', 'J': '😕', 'K': '🙃', 'L': '🤑', 'M': '😲', 'N': '🙁',
           'O': '😖', 'P': '😞', 'Q': '😟', 'R': '😤', 'S': '😢', 'T': '😭', 'U': '😦', 'V': '😧', 'W': '😨', 'X': '😩',
           'Y': '🤯', 'Z': '😬', '!': '😰', '"': '😱', '#': '🥵', '$': '🥶', '%': '😳', '&': '🤪', "'": '😵', '(': '🥴',
           ')': '😠', '*': '😡', '+': '😷', ',': '🤒', '-': '🤕', '.': '🤢', '/': '🤮', ':': '🤧', ';': '😇', '<': '🥳',
           '=': '🥺', '>': '🤠', '?': '🤡', '@': '🤥', '[': '🤫', '\\': '🤭', ']': '🧐', '^': '🤓', '_': '😈', '`': '👿',
           '{': '🤖', '|': '😺', '}': '😹', '~': '😻', '£': '😼', '¬': '😽', '': '😿', ' ': '😾'}
# Decryption
r_emoji = {'😀': '0', '😁': '1', '😂': '2', '🤣': '3', '😃': '4', '😄': '5', '😅': '6', '😆': '7', '😉': '8', '😊': '9',
           '😋': 'a', '😎': 'b', '😍': 'c', '😘': 'd', '🥰': 'e', '😗': 'f', '😙': 'g', '😚': 'h', '🙂': 'i', '🤗': 'j',
           '🤩': 'k', '🤔': 'l', '🤨': 'm', '😐': 'n', '😑': 'o', '😶': 'p', '🙄': 'q', '😏': 'r', '😣': 's', '😥': 't',
           '😮': 'u', '🤐': 'v', '😯': 'w', '😪': 'x', '😫': 'y', '🥱': 'z', '😴': 'A', '😌': 'B', '😛': 'C', '😜': 'D',
           '😝': 'E', '🤤': 'F', '😒': 'G', '😓': 'H', '😔': 'I', '😕': 'J', '🙃': 'K', '🤑': 'L', '😲': 'M', '🙁': 'N',
           '😖': 'O', '😞': 'P', '😟': 'Q', '😤': 'R', '😢': 'S', '😭': 'T', '😦': 'U', '😧': 'V', '😨': 'W', '😩': 'X',
           '🤯': 'Y', '😬': 'Z', '😰': '!', '😱': '"', '🥵': '#', '🥶': '$', '😳': '%', '🤪': '&', '😵': "'", '🥴': '(',
           '😠': ')', '😡': '*', '😷': '+', '🤒': ',', '🤕': '-', '🤢': '.', '🤮': '/', '🤧': ':', '😇': ';', '🥳': '<',
           '🥺': '=', '🤠': '>', '🤡': '?', '🤥': '@', '🤫': '[', '🤭': '\\', '🧐': ']', '🤓': '^', '😈': '_', '👿': '`',
           '🤖': '{', '😺': '|', '😹': '}', '😻': '~', '😼': '£', '😽': '¬', '😿': '', '😾': ' '}
# >>> 3T data <<<
d_3t = ['⭕⭕⭕⭕⭕⭕⭕', '⭕⭕⭕⭕⭕⭕❌', '⭕⭕⭕⭕⭕❌⭕', '⭕⭕⭕⭕⭕❌❌', '⭕⭕⭕⭕❌⭕⭕', '⭕⭕⭕⭕❌⭕❌',
        '⭕⭕⭕⭕❌❌⭕', '⭕⭕⭕⭕❌❌❌', '⭕⭕⭕❌⭕⭕⭕', '⭕⭕⭕❌⭕⭕❌', '⭕⭕⭕❌⭕❌⭕', '⭕⭕⭕❌⭕❌❌'
    , '⭕⭕⭕❌❌⭕⭕', '⭕⭕⭕❌❌⭕❌', '⭕⭕⭕❌❌❌⭕', '⭕⭕⭕❌❌❌❌', '⭕⭕❌⭕⭕⭕⭕', '⭕⭕❌⭕⭕⭕❌'
    , '⭕⭕❌⭕⭕❌⭕', '⭕⭕❌⭕⭕❌❌', '⭕⭕❌⭕❌⭕⭕', '⭕⭕❌⭕❌⭕❌', '⭕⭕❌⭕❌❌⭕', '⭕⭕❌⭕❌❌❌'
    , '⭕⭕❌❌⭕⭕⭕', '⭕⭕❌❌⭕⭕❌', '⭕⭕❌❌⭕❌⭕', '⭕⭕❌❌⭕❌❌', '⭕⭕❌❌❌⭕⭕', '⭕⭕❌❌❌⭕❌'
    , '⭕⭕❌❌❌❌⭕', '⭕⭕❌❌❌❌❌', '⭕❌⭕⭕⭕⭕⭕', '⭕❌⭕⭕⭕⭕❌', '⭕❌⭕⭕⭕❌⭕', '⭕❌⭕⭕⭕❌❌'
    , '⭕❌⭕⭕❌⭕⭕', '⭕❌⭕⭕❌⭕❌', '⭕❌⭕⭕❌❌⭕', '⭕❌⭕⭕❌❌❌', '⭕❌⭕❌⭕⭕⭕', '⭕❌⭕❌⭕⭕❌'
    , '⭕❌⭕❌⭕❌⭕', '⭕❌⭕❌⭕❌❌', '⭕❌⭕❌❌⭕⭕', '⭕❌⭕❌❌⭕❌', '⭕❌⭕❌❌❌⭕', '⭕❌⭕❌❌❌❌'
    , '⭕❌❌⭕⭕⭕⭕', '⭕❌❌⭕⭕⭕❌', '⭕❌❌⭕⭕❌⭕', '⭕❌❌⭕⭕❌❌', '⭕❌❌⭕❌⭕⭕', '⭕❌❌⭕❌⭕❌'
    , '⭕❌❌⭕❌❌⭕', '⭕❌❌⭕❌❌❌', '⭕❌❌❌⭕⭕⭕', '⭕❌❌❌⭕⭕❌', '⭕❌❌❌⭕❌⭕', '⭕❌❌❌⭕❌❌'
    , '⭕❌❌❌❌⭕⭕', '⭕❌❌❌❌⭕❌', '⭕❌❌❌❌❌⭕', '⭕❌❌❌❌❌❌', '❌⭕⭕⭕⭕⭕⭕', '❌⭕⭕⭕⭕⭕❌'
    , '❌⭕⭕⭕⭕❌⭕', '❌⭕⭕⭕⭕❌❌', '❌⭕⭕⭕❌⭕⭕', '❌⭕⭕⭕❌⭕❌', '❌⭕⭕⭕❌❌⭕', '❌⭕⭕⭕❌❌❌'
    , '❌⭕⭕❌⭕⭕⭕', '❌⭕⭕❌⭕⭕❌', '❌⭕⭕❌⭕❌⭕', '❌⭕⭕❌⭕❌❌', '❌⭕⭕❌❌⭕⭕', '❌⭕⭕❌❌⭕❌'
    , '❌⭕⭕❌❌❌⭕', '❌⭕⭕❌❌❌❌', '❌⭕❌⭕⭕⭕⭕', '❌⭕❌⭕⭕⭕❌', '❌⭕❌⭕⭕❌⭕', '❌⭕❌⭕⭕❌❌'
    , '❌⭕❌⭕❌⭕⭕', '❌⭕❌⭕❌⭕❌', '❌⭕❌⭕❌❌⭕', '❌⭕❌⭕❌❌❌', '❌⭕❌❌⭕⭕⭕', '❌⭕❌❌⭕⭕❌'
    , '❌⭕❌❌⭕❌⭕', '❌⭕❌❌⭕❌❌', '❌⭕❌❌❌⭕⭕', '❌⭕❌❌❌⭕❌', '❌⭕❌❌❌❌⭕', '❌⭕❌❌❌❌❌'
    , '❌❌⭕⭕⭕⭕⭕', '❌❌⭕⭕⭕⭕❌']

# DATA END______________________________________________________________________________________________________________

temp_else = 0
pa_in = 0
pa = 0
# ______________________________________________________________________________________________________________________
# >>>>> MAIN programme <<<<<
ans = ''
# >>>>> Name using inbuilt module <<<<<
#tprint('Tehseen     ENCRYPTION'.center(42))
print("""                    _____        _                                   _____  _   _   ____  ____  __   __ ____   _____  ___   ___   _   _           
                   |_   _|  ___ | |__   ___   ___   ___  _ __       | ____|| \ | | / ___||  _ \ \ \ / /|  _ \ |_   _||_ _| / _ \ | \ | |          
                     | |   / _ \| '_ \ / __| / _ \ / _ \| '_ \      |  _|  |  \| || |    | |_) | \ V / | |_) |  | |   | | | | | ||  \| |          
                     | |  |  __/| | | |\__ \|  __/|  __/| | | |     | |___ | |\  || |___ |  _ <   | |  |  __/   | |   | | | |_| || |\  |          
                     |_|   \___||_| |_||___/ \___| \___||_| |_|     |_____||_| \_| \____||_| \_\  |_|  |_|      |_|  |___| \___/ |_| \_|          
                                                                                                                                                 
""")
# >>>>> Some Information And Instructions
print('\033[1mWELCOME TO Tehseen\'s ENCRYPTION Program.\033[0m')
time.sleep(0.01)
print('Content Table:\n1.Types\n2.Explanation of types.\n3.Examples\n4.Program')
time.sleep(0.01)
print('\033[1mTYPES\033[0m'.center(135))
time.sleep(0.01)
print('◈ Random Word Encryption', end=' ' * 33)
time.sleep(0.01)
print('◈ Morse Code Encryption', end=' ' * 33)
time.sleep(0.01)
print('◈ Custom Encryption')
time.sleep(0.01)
print('◈ Common Encryption', end=' ' * 38)
time.sleep(0.01)
print('◈ Tehseen\'s Encryption', end=' ' * 34)
time.sleep(0.01)
print('◈ Binary Encryption')
time.sleep(0.01)
print('◈ Heart Encryption', end=' ' * 39)
time.sleep(0.01)
print('◈ Emoji\'s Encryption', end=' ' * 36)
time.sleep(0.01)
print('◈ Colon Encryption')
time.sleep(0.01)
print('◈ YNK Encryption', end=' ' * 41)
time.sleep(0.01)
print('◈ Ect  Encryption', end=' ' * 39)
time.sleep(0.01)
print('◈ Book Encryption')
time.sleep(0.01)
print('◈ Clock  Encryption',end=' ' * 38)
time.sleep(0.01)
print('◈ 3T Encryption')
# >>>>> Explanation of Types
time.sleep(0.01)
a = '\nABOUT ENCRYPTION TYPES\n\033[1m1.Random Word Encryption>>>\033[0m\n◈It always produce a different Encrypted text' \
    ' even for same input.\n◈It has option to add password.\n FOR EXAMPLE:\n Encrypted text of:"Exp Encrypt", password:' \
    '1@2\n Encrypted Text: _n-wsvu`qBv#g-=1+X0Ws{Bf,A-=1+KSS.%i>-=1+@f)Ct"7-=1+}@D5*Q$-=1+3-=1+_-1Ls-=1+3\n____________' \
    '__________________________________________________________________________________________________________________' \
    '___________________\n\033[1m2.Morse Code>>>\033[0m\n◈It is not exactly morse code because I don\'t know about mors' \
    'e code.\n Encrypted text of:"Exp Encrypt"\n Encrypted Text: -—_--—-__–.¯-—__¯—_..-_.--¯-__-_¯–.¯__—\n_______________' \
    '____________________________________________________________________________________________________________________' \
    '______________\n\033[1m3.Custom Encryption\033[0m\n◈In custom Encryption you have to add 5 letters and the program' \
    'me will make encrypted sentence using those 5 letters\n For Example:\n Encrypted text of:"Exp Encrypt", String : QW' \
    'ERT\n Encrypted Text: WRETWEQTWQTRTQRWWRETQTRWQRWEWQERWQTRWQRETQRWQWERT\n__________________________________________' \
    '_______________________________________________________________________________________________________\n\033[1m4.C' \
    'ommon Encyption\033[0m\n◈This Encryption type is easy to crack but not very easy.\n For Example\n Encrypted text of:' \
    '"Exp Encrypt"\n Encrypted Text: snjcoupdkMaRA NDEozMuFxlhaY\n_____________________________________________________' \
    '____________________________________________________________________________________________\n'
for i in a:
    print(i, end='')
    time.sleep(0.003)
print("\nABOUT ENCRYPTION TYPES\n\033[1m1.Random Word Encryption>>>\033[0m"
      "\n◈It always produce a different Encrypted text even for same input.\n◈It has option to add password.\n FOR "
      "EXAMPLE:\n Encrypted text of:\"Exp Encrypt\", password:1@2\n Encrypted Text: _n-wsvu`qBv#g-=1+X0Ws{Bf,"
      "A-=1+KSS.%i>-=1+@f)Ct\"7-=1+}@D5*Q$-=1+3-=1+_-1Ls-=1+3"
      "\n___________________________________________________________________________________________________________"
      "______________________________________\n\033[1m2.Morse Code>>>\033[0m\n◈It is not exactly morse code because I"
      " don't know about morse code.\n Encrypted text"
      " of:\"Exp Encrypt\"\n Encrypted Text: -—_--—-__–.¯-—__¯—_..-_.--¯-__-_¯–.¯__—\n__________________________________"
      "_______________________________________________________________________________________________________________\
      n\033[1m3.Custom Encryption\033[0m\n◈In custom Encryption you have to add 5 letters and the programme will make "
      "encrypted sentence using those 5 letters\n For Example:\n Encr"
      "ypted text of:\"Exp Encrypt\", String : QWERT\n Encrypted Text: WRETWEQTWQTRTQRWWRETQTRWQRWEWQERWQTRWQRETQRWQWERT"
      "\n______________________________________________________________________________________________________________"
      "___________________________________\n\033[1m4.Common Encyption\033[0m\n◈This Encryption type is easy to crack but"
      " not very easy.\n For Example\n Encrypted"
      " text of:\"Exp Encrypt\"\n Encrypted Text: snjcoupdkMaRA NDEozMuFxlhaY\n___________________________________________"
      "______________________________________________________________________________________________________\n\033[1m5."
      "Tehseen's Encryption\033[0m\n◈In this type, Encrypted text contains only \"Tehseen\" letters\n For Example\n Encr"
      "ypted text of:\"Exp Encrypt\"\n Encrypted Text: eshnehtnetnsntseeshntnsetsehethsehstetnsetshntsetehsn\n___________"
      "________________________________________________________________________________________________________________"
      "______________________\n\033[1m7.Binary Encryption\033[0m\n◈In this Encryption, Encrypted text contains only \"0\""
      "and \"1\".\n For Example\n Encrypted text of:\"Exp Encrypt\"\n Encrypted Text: "
      "010100001000010011001110000101010000"
      "0101110001100001101101000100011001001110111000011100000\n_______________________________________________________"
      "__________________________________________________________________________________________\n\033[1m8.Emoji Encry"
      "ption\033[0m\n◈In this type Encrypted text contains only emojis.\n For Example\n Encrypted text of:\"Exp Encrypt\""
      "\n Encrypted Text: 😝😪😶😾😝😐😍😏😫😶😥😾😿\n______________________________________________________________"
      "___________________________________________________________________________________\n\033[1m9.Heart Encryption"
      "\033[0m\n◈This works same as name.\n For Example \n Encrypted text of:\"Exp Encrypt\"\n Encrypted Text: 💙💛💚🖤💙"
      "💚💜🖤💙💜🖤💛🖤💛💙💚💙💛💚🖤💜🖤💛💙💜💛💙💚💙💜💚💛💙💚💛💜💙💜🖤💛💙💜💛💚🖤💛💙💚🖤💛💙💜🤎\n__"
      "________________________________________________________________________________________________________________"
      "_______________________________\n\033[1m10.Colon Encryption\033[0m\n◈This Encryption contains \":\" and \";\" only."
      "\n For Example \n Encrypted text of:\"Exp Encrypt\"\n Encrypted Text: :;:;::::;::::;::;;::;;;;;;;;:;:;:::::;:;;;:"
      "::;;::::;;:;;:;:::;:::;;::;::;;;:;;;;;;;;;;;;;;:\n_____________________________________________________________"
      "____________________________________________________________________________________\n\033[1m11.YNK Encryption\033[0m"
      "\n◈This Encryption contains only one pharase \"You never know\".\n For Example \n Encrypted text of:\"Exp En"
      "crypt\"\n Encrypted Text: you never Know.you never know.you Never know.you Never know.YOU NEVER KNOW.You never "
      "know.YOU NEVER know.you NEVER know.you never Know.you never know.YOU NEVER KNOW.you Never know.You Never Know."
      "YOU NEVER KNOW.YOU NEVER KNOW.you NEVER know.you Never know.you never Know.YOU NEVER KNOW.You never know.YOU N"
      "EVER KNOW.YOU NEVER know.YOU NEVER know.you NEVER know.YOU NEVER know.You never Know.\n_______________________"
      "_______________________________________________________________________________________________________________"
      "___________\n\033[1m12.ECT Encryption\033[0m\n◈This types contains only word \"Encrypted\".\n For Example \n Encr"
      "ypted text of:\"Exp Encrypt\"\n Encrypted Text: enCRYpted.Encrypted.ENcrypTED.ENcrypTED.encrypted.ENCRYPted.Encry"
      "pteD.eNcRyPtEd.enCRYpted.Encrypted.encrypted.ENcrypTED.EnCrypted.encrypted.encrypted.eNcRyPtEd.ENcrypTED.enCRYp"
      "ted.encrypted.ENCRYPted.encrypted.EncrypteD.EncrypteD.eNcRyPtEd.EncrypteD.encrypTED.\n_________________________"
      "_______________________________________________________________________________________________________________"
      "_________\n\033[1m13.Book Encryption\033[0m\n◈This type contains books only.\n For Example \n Encrypted text of"
      ":\"Exp Encrypt\"\n Encrypted Text: 📗📙📘📔📗📘📕📔📗📕📔📙📔📙📗📘📗📙📘📔📕📔📙📗📕📙📗📘📗📕📘📙📗📘📙📕📗📕📔📙📗"
      "📕📙📘📔📙📗📘📔📙📗📕📒\n______________________________________________________________________________________"
      "___________________________________________________________\n\033[1m14.Clock Encryption\033[0m\n◈This encryptio"
      "n contains clock emojis only.\n For Example \n Encrypted text of:\"Exp Encrypt\"\n Encrypted Text: 🕕🕛🕘🕧🕕🕘"
      "🕒🕧🕕🕒🕧🕛🕧🕛🕕🕘🕕🕛🕘🕧🕒🕧🕛🕕🕒🕛🕕🕘🕕🕒🕘🕛🕕🕘🕛🕒🕕🕒🕧🕛🕕🕒🕛🕘🕧🕛🕕🕘🕧🕛🕕🕒\n_____"
      "_______________________________________________________________________________________________________________"
      "_____________________________\n\033[1m15.3T Encryption\033[0m\n◈This encryptio"
      "n contains Tic Tac Toe only.\n For Example \n Encrypted text of:\"Exp Encrypt\"\n Encrypted Text: ⭕❌⭕❌⭕⭕⭕"
      "⭕❌⭕⭕⭕⭕❌⭕⭕❌❌⭕⭕❌❌❌⭕⭕⭕⭕❌⭕❌⭕❌⭕⭕⭕⭕⭕❌⭕❌❌❌⭕⭕⭕❌❌⭕⭕⭕⭕❌❌⭕❌❌⭕❌"
      "⭕⭕⭕❌⭕⭕⭕❌❌⭕⭕❌⭕⭕❌❌❌⭕❌❌❌⭕⭕⭕⭕❌❌❌⭕⭕⭕⭕⭕\n_____"
      "_______________________________________________________________________________________________________________"
      "_____________________________\n\n\033[1mEnter all to encrypt messagein all the types.\033[0m\nEnter 5, then en"
      "ter encypted message like 1 : 2 : 4 : 3\n\033[1mNew Method\033[0m\nEnter all Encrypted Messages separated by \"@"
      "-@\".\nEncrypted Text: ~~|+]]­0‑0]]0­0+]]]+‖­­0‖]+0­++]]­­0‖0‖0­0+"
      "]]]+‖­­0‖]]0­0+]]]+‖­­00‖]­0]­­+­]]]+]‖‖‖]]+0­0+]]]+‖­­0+0‖]­]]­+00+‖0‖­‖]]‖+0­0+]]]+"
      "‖­­0­]‖0­0­­]+]‖‖+]+0]­­]0­0+]]]+‖­­0++00]+­+‖+­+0++­]0‖‖000]0­0+]]]+‖­­0‖‖‖­0000"
      "]]]+‖0‖]­]00]]00]‖0]]‖0­0+]]]+‖­­0]0+‖‖++]‖+‖]+]+‖‖+000]­00­0+]]]+‖­­0‖0]000]0+0+000]­‖]+]+00]00]]]+"
      "]]]+0+‖0‖]]+‖­]­­]00+0­0+]]]+‖­­0‖]0­­+0‖]0++0­]‖]+‖‖]­‖0­++0­0+]]]+‖­­0++]‖]0]+]]‖]00]]0"
      "]0­]]‖]00]0++‖+++]+0­0+]]]+‖­­00‖+‖]‖+‖]+‖]+++]]]0+0+0]­0‖*-y-=1+vYn/Ya~-=1+Gi?B7w6-=1+{5O4@/1-=1+3-=1+_-1"
      "Ls-=1+2\nPlease decode above message multiple times, password:1@2\n_____________________________________________"
      "____________________________________________________________________________________________________")
time.sleep(0.2)
print("""                    _____        _                                   _____  _   _   ____  ____  __   __ ____   _____  ___   ___   _   _           
                   |_   _|  ___ | |__   ___   ___   ___  _ __       | ____|| \ | | / ___||  _ \ \ \ / /|  _ \ |_   _||_ _| / _ \ | \ | |          
                     | |   / _ \| '_ \ / __| / _ \ / _ \| '_ \      |  _|  |  \| || |    | |_) | \ V / | |_) |  | |   | | | | | ||  \| |          
                     | |  |  __/| | | |\__ \|  __/|  __/| | | |     | |___ | |\  || |___ |  _ <   | |  |  __/   | |   | | | |_| || |\  |          
                     |_|   \___||_| |_||___/ \___| \___||_| |_|     |_____||_| \_| \____||_| \_\  |_|  |_|      |_|  |___| \___/ |_| \_|          

""")
#tprint('Tehseen     ENCRYPTION'.center(42))
print('>>>User Guide Manual is Given Above<<<'.center(130))
# ______________________________________________________________________________________________________________________
# >>>>> From 1 --> 4 ,6-->7 ENCRYPTION is being done <<<<<
while ans.lower() != 'stop':
    ans = input('\033[1mMODES\033[0m:\n\x1B[3m01.Random Word Encryption (password protected)\n02.Morse Code\n03.Custom '
                'Encryption\n04.Common Encryption\n05.Decryption\n06.Tehseen\'s Special Encryption\n07.Binaray Encryption\n'
                '08.Emoji Encryption\n09.Heart Encryption\n10.Colon Encryption\n11.YNK encryption\n12.Ect Encryption\n13.'
                'Book Encryption\n14.Clock Encryption\n15.3T Encryption\n16.NOTE:Enter "all" For all '
                'Type of encryption by giving single input.\x1B[0m\n>>>Please Enter>>>'
                ':')
    print(
        '______________________________________________________________________________________________________________'
        '___________________________________')
    # >>>>> My Best Encryption Programme <<<<<
    # ______________________________________________________________________________________________________________________
    if ans == 'all':
        inp = input('Enter message you want to Encrypt:')
    if ans == '1' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        pas = input('would you like to add password:(y)')
        pa_in = ''
        pa = 0
        temp_inp = inp
        # >>>>> password <<<<<
        if pas == 'y':
            pa = input('Enter your password:')
        output = ''
        inp = inp[::-1]
        # inp=list(inp)
        inp = inp.split(' ')
        if len(inp) > 0:
            for i in inp:
                # ind=inp.index(i)
                # if ind==0: #or i==' ' or ind==len(inp)-1:
                for k in range(3):
                    output += random.choice(r_letter)
                '''for j in i:
                    if j in replace_dic:
                        output+=replace_dic[j]'''
                for j in i:
                    if j in replace_dic:
                        output += replace_dic[j]
                    else:
                        if ord(j) % 2 == 0:
                            output += chr(ord(j) + r_alpha)
                        elif ord(j) % 2 != 0:
                            output += chr(ord(j) - r_alpha)
                for k in range(3):
                    output += random.choice(r_letter)
                output += '-=1+'
        if pas == 'y':
            for i in pa:
                # ind=inp.index(i)
                # if ind==0: #or i==' ' or ind==len(inp)-1:
                for k in range(3):
                    output += random.choice(r_letter)
                '''for j in i:
                    if j in replace_dic:
                        output+=replace_dic[j]'''
                for j in i:
                    if j in replace_dic:
                        output += replace_dic[j]
                    else:
                        if ord(j) % 2 == 0:
                            output += chr(ord(j) + r_alpha)
                        elif ord(j) % 2 != 0:
                            output += chr(ord(j) - r_alpha)
                for k in range(3):
                    output += random.choice(r_letter)
                output += '-=1+'
            output += str(len(pa))
            output += '-=1+'
            output += '_-1Ls'
            output += '-=1+'
        output += str(r_alpha)
        print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Best Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    # >>>>> MY OWN MORSE CODE PROGRAMME <<<<<
    if ans == '2' or ans == 'all':
        r = random.choice(r_morse)
        output = ''
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        for i in inp:
            for j in i:
                if j in b_morse:
                    output += d_morse[b_morse.index(j)]
            output += '–.¯'
        output += r
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Custom Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # >>>>> Custom Encryption <<<<<
    # ______________________________________________________________________________________________________________________
    if ans == '3' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        a = input('Enter 5 Unique letter String:')
        te = a
        e = 'tehsn'
        ds_1 = ds_cus
        for i in range(5):
            ds_1 = ds_1.replace(e[i], a[i])
        ds_1 = ds_1.split(',')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += ds_1[b.index(j)]
            output += ds_1[-1]
        output += te
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Morse Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # >>>>> Most Common Encryption <<<<<
    # ______________________________________________________________________________________________________________________
    if ans == '4' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for k in range(3):
                output += random.choice(r_letter_1)
            for j in i:
                if j in m_com:
                    output += m_com[j]
            for k in range(3):
                output += random.choice(r_letter_1)
            output += ' '
        output = output[::-1]
        output += 'lhaY'
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Common Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    # >>>> Tehseen's Encryption <<<<
    if ans == '6' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        e = 'tehsn'
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += d[b.index(j)]
            output += d[-1]
        output += d[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Morse Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    # >>>> Binaray Encryption <<<<
    if ans == '7' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += d_bin[b.index(j)]
            output += d_bin[-1]
        output += d_bin[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Binaray Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    # >>>>> Emoji Encryption <<<<
    if ans == '8' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in d_emoji:
                    output += d_emoji[j]
            output += '😾'
        output += "😿"
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Emoji Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    # 8>>>> Heart Encryption <<<<
    if ans == '9' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += h_list[b.index(j)]
            output += h_list[-1]
        output += h_list[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Heart Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    # >>>> Colon Encryption <<<<
    if ans == '10' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += co_list[b.index(j)]
            output += co_list[-1]
        output += co_list[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Colons Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    if ans == '11' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += ynk_list[b.index(j)]
            output += ynk_list[-1]
        output += ynk_list[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> YNK Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    if ans == '12' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += en_list[b.index(j)]
            output += en_list[-1]
        output += en_list[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Ect Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    if ans == '13' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += bk_list[b.index(j)]
            output += bk_list[-1]
        output += bk_list[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Book Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # ______________________________________________________________________________________________________________________
    if ans == '14' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += cl_list[b.index(j)]
            output += cl_list[-1]
        output += cl_list[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> Clock Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')
        inp = temp_inp
    # >>> TIC TAC TOE Encryption <<<
    if ans == '15' or ans == 'all':
        if ans != 'all':
            inp = input('Enter message you want to Encrypt:')
        temp_inp = inp
        inp = inp.split(' ')
        output = ''
        for i in inp:
            for j in i:
                if j in b:
                    output += d_3t[b.index(j)]
            output += d_3t[-1]
        output += d_3t[-2]
        if ans != 'all':
            print(f'>>>>> Input Message: {temp_inp}')
        print(f'>>>>> 3T Encrypted Message: {output}')
        print(
            '_________________________________________________________________________________________________________________________________________________')

    # ______________________________________________________________________________________________________________________
    # >>>>> ALL TYPES DECRYPTION PROGRAMME <<<<<
    # Auto Detect
    if ans == '5':
        d_inp = ''
        while d_inp != 'st':
            # d_inp = input('Enter Encrypted message to Decrypt:')
            '''if d_inp=='st':
                break'''
            d_inp = input('Enter Encrypted message to Decrypt:')
            if d_inp.find('@-@'):
                l_round = d_inp.split('@-@')
            else:
                l_round = list(d_inp)
            if d_inp == 'st':
                break
            d_inp_1 = d_inp.split(' : ')
            d_inp = d_inp_1[0]
            # temp_d_inp = d_inp
            for d_inp in l_round:
                temp_d_inp = d_inp
                if d_inp.find('-=1+') > -1:
                    d_inp = d_inp.split('-=1+')
                    r = int(d_inp[-1])
                    if d_inp[-2] == '_-1Ls':
                        pas = 'y'
                    else:
                        pas = 'n'
                    if pas == 'y':
                        pa_in = input('To Decrypt message enter password:')
                        out = ''
                        length = int(d_inp[-3])
                        d_inp.pop(-3)
                        temp_list_st = -2
                        temp_list_en = -1 * (length + 2)
                        r = int(d_inp[-1])
                        if r % 2 == 0:
                            m = 2
                        else:
                            m = 1
                        d_inp.pop(-2)
                        for i in d_inp[temp_list_st:temp_list_en:-1]:
                            k = list(i)
                            d_inp.remove(i)
                            i = k
                            for k in range(3):
                                i.pop(0)
                            for k in range(-3, 0):
                                i.pop(-1)
                            for j in i:
                                if ord(j) % 2 == 0 and m == 2:
                                    out += chr(ord(j) - r)
                                elif ord(j) % 2 != 0 and m == 2:
                                    out += chr(ord(j) + r)
                                elif ord(j) % 2 == 0 and m != 2:
                                    out += chr(ord(j) + r)
                                else:
                                    out += chr(ord(j) - r)
                        pa = out[::-1]
                    else:
                        password = 'confirm'
                    out = ''
                    '''for i in d_inp:
                        for k in range(3):
                            out+=''
                        for j in i:
                            if j in reverse_dic:
                                out+=reverse_dic[j]
                        for k in range(-1,-3,-1):
                            out += ''
                        out+=' ' '''
                    '''if pas=='y':
                        pa_in=input('To Decrypt message enter password:')'''
                    for i in range(1, 3):
                        if pa_in == pa:
                            password = 'confirm'
                            break
                        elif pas == 'y':
                            pa_in = input(
                                f'You entered wrong passsword only {3 - i} chances left, Plz Enter password again:')
                    if pa_in == pa:
                        password = 'confirm'
                    if pa_in != pa and pas == 'y':
                        print('>>>Wrong Password Multiple times<<<')
                        password = ''
                    if password == 'confirm':
                        if r % 2 == 0:
                            m = 2
                        else:
                            m = 1
                        d_inp.pop(-1)
                        for i in d_inp:
                            i = list(i)
                            for k in range(3):
                                i.pop(0)
                            for k in range(-3, 0):
                                i.pop(-1)
                            for j in i:
                                if ord(j) % 2 == 0 and m == 2:
                                    out += chr(ord(j) - r)
                                elif ord(j) % 2 != 0 and m == 2:
                                    out += chr(ord(j) + r)
                                elif ord(j) % 2 == 0 and m != 2:
                                    out += chr(ord(j) + r)
                                else:
                                    out += chr(ord(j) - r)
                            out += ' '
                        out = out[::-1]
                        print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                        if len(out) > 0:
                            print(f'>>>>>>>Decrypted Text: {out}')
                            print(
                                '_________________________________________________________________________________________________________________________________________________')
                        else:
                            print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 1:
                        d_inp = d_inp_1[1]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Morse Code Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp[-3::] in r_morse:
                    r = d_inp[-3::]
                    inp = []
                    out = ''
                    i = 0
                    while 1:
                        if len(d_inp) >= len(inp):
                            inp.append(d_inp[i:i + 3])
                            i += 3
                        else:
                            break
                    for i in inp:
                        if i in d_morse:
                            out += b_morse[d_morse.index(i)]
                    out = out[:-1]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 2:
                        d_inp = d_inp_1[2]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Most common Encryption's Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('lhaY') > -1:  # d_inp.find(' ') > -1 or
                    # else: #d_inp.find()>-1:
                    # d_inp = input()
                    if d_inp.find('lhaY') > -1:
                        d_inp = d_inp[:-4]
                    d_inp = d_inp[::-1]
                    d_inp = d_inp.split(' ')
                    out = ''
                    for i in d_inp:
                        i = list(i)
                        for k in range(3):
                            i.pop(0)
                        for k in range(-3, 0):
                            i.pop(-1)
                        for j in i:
                            if j in m_com_r:
                                out += m_com_r[j]
                        out += ' '
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                if d_inp.find('1100000') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-7]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 7])
                            i += 7
                        else:
                            break
                    for i in inp:
                        if i in d_bin:
                            out += b[d_bin.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Emoji Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('😾') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-1]
                    for i in d_inp:
                        if i in r_emoji:
                            out += r_emoji[i]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Heart Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('🖤💛💙💜🤎') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-5]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 4])
                            i += 4
                        else:
                            break
                    for i in inp:
                        if i in h_list:
                            out += b[h_list.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Colon Encryption's Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find(';;;;;;:') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-7]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 7])
                            i += 7
                        else:
                            break
                    for i in inp:
                        if i in co_list:
                            out += b[co_list.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> YNK Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('YOU NEVER know.You never Know.') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-30]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 30])
                            i += 30
                        else:
                            break
                    for i in inp:
                        if i in ynk_list:
                            out += b[ynk_list.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Encrypted Type Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('EncrypteD.encrypTED.') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-20]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 20])
                            i += 20
                        else:
                            break
                    for i in inp:
                        if i in en_list:
                            out += b[en_list.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Book Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('📔📙📗📕📒') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-5]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 4])
                            i += 4
                        else:
                            break
                    for i in inp:
                        if i in bk_list:
                            out += b[bk_list.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>> Clock Encryption's Decryption <<<<
                # ______________________________________________________________________________________________________________________
                if d_inp.find('🕧🕛🕕🕒') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-4]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 4])
                            i += 4
                        else:
                            break
                    for i in inp:
                        if i in cl_list:
                            out += b[cl_list.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
# >>> 3T Decryption <<<
                if d_inp.find('❌❌⭕⭕⭕⭕⭕') > -1:
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-7]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 7])
                            i += 7
                        else:
                            break
                    for i in inp:
                        if i in d_3t:
                            out += b[d_3t.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')
                    if len(d_inp_1) > 3:
                        d_inp = d_inp_1[3]
                        temp_d_inp = d_inp
                    else:
                        d_inp = ''
                # >>>>> Custom Encryption's Decryption <<<<<
                # ______________________________________________________________________________________________________________________
                else:
                    if len(d_inp) > 0:
                        temp_else = 1
                if len(d_inp_1) > 3 or temp_else == 1:
                    temp_else = 0
                    or_a = 'tehsn'
                    te = d_inp[-5::]
                    ds_2 = ds_cus
                    for i in range(5):
                        if len(d_inp) > 5:
                            ds_2 = ds_2.replace(or_a[i], te[i])
                    # else:
                    #    print('Wrong input')
                    ds_2 = ds_2.split(',')
                    inp = []
                    out = ''
                    i = 0
                    d_inp = d_inp[:-5]
                    while 1:
                        if len(d_inp) > len(inp):
                            inp.append(d_inp[i:i + 4])
                            i += 4
                        else:
                            break
                    for i in inp:
                        if i in ds_2:
                            out += b[ds_2.index(i)]
                    print(f'>>>>>>>Encrypted Text: {temp_d_inp}')
                    if len(out) > 0:
                        print(f'>>>>>>>Decrypted Text: {out}')
                        print(
                            '_________________________________________________________________________________________________________________________________________________')
                    else:
                        print('May Be your Encrypted Text is not Correct>>>')