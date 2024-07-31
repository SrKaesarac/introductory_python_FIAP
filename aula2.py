access_level = input("Qual seu nivel de acesso? (ADM, USER, GUEST)").upper()
gender = input("Qual seu genero? (MASC, FEM)").upper()

if gender == "MASC":
    if access_level == "ADM":
        print("Ola Administrador!")
    elif access_level == "USER":
        print("Ola Usuario!")
    elif access_level == "GUEST":
        print("Ola Convidado!")
elif gender == "FEM":
    if access_level == "ADM":
        print("Ola Administradora!")
    elif access_level == "USER":
        print("Ola Usuaria!")
    elif access_level == "GUEST":
        print("Ola Convidada!")
else:
    print("Ola Desconhecido!")