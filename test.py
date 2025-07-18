# def decorar_partediente(funcion_torta):
#     def torta_decorada():
#         funcion_torta()
#         print("Agregando 🍓 con crema de leche 🥛")
#         print("Torta lista para servir 🎂🍰")
        
#     return torta_decorada

# @decorar_partediente
# def hacer_torta():
#     print("Decorando una torta pero esta vez, con chocolate 🍩")

# hacer_torta()

#Es una funcion que recibe otra funcion como entrada--> parametro , le añade otra funcionalidad (añade logica distinta) y retorna otra funcion  


#Funcion externa ---> ESTE ES EL DECORADOR 
# def envoltorio(CUAK):
#     def nueva_funcion():
#         print("Estoy envolviendo la funcion original")
#         CUAK()
#         print("Termine de envolver")
#     return nueva_funcion

# #ESTA ES LA FUNCION ORIGINAL
# @envoltorio
# def decir_hola():
#     print("Soy la funcion original y me encargo solamente de decir HOLA")
# decir_hola()

# def con_emocion(funcion):
#     def nueva_funcion():
#         print("Estoy super Feliz")
#         funcion()
#         return print("Que tengas un lindo dia")
#     return nueva_funcion


# @con_emocion
# def saludar():
#     print("Hola como estas?")
    
# saludar()


# def fabrica_galletas():
#     for i in range(5):
#         print("Horneando 🥨 ... ")
#         yield f"Galleta {i + 1}"
        
# galletas = fabrica_galletas()

# print(next(galletas))
# print(next(galletas))
# print(next(galletas))
# print(next(galletas))
# print(next(galletas))