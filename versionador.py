
posicoes = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

qtde_posicoes = len(posicoes)

versao = 650
"""
A - Z = 1 - 26
A[A-Z] = 27 - 52
B[A-Z] = 53- 78
C[A-Z] = 79 - 104
D[A-Z] = 105 - 130
E[A-Z] = 131 - 156
F[A-Z] = 157 - 182
Z[A-Z] = - 650
"""
v_1 = int(versao / qtde_posicoes)

if (versao % qtde_posicoes) == 0 :
    v_1 = v_1 -1

v_2 = versao - ( qtde_posicoes  * v_1 )

if(v_2 > qtde_posicoes):
    v_2 = int(v_2 / qtde_posicoes)

print(posicoes[v_1 - 1]+posicoes[v_2 - 1])

def letter_to_number(string):
    number = 0
    for char in string:
        number = number * 256 + ord(char)
    return number

def number_to_letter(number):
    string = ""
    while number > 0:
        number, remainder = divmod(number, 256)
        string = chr(remainder) + string
    return string.encode('latin-1').decode('latin-1')

s = 'EuAmoVocê'
encoded_str = str(letter_to_number(s))
print(encoded_str)
decoded_str = number_to_letter(int(encoded_str))
print(decoded_str)  # Output: EuAmoVocê

# Example usage:
#print(number_to_letter(1213273961775))
#print(reverse_encoding('1213273961775'))
#print(letter_to_number("EuAmoVoce"))
