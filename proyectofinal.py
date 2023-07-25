#Oscar Andres Hernandez Pineda
#2264488-2724
#Tecnologia en desarrollo de software
#Universidad del valle

tarifa_moto = 0
tarifa_auto = 0
autos = []
motos = []
placas_registradas = []
lista_autos = []
lista_motos = []

def menu():
    print("\n--------Menú-------- \n 1. Tarifas \n 2. Ingresar vehiculo \n 3. Buscar vehiculo \n 4. Mostrar vehiculos \n 5. Salida de vehiculo \n 6. Cuadre de caja \n 7. Salir\n")
    inputmenu = int(input("Ingrese una opcion: "))
    while inputmenu !=7:
        if inputmenu == 1:
            tarifas()
        elif inputmenu == 2:
            ingresar_vehiculo()
        elif inputmenu == 3:
            buscarvehiculo()
        elif inputmenu == 4:
            mostrarvehiculos()
        elif inputmenu == 5:
            salida()
        elif inputmenu == 6:
            cuadre()
        else:
            print("[!] Porfavor ingrese una opcion valida [!]\n")
            menu()


def tarifas():
    print("\n------Tarifas------ \n 1. Ingresar tarifas \n 2. Mostrar tarifas \n 3. Modificar tarifas \n 4. Regresar \n")
    inputtarifas = int(input("Ingrese una opcion: "))
    if inputtarifas == 1:
        ingresartarifas()
    elif inputtarifas == 2:
        print(f"\n > El valor por minuto de automoviles es: ${tarifa_auto} \n > El valor por minuto de motocicletas es: ${tarifa_moto}\n")
    elif inputtarifas == 3:
        modificartarifas()
    elif inputtarifas == 4:
        menu() 


def modificartarifas():
        print("\n------Modificar tarifa------ \n 1. Modificar tarifa automovil \n 2. Modificar tarifa motocicleta \n 3. Regresar \n")
        inputmodificartarifas = int(input("Ingrese una opcion: "))
        if inputmodificartarifas == 1:
            global tarifa_auto
            tarifa_auto = float(input("\nIngrese tarifa automovil (por minuto): "))
        if inputmodificartarifas == 2:
            global tarifa_moto
            tarifa_moto = float(input("\nIngrese tarifa motocicleta (por minuto): "))
        if inputmodificartarifas == 3:
            tarifas()


def ingresartarifas():
        print("\n------Ingresar tarifas------ \n 1. Ingresar tarifa de automovil \n 2. Ingresar tarifa de motocicleta \n 3. Regresar \n")
        inputingresartarifas = int(input("Ingrese una opcion: "))
        if inputingresartarifas == 1:
            global tarifa_auto
            tarifa_auto = float(input("\nIngrese tarifa automovil (por minuto): "))
        elif inputingresartarifas == 2:
            global tarifa_moto
            tarifa_moto = float(input("\nIngrese tarifa motocicleta (por minuto): "))
        elif inputingresartarifas == 3:
            tarifas()
        else:
            print("[!] Porfavor ingrese una opcion valida [!]\n")


def ingresar_vehiculo():
    cliente = []

    tipo_vehiculo = str(input("Ingrese el tipo de vehículo (a: automóvil, m: moto): "))

    if tipo_vehiculo == "a":
        pass

    elif tipo_vehiculo == "m":
        pass
    
    else:
        print("\n Porfavor ingrese una opcion valida \n")
        ingresar_vehiculo()

    placa = input("Ingrese el número de la placa: ")

    if placa in placas_registradas:
        print("\n La placa ya está registrada\n")
        menu()
    else:
        placas_registradas.append(placa)
        hora_entrada = int(input("Ingrese la hora de ingreso (en formato de 24 horas: hhmm): "))
        nombre_cliente = str(input("Ingrese el nombre del cliente: "))
        print("\n > Vehículo registrado exitosamente \n")
        if tipo_vehiculo == "a":
            cliente.append(placa)
            cliente.append("auto")
            cliente.append(hora_entrada)
            cliente.append(nombre_cliente)
            autos.append(cliente)
            

        elif tipo_vehiculo == "m":
            cliente.append(placa)
            cliente.append("moto")
            cliente.append(hora_entrada)
            cliente.append(nombre_cliente)
            motos.append(cliente)
        menu()


def buscarvehiculo():
    print("\n------Buscar vehiculo------ \n 1. Buscar motos \n 2. Buscar automoviles \n 3.Regresar \n")
    inputbuscarvehiculo = int(input("Ingrese una opcion: "))
    if inputbuscarvehiculo == 1:
        buscarmoto = input("Ingrese la placa de la motocicleta: ")
        if buscarmoto in placas_registradas:
            n = len(motos)
            for i in range(n):
                if buscarmoto == motos[i][0]:
                    print(f"\n Num placa: {motos[i][0]} \n Tipo de vehiculo: Moto \n Hora de ingreso: {motos[i][2]}\n Nombre: {motos[i][3]}\n")
                else:
                    print(" \n Vehiculo no encontrado \n")
            n1 = len(lista_motos)
            for k in range(n1):
                if buscarmoto == lista_motos[k][0]:
                    print(f"Hora salida: {lista_motos[i][1]}\n Numero minutos: {lista_motos[k][2]}\n Total: {lista_motos[k][3]}")
                else:
                    pass
        else:
            print("\n Vehiculo no encontrado \n")

    elif inputbuscarvehiculo == 2:
        buscarauto = str(input("Ingrese la placa del automovil: "))
        if buscarauto in placas_registradas:
            n = len(autos)
            for j in range(n):
                if buscarauto == autos[j][0]:
                    print(f"\n Num placa: {autos[j][0]} \n Tipo de vehiculo: Auto \n Hora de ingreso: {autos[j][2]}\n Nombre: {autos[j][3]}")
                else:
                    print(" \n Vehiculo no encontrado \n")
            n1 = len(lista_autos)
            for k in range(n1):
                if buscarauto == lista_autos[k][0]:
                    print(f" Hora salida: {lista_autos[k][1]}\n Numero minutos: {lista_autos[k][2]}\n Total: {lista_autos[k][3]}")
                else:
                    pass
        else:
            print("\n Vehiculo no encontrado \n")
    elif inputbuscarvehiculo == 3:
        menu()
    else:
        print("[!] Porfavor ingrese una opcion valida [!]\n")


def mostrarvehiculos():
    print("\n------Mostrar vehiculos------ \n 1. Mostrar todos los automoviles \n 2. Mostrar todas las motocicletas \n 3. Regresar")
    inputmostrarvehiculos = int(input("Ingrese una opcion: "))
    if inputmostrarvehiculos == 1:
        print("\nPlaca     Ingreso     Salida     Minutos     TOTAL\n")
        if len(autos) > 0:
            for i in range(len(autos)):
                print(f"{autos[i][0]}    {autos[i][2]}     ",end="  ")
                if len(lista_autos) > 0:
                    for q in range(len(lista_autos)):
                        print(f"{lista_autos[q][1]}           {lista_autos[q][2]}         {lista_autos[q][3]}",end="  ")

    elif inputmostrarvehiculos == 2:
        print("Placa     Ingreso     Salida     Minutos     TOTAL\n")
        if len(motos) > 0:
            for j in range(len(motos)):
                print(f"{motos[j][0]}    {motos[j][2]}     ",end="  ")
                if len(lista_motos) > 0:
                    for w in range(len(lista_motos)):
                        print(f"{lista_motos[w][1]}           {lista_motos[w][2]}         {lista_motos[w][3]}",end="  ")

    elif inputmostrarvehiculos == 3:
        menu()
    else:
        print("[!] Porfavor ingrese una opcion valida [!]\n")

def salida():
    datos = []
    global hora_salida
    tipo_vehiculo = input("Tipo de vehiculo (a: auto, m: moto): ")
    if tipo_vehiculo == "a":
        pass
    elif tipo_vehiculo == "m":
        pass
    else:
        print("\n Porfavor ingrese una opcion valida \n")
        salida()

    placa = input("Placa: ")
    if tipo_vehiculo == "a":
        n = len(autos)
        for i in range(n):
            if placa in placas_registradas:
                hora_entrada = autos[i][2]
                datos.append(placa)

            else:
                print("\n Esta placa no esta registrada \n")
                menu()
    
    hora_salida = int(input("Hora de salida: "))
    if hora_salida < hora_entrada:
        print("Hora incorrecta, porfavor intentelo de nuevo")
    else:
        datos.append(hora_salida)
        horas = (hora_salida - hora_entrada)
        x = (horas//100)*60
        minutos = (horas%100)+x
        datos.append(minutos)
        print(f"Numero de minutos: {minutos}")

        if tipo_vehiculo == "a":
            total_pagar1 = minutos*tarifa_auto
            datos.append(total_pagar1)
            lista_autos.append(datos)
            print(f"Total a pagar: {total_pagar1}")
            menu()
            
        elif tipo_vehiculo == "m":
            total_pagar2 = minutos*tarifa_moto
            datos.append(total_pagar2)
            lista_motos.append(datos)
            print(f"Total a pagar: {total_pagar2}")
            menu()


def cuadre():
    suma_total = 0
    for o in range(len(lista_motos)):
        if len(lista_motos) > 0:
            suma_total += lista_motos[o][3]

    for p in range(len(lista_autos)):
        if len(lista_autos) > 0:
            suma_total += lista_autos[p][3]

    print(f"El total es: {suma_total}")
    menu()
        
menu()
