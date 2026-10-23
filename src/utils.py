def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    # Completar
    try:
        int(id_usuario)
        return True
    except ValueError:
        return False
    return True

def validar_nombre(nombre:str):
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    # Completar
    return True

def validar_email(email:str):
    """
    Valida que email sea un correo válido"""
    # Completar
    return True