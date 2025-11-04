# Lista de usuarios y contraseñas válidas
usuContra = [["Manuel", "canMorto"], ["pepe", "usuaya"]]


# Función para comprobar si el usuario y contraseña existen

def comprobarUsuario(listaUsuarioContrasinal):
    existeUsuario = False
    nomeUsuario = input("¿Cuál es el nombre de usuario? ")
    contrasinal = input("¿Cuál es la contraseña? ")

    # Recorre toda la lista de usuarios
    for usuarioContrasinal in listaUsuarioContrasinal:
        # Comprueba si el nombre coincide
        if usuarioContrasinal[0] == nomeUsuario:
            if usuarioContrasinal[1] == contrasinal:
                existeUsuario = True
    return existeUsuario

# Llamada a la función para comprobar usuario y contraseña
existe = comprobarUsuario(usuContra)

# Muestra un mensaje según el resultado
if existe:
    print("Usuario válido")
else:
    print("Contraseña o usuario erróneo")


# Función para comprobar la longitud del contraseña

def comprobarLonxitude(contrasinal):
    if len(contrasinal) > 8:
        return True
    else:
        return False


# Función para comprobar si el contraseña contiene mayúsculas

def comprobarMaisculasContrasinal(contrasinal):
    # Recorre cada letra del contraseña
    for letra in contrasinal:
        if letra == letra.upper() and letra.isalpha():
            return True
    return False


# Función para comprobar si el contraseña contiene números

def comprobarNumerosEnContrasinal(contrasinal):
    # Recorre cada carácter del contraseña
    for caracter in contrasinal:
        if caracter.isnumeric():
            return True
    return False


# Función para comprobar si hay caracteres especiales

def comprobarCaracteresEspeciais(contrasinal):
    especiais = '!@$%&*_'
    for caracter in contrasinal:
        if caracter in especiais:
            return True
    return False