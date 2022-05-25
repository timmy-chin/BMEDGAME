def protein_translation(DNA):
    RNA_strand = []
    for letter in DNA:
        if letter == 'G':
            RNA_strand.append('C')
        elif letter == 'C':
            RNA_strand.append('G')
        elif letter == 'A':
            RNA_strand.append('U')
        elif letter == 'T':
            RNA_strand.append('A')
    translation = [''.join(RNA_strand[i:i+3]) for i in range(0,len(DNA), 3)]

    code_list = []
    protein_list = []
    count = 0

    for one in ['U', 'C', 'A',
                'G']:  # Creating Code List with its index corresponding to another list named protein_list
        for two in ['U', 'C', 'A', 'G']:
            for three in ['U', 'C', 'A', 'G']:
                letter_str = f'{one}{two}{three}'
                code_list.append(letter_str)
                count += 1
                if count <= 2:
                    protein_list.append('F')
                elif count <= 4:
                    protein_list.append('L')
                elif count <= 8:
                    protein_list.append('S')
                elif count <= 10:
                    protein_list.append('Y')
                elif count <= 12:
                    protein_list.append('Stop')
                elif count <= 14:
                    protein_list.append('C')
                elif count <= 15:
                    protein_list.append('Stop')
                elif count <= 16:
                    protein_list.append('W')
                elif count <= 20:
                    protein_list.append('L')
                elif count <= 24:
                    protein_list.append('P')
                elif count <= 26:
                    protein_list.append('H')
                elif count <= 28:
                    protein_list.append('Q')
                elif count <= 32:
                    protein_list.append('R')
                elif count <= 35:
                    protein_list.append('I')
                elif count <= 36:
                    protein_list.append('M')
                elif count <= 40:
                    protein_list.append('T')
                elif count <= 42:
                    protein_list.append('N')
                elif count <= 44:
                    protein_list.append('K')
                elif count <= 46:
                    protein_list.append('S')
                elif count <= 48:
                    protein_list.append('R')
                elif count <= 52:
                    protein_list.append('V')
                elif count <= 56:
                    protein_list.append('A')
                elif count <= 58:
                    protein_list.append('D')
                elif count <= 60:
                    protein_list.append('E')
                elif count <= 64:
                    protein_list.append('G')

    protein = [protein_list[code_list.index(code)] for code in translation]
    return f"{' '.join(translation)}  ---->  {' '.join(protein)}"



