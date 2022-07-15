from numpy import void


def errorText(text : str) -> str:
    ''' Returns input text as a bold, red-colored text. '''
    red = '\033[1;31m'
    end = '\033[0m'
    return f'{red}{text}{end}'

def testSetup(squares : list, unitlist : list, units : dict, peers : dict) -> void: 
    ''' Asserts that the setup lists and dictionaries were setup correctly. '''
    expected_squares = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
    #f'Got {squares}'
    expected_unitlist = [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']]
    #f'Got {unitlist}'
    expected_units = {'A1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'A2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'A3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'A4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'A5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'A6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'A7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'A8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'A9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'B1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'B2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'B3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'B4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'B5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'B6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'B7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'B8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'B9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'C1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'C2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'C3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']], 'C4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'C5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'C6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']], 'C7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'C8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'C9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9']], 'D1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'D2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'D3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'D4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'D5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'D6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'D7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'D8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'D9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'E1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'E2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'E3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'E4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'E5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'E6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'E7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'E8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'E9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'F1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'F2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'F3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']], 'F4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'F5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'F6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6']], 'F7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'F8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'F9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9']], 'G1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'G2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'G3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'G4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'G5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'G6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'G7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'G8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'G9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'H1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'H2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'H3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'H4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'H5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'H6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'H7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'H8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'H9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'I1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'I2': [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'I3': [['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3']], 'I4': [['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'I5': [['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'I6': [['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6']], 'I7': [['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'I8': [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']], 'I9': [['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']]}
    #f'Got {units}'
    expected_peers = {'A1': {'B3', 'A2', 'A9', 'E1', 'A4', 'A5', 'A7', 'A3', 'H1', 'A8', 'C3', 'C1', 'C2', 'I1', 'D1', 'F1', 'B1', 'A6', 'G1', 'B2'}, 'A2': {'B3', 'A1', 'A9', 'A4', 'A5', 'A7', 'A3', 'A8', 'C3', 'C1', 'C2', 'E2', 'F2', 'B1', 'A6', 'D2', 'G2', 'H2', 'I2', 'B2'}, 'A3': {'B3', 'A2', 'F3', 'I3', 'A9', 'A4', 'A5', 'A7', 'A8', 'C3', 'C1', 'D3', 'C2', 'E3', 'H3', 'G3', 'B1', 'A6', 'A1', 'B2'}, 'A4': {'I4', 'A2', 'B6', 'A9', 'A5', 'A7', 'H4', 'A3', 'A8', 'C6', 'D4', 'F4', 'C4', 'G4', 'E4', 'A6', 'A1', 'C5', 'B5', 'B4'}, 'A5': {'A2', 'B6', 'H5', 'A9', 'F5', 'A4', 'A7', 'A3', 'A8', 'C6', 'E5', 'C4', 'G5', 'D5', 'A6', 'I5', 'A1', 'C5', 'B5', 'B4'}, 'A6': {'A2', 'B6', 'F6', 'D6', 'A9', 'A4', 'A5', 'A7', 'A3', 'C6', 'A8', 'H6', 'C4', 'G6', 'E6', 'I6', 'A1', 'C5', 'B5', 'B4'}, 'A7': {'A2', 'C7', 'A9', 'I7', 'A4', 'A5', 'A3', 'B9', 'A8', 'B7', 'H7', 'F7', 'D7', 'C8', 'B8', 'C9', 'A6', 'G7', 'A1', 'E7'}, 'A8': {'A2', 'G8', 'C7', 'A9', 'I8', 'A4', 'A5', 'A7', 'A3', 'B9', 'D8', 'B7', 'H8', 'E8', 'C8', 'B8', 'C9', 'A6', 'A1', 'F8'}, 'A9': {'A2', 'C7', 'A4', 'A5', 'B9', 'A3', 'A7', 'A8', 'F9', 'I9', 'E9', 'B7', 'D9', 'H9', 'C8', 'B8', 'C9', 'A6', 'G9', 'A1'}, 'B1': {'B3', 'A2', 'B6', 'E1', 'B9', 'A3', 'H1', 'C3', 'C1', 'C2', 'B7', 'I1', 'D1', 'F1', 'B8', 'G1', 'A1', 'B5', 'B4', 'B2'}, 'B2': {'B3', 'A2', 'B6', 'A1', 'B9', 'A3', 'C3', 'C1', 'C2', 'B7', 'E2', 'I2', 'F2', 'B8', 'B1', 'D2', 'G2', 'H2', 'B5', 'B4'}, 'B3': {'A2', 'F3', 'B6', 'I3', 'B9', 'A3', 'C3', 'C1', 'D3', 'C2', 'B7', 'E3', 'B8', 'H3', 'G3', 'B1', 'A1', 'B5', 'B4', 'B2'}, 'B4': {'B3', 'I4', 'B6', 'A4', 'A5', 'B9', 'H4', 'C6', 'F4', 'D4', 'C4', 'B7', 'G4', 'B8', 'B1', 'A6', 'E4', 'C5', 'B5', 'B2'}, 'B5': {'B3', 'B6', 'H5', 'F5', 'A5', 'A4', 'B9', 'C6', 'E5', 'C4', 'B7', 'G5', 'D5', 'B8', 'B1', 'A6', 'I5', 'C5', 'B4', 'B2'}, 'B6': {'B3', 'F6', 'D6', 'A4', 'A5', 'B9', 'C6', 'H6', 'C4', 'B7', 'G6', 'B8', 'E6', 'I6', 'B1', 'A6', 'C5', 'B5', 'B4', 'B2'}, 'B7': {'B3', 'B6', 'C7', 'A9', 'I7', 'A7', 'B9', 'A8', 'H7', 'F7', 'E7', 'D7', 'C8', 'B8', 'C9', 'B1', 'G7', 'B5', 'B4', 'B2'}, 'B8': {'B3', 'G8', 'B6', 'C7', 'A9', 'I8', 'B9', 'A7', 'A8', 'D8', 'B7', 'H8', 'E8', 'C8', 'C9', 'B1', 'B4', 'F8', 'B5', 'B2'}, 'B9': {'B3', 'B6', 'C7', 'A9', 'A7', 'A8', 'F9', 'I9', 'E9', 'B7', 'D9', 'H9', 'C8', 'B8', 'C9', 'B1', 'G9', 'B5', 'B4', 'B2'}, 'C1': {'B3', 'A2', 'C7', 'E1', 'A3', 'H1', 'C6', 'C3', 'C4', 'C2', 'I1', 'D1', 'C8', 'F1', 'C9', 'B1', 'G1', 'A1', 'C5', 'B2'}, 'C2': {'B3', 'A2', 'A1', 'C7', 'A3', 'C6', 'C3', 'C1', 'C4', 'E2', 'C8', 'F2', 'C9', 'B1', 'D2', 'G2', 'H2', 'C5', 'I2', 'B2'}, 'C3': {'B3', 'A2', 'F3', 'I3', 'C7', 'A3', 'C6', 'C1', 'C4', 'C2', 'D3', 'E3', 'C8', 'H3', 'G3', 'C9', 'B1', 'A1', 'C5', 'B2'}, 'C4': {'I4', 'B6', 'C7', 'A4', 'A5', 'H4', 'C6', 'C3', 'D4', 'C1', 'C2', 'F4', 'G4', 'C8', 'C9', 'E4', 'A6', 'C5', 'B5', 'B4'}, 'C5': {'B6', 'H5', 'C7', 'F5', 'A5', 'A4', 'C6', 'C3', 'C1', 'E5', 'C2', 'C4', 'G5', 'D5', 'C8', 'C9', 'A6', 'I5', 'B5', 'B4'}, 'C6': {'B6', 'F6', 'D6', 'C7', 'A4', 'A5', 'C3', 'C1', 'C4', 'C2', 'H6', 'C8', 'G6', 'E6', 'I6', 'C9', 'A6', 'C5', 'B5', 'B4'}, 'C7': {'A9', 'I7', 'A7', 'B9', 'C6', 'A8', 'C1', 'C3', 'C2', 'B7', 'C4', 'H7', 'F7', 'D7', 'C8', 'B8', 'C9', 'G7', 'C5', 'E7'}, 'C8': {'G8', 'C7', 'A9', 'I8', 'A7', 'B9', 'A8', 'C6', 'C1', 'C3', 'C2', 'D8', 'B7', 'C4', 'H8', 'E8', 'B8', 'C9', 'C5', 'F8'}, 'C9': {'C7', 'A9', 'B9', 'A7', 'A8', 'C6', 'C1', 'I9', 'C2', 'B7', 'C3', 'F9', 'C4', 'E9', 'D9', 'H9', 'C8', 'B8', 'G9', 'C5'}, 'D1': {'F3', 'D6', 'E1', 'H1', 'D4', 'C1', 'D8', 'D3', 'D9', 'I1', 'E3', 'D7', 'D5', 'F1', 'F2', 'B1', 'D2', 'G1', 'A1', 'E2'}, 'D2': {'A2', 'F3', 'D6', 'E1', 'D4', 'D3', 'D8', 'C2', 'D9', 'D1', 'E2', 'E3', 'D7', 'D5', 'F1', 'F2', 'G2', 'H2', 'I2', 'B2'}, 'D3': {'B3', 'F3', 'D6', 'I3', 'E1', 'A3', 'C3', 'D4', 'D8', 'D9', 'D1', 'E3', 'D7', 'D5', 'F1', 'F2', 'H3', 'G3', 'D2', 'E2'}, 'D4': {'I4', 'F6', 'D6', 'F5', 'A4', 'H4', 'F4', 'E5', 'D8', 'D3', 'D9', 'C4', 'D1', 'G4', 'D7', 'D5', 'E6', 'E4', 'D2', 'B4'}, 'D5': {'F6', 'H5', 'D6', 'F5', 'A5', 'F4', 'D4', 'E5', 'D8', 'D3', 'D9', 'D1', 'D7', 'G5', 'E6', 'E4', 'D2', 'I5', 'C5', 'B5'}, 'D6': {'B6', 'F6', 'F5', 'C6', 'F4', 'D4', 'E5', 'D8', 'D3', 'D9', 'H6', 'D1', 'D7', 'D5', 'G6', 'E6', 'I6', 'E4', 'A6', 'D2'}, 'D7': {'D6', 'C7', 'I7', 'A7', 'F9', 'D4', 'E9', 'D8', 'B7', 'D9', 'H7', 'D1', 'D3', 'F7', 'E8', 'D5', 'D2', 'G7', 'F8', 'E7'}, 'D8': {'G8', 'D6', 'I8', 'A8', 'F9', 'D4', 'E9', 'D9', 'H8', 'D3', 'D1', 'F7', 'E8', 'D7', 'C8', 'D5', 'B8', 'D2', 'F8', 'E7'}, 'D9': {'D6', 'A9', 'B9', 'F9', 'D4', 'I9', 'D8', 'D3', 'E9', 'D1', 'H9', 'F7', 'E8', 'D7', 'D5', 'C9', 'G9', 'D2', 'F8', 'E7'}, 'E1': {'F3', 'H1', 'C1', 'E5', 'D3', 'E9', 'I1', 'D1', 'E7', 'E3', 'E8', 'F1', 'F2', 'E6', 'B1', 'E4', 'D2', 'G1', 'A1', 'E2'}, 'E2': {'A2', 'B2', 'F3', 'E1', 'E5', 'D3', 'C2', 'E9', 'D1', 'E3', 'E8', 'F1', 'F2', 'E6', 'E4', 'D2', 'G2', 'H2', 'I2', 'E7'}, 'E3': {'B3', 'F3', 'I3', 'E1', 'A3', 'C3', 'E5', 'E9', 'D3', 'D1', 'E2', 'E8', 'F1', 'F2', 'E6', 'H3', 'G3', 'E4', 'D2', 'E7'}, 'E4': {'I4', 'F6', 'D6', 'E1', 'F5', 'A4', 'H4', 'F4', 'D4', 'E5', 'E9', 'C4', 'E2', 'E3', 'E8', 'G4', 'D5', 'E6', 'B4', 'E7'}, 'E5': {'F6', 'H5', 'D6', 'E1', 'F5', 'A5', 'F4', 'D4', 'E9', 'E2', 'E3', 'E8', 'G5', 'D5', 'E6', 'E4', 'I5', 'C5', 'B5', 'E7'}, 'E6': {'B6', 'F6', 'D6', 'E1', 'F5', 'C6', 'F4', 'D4', 'E5', 'E9', 'H6', 'E2', 'E3', 'E8', 'D5', 'G6', 'I6', 'E4', 'A6', 'E7'}, 'E7': {'C7', 'E1', 'I7', 'A7', 'F9', 'E5', 'E9', 'D8', 'B7', 'D9', 'H7', 'F7', 'E3', 'E8', 'D7', 'E6', 'E4', 'G7', 'F8', 'E2'}, 'E8': {'G8', 'E1', 'I8', 'A8', 'F9', 'E5', 'E9', 'D8', 'D9', 'H8', 'F7', 'E2', 'E3', 'D7', 'C8', 'B8', 'E6', 'E4', 'F8', 'E7'}, 'E9': {'A9', 'E1', 'B9', 'F9', 'E5', 'I9', 'D8', 'D9', 'H9', 'F7', 'E2', 'E3', 'E8', 'D7', 'E6', 'C9', 'E4', 'G9', 'F8', 'E7'}, 'F1': {'F3', 'F6', 'E1', 'F5', 'H1', 'F9', 'F4', 'C1', 'D3', 'F7', 'I1', 'D1', 'E3', 'F2', 'B1', 'D2', 'G1', 'A1', 'F8', 'E2'}, 'F2': {'A2', 'F3', 'F6', 'E1', 'F5', 'F9', 'F4', 'D3', 'C2', 'F7', 'D1', 'E2', 'E3', 'F1', 'D2', 'G2', 'H2', 'F8', 'I2', 'B2'}, 'F3': {'B3', 'F6', 'I3', 'E1', 'F5', 'A3', 'F9', 'C3', 'F4', 'D3', 'F7', 'D1', 'E3', 'F1', 'F2', 'H3', 'G3', 'D2', 'F8', 'E2'}, 'F4': {'I4', 'F3', 'F6', 'D6', 'F5', 'A4', 'H4', 'F9', 'D4', 'E5', 'C4', 'F7', 'G4', 'D5', 'F1', 'F2', 'E6', 'E4', 'F8', 'B4'}, 'F5': {'F3', 'F6', 'H5', 'D6', 'A5', 'F9', 'F4', 'D4', 'E5', 'F7', 'G5', 'D5', 'F1', 'F2', 'E6', 'E4', 'F8', 'I5', 'C5', 'B5'}, 'F6': {'B6', 'F3', 'D6', 'F5', 'C6', 'F9', 'D4', 'F4', 'E5', 'H6', 'F7', 'D5', 'F1', 'F2', 'G6', 'E6', 'I6', 'E4', 'A6', 'F8'}, 'F7': {'F3', 'F6', 'C7', 'I7', 'F5', 'A7', 'F9', 'F4', 'E9', 'D8', 'B7', 'D9', 'H7', 'E8', 'D7', 'F1', 'F2', 'G7', 'F8', 'E7'}, 'F8': {'G8', 'F3', 'F6', 'I8', 'F5', 'A8', 'F9', 'F4', 'E9', 'D8', 'H8', 'D9', 'F7', 'E8', 'D7', 'C8', 'F1', 'F2', 'B8', 'E7'}, 'F9': {'F3', 'F6', 'A9', 'F5', 'B9', 'F4', 'I9', 'D8', 'E9', 'D9', 'H9', 'F7', 'E8', 'D7', 'F1', 'F2', 'C9', 'G9', 'F8', 'E7'}, 'G1': {'A1', 'I3', 'E1', 'H1', 'C1', 'I1', 'D1', 'G4', 'G5', 'F1', 'G6', 'H3', 'G3', 'B1', 'G9', 'G7', 'G2', 'H2', 'G8', 'I2'}, 'G2': {'A2', 'I3', 'H1', 'C2', 'I1', 'E2', 'G4', 'G5', 'F2', 'G6', 'H3', 'G3', 'D2', 'G9', 'G1', 'G7', 'H2', 'G8', 'I2', 'B2'}, 'G3': {'B3', 'F3', 'I3', 'A3', 'H1', 'C3', 'D3', 'I1', 'E3', 'G4', 'G5', 'G6', 'H3', 'G9', 'G1', 'G7', 'G2', 'H2', 'G8', 'I2'}, 'G4': {'I4', 'H5', 'A4', 'H4', 'F4', 'D4', 'H6', 'C4', 'G5', 'G6', 'G3', 'I6', 'E4', 'G9', 'I5', 'G1', 'G7', 'G2', 'G8', 'B4'}, 'G5': {'I4', 'G8', 'H5', 'F5', 'A5', 'H4', 'E5', 'H6', 'G4', 'D5', 'G6', 'G3', 'I6', 'G9', 'I5', 'G1', 'G7', 'G2', 'C5', 'B5'}, 'G6': {'I4', 'B6', 'F6', 'D6', 'H5', 'H4', 'C6', 'H6', 'G4', 'G5', 'E6', 'G3', 'I6', 'A6', 'G9', 'G1', 'G7', 'G2', 'I5', 'G8'}, 'G7': {'C7', 'I8', 'I7', 'A7', 'I9', 'H8', 'B7', 'H7', 'H9', 'F7', 'G4', 'D7', 'G5', 'G6', 'G3', 'G9', 'G1', 'G2', 'G8', 'E7'}, 'G8': {'I8', 'I7', 'A8', 'I9', 'D8', 'H8', 'H7', 'H9', 'E8', 'G4', 'G5', 'C8', 'B8', 'G6', 'G3', 'G9', 'G1', 'G7', 'G2', 'F8'}, 'G9': {'A9', 'I8', 'I7', 'B9', 'F9', 'I9', 'E9', 'D9', 'H7', 'H9', 'H8', 'G4', 'G5', 'G6', 'G3', 'C9', 'G1', 'G7', 'G2', 'G8'}, 'H1': {'A1', 'H5', 'I3', 'E1', 'H4', 'C1', 'H6', 'H8', 'H7', 'H9', 'I1', 'D1', 'F1', 'H3', 'G3', 'B1', 'G1', 'G2', 'H2', 'I2'}, 'H2': {'A2', 'H5', 'I3', 'H4', 'H1', 'H6', 'C2', 'H8', 'H7', 'H9', 'I1', 'E2', 'F2', 'H3', 'G3', 'D2', 'G1', 'G2', 'I2', 'B2'}, 'H3': {'B3', 'F3', 'H5', 'I3', 'H4', 'A3', 'H1', 'C3', 'D3', 'H8', 'H7', 'H9', 'H6', 'I1', 'E3', 'G3', 'G1', 'G2', 'H2', 'I2'}, 'H4': {'I4', 'H5', 'A4', 'H1', 'F4', 'D4', 'C4', 'H8', 'H6', 'H9', 'H7', 'G4', 'G5', 'G6', 'H3', 'I6', 'E4', 'I5', 'H2', 'B4'}, 'H5': {'I4', 'F5', 'A5', 'H4', 'H1', 'E5', 'H6', 'H8', 'H7', 'H9', 'G4', 'G5', 'D5', 'G6', 'H3', 'I6', 'I5', 'H2', 'C5', 'B5'}, 'H6': {'I4', 'B6', 'F6', 'D6', 'H5', 'H4', 'H1', 'C6', 'H8', 'H7', 'H9', 'G4', 'G5', 'G6', 'E6', 'H3', 'I6', 'A6', 'I5', 'H2'}, 'H7': {'H5', 'C7', 'I8', 'I7', 'A7', 'H4', 'H1', 'I9', 'H6', 'B7', 'H8', 'H9', 'F7', 'D7', 'H3', 'G9', 'G7', 'H2', 'G8', 'E7'}, 'H8': {'G8', 'H5', 'I8', 'I7', 'H4', 'H1', 'A8', 'I9', 'D8', 'H6', 'H7', 'H9', 'E8', 'C8', 'B8', 'H3', 'G9', 'G7', 'H2', 'F8'}, 'H9': {'H5', 'A9', 'I8', 'I7', 'B9', 'H4', 'H1', 'F9', 'I9', 'H6', 'H8', 'E9', 'D9', 'H7', 'H3', 'C9', 'G9', 'G7', 'H2', 'G8'}, 'I1': {'I4', 'A1', 'I3', 'E1', 'I8', 'I7', 'H1', 'C1', 'I9', 'D1', 'F1', 'H3', 'G3', 'I6', 'B1', 'I5', 'G1', 'G2', 'H2', 'I2'}, 'I2': {'I4', 'A2', 'I3', 'I8', 'I7', 'H1', 'I9', 'C2', 'I1', 'E2', 'F2', 'H3', 'G3', 'I6', 'D2', 'I5', 'G1', 'G2', 'H2', 'B2'}, 'I3': {'B3', 'I4', 'F3', 'I8', 'I7', 'A3', 'H1', 'C3', 'I9', 'D3', 'I1', 'E3', 'H3', 'G3', 'I6', 'I5', 'G1', 'G2', 'H2', 'I2'}, 'I4': {'H5', 'I3', 'I8', 'I7', 'A4', 'H4', 'F4', 'D4', 'I9', 'C4', 'H6', 'I1', 'G4', 'G5', 'G6', 'I6', 'B4', 'E4', 'I5', 'I2'}, 'I5': {'I4', 'H5', 'I3', 'I8', 'I7', 'F5', 'A5', 'H4', 'E5', 'I9', 'H6', 'I1', 'G4', 'G5', 'D5', 'G6', 'I6', 'C5', 'B5', 'I2'}, 'I6': {'I4', 'B6', 'F6', 'D6', 'H5', 'I3', 'I8', 'I7', 'H4', 'C6', 'I9', 'H6', 'I1', 'G4', 'G5', 'G6', 'E6', 'A6', 'I5', 'I2'}, 'I7': {'I4', 'I3', 'C7', 'I8', 'A7', 'I9', 'H8', 'B7', 'H7', 'H9', 'I1', 'F7', 'D7', 'I6', 'G9', 'I5', 'G7', 'G8', 'I2', 'E7'}, 'I8': {'I4', 'G8', 'I3', 'I7', 'A8', 'I9', 'D8', 'H8', 'H7', 'H9', 'I1', 'E8', 'C8', 'B8', 'I6', 'G9', 'I5', 'G7', 'F8', 'I2'}, 'I9': {'I4', 'I3', 'A9', 'I8', 'I7', 'B9', 'F9', 'E9', 'D9', 'H7', 'H9', 'I1', 'H8', 'C9', 'I6', 'G9', 'I5', 'G7', 'G8', 'I2'}}
    #f'Got {peers}'

    assert squares == expected_squares, f"{errorText('Square list does not have the expected values. Got ')}{squares}"
    assert unitlist == expected_unitlist, f"{errorText('Unit list does not have the expected values. Got ')}{unitlist}"
    assert units == expected_units, f"{errorText('Units dictionary does not have the expected values. Got ')}{units}"
    assert peers == expected_peers, f"{errorText('Peers dictionary does not have the expected values. Got ')}{peers}"