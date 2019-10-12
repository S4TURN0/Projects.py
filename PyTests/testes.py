
id = 0
for x in range(1,5):
    id = id + 1 #Quantidade de usuarios
    user = str(input("User: "))
    email = str(input("Email: "))
    password = str(input("Senha: "))
    dici = {"id" : id,
        "user" : user, 
        "email" : email, 
        "password" : password}
    print (dici["id"])
