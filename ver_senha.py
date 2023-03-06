contador=0
while contador == 0:
    print("Bem-vindo ao verificador de senha")
    senha1=input("Senha:")
    
    ver_senha=input("Verifique a sua senha:")
    if senha1 == ver_senha:
        print("As senhas coincidem.")
        break
    elif senha1 != ver_senha:
        print("As senhas coincidem")
        break
     
        