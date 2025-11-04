usuContra=[["Manuel","canMorto"],["pepe","usuaya"]]

def comprobarUsuario(listaUsuarioContrasinal):
    existeUsuario = False
    nomeUsuario =input("Cal e o nome de usuario? ")
    contrasinal = input("Cal é o contrasinal? ")
    for usuarioContrasinal in listaUsuarioContrasinal:
        if usuarioContrasinal[0] == nomeUsuario:
            if usuarioContrasinal[1] == contrasinal:
                existeUsuario = True
    return  existeUsuario

existe = comprobarUsuario(usuContra)

if existe:
    print("Usuario valido")
else:
    print("Contrasinal ou usuario erroneo")

def comprobarLonxitude (contrasinal):
    if len(contrasinal) > 8:
        return True
    else:
        return False

def comprobarMaisculasContrasinal(contrasinal):
    for letra in contrasinal:
        if letra == letra.upper():
            return True

def comprobarNumerosEnContrasinal(contrasinal):
    for caracter in contrasinal:
        if caracter.isNumeric():
            return True


def comprobarCaracteresEspeciais (contrasinal):
    especiais = '!@$%&*_'
    for caracter in contrasinal:
        if simbolo in especiais:
            if caracter == simbolo:
                return True