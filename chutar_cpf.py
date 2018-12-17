def validaCpf(cpf, d1=0, d2=0, i=0):
    while i < 10:
        d1, d2, i = (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1, (
                d2 + (int(cpf[i]) * (11 - i))) % 11, i + 1
    return (int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11 - d2 if d2 > 1 else 0))

if __name__ == '__main__':
    # xxx.452.748-44
    cpf_string = input("Digite o cpf, utilize x onde não souber o dígito: ")
    cpf_string = cpf_string.replace(".", "").replace("-", "").replace(" ", "")

    number = cpf_string.count('x')


    for i in range (1, 10**(number)-1):
        cpf = cpf_string.replace("x", "")
        cpf = (str(i)+cpf).zfill(11)
        if validaCpf(cpf):
            print(cpf)

