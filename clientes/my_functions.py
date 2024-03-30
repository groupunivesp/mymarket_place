def confere_senha(senha, senha1):
    if senha == senha1:
        return True
    else:
        return False
    
def tamanho_valid(senha):
    if len(senha) >= 8:
        return True
    else:
        return False
    
