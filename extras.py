# puse acá las otras dos clases para que no me molestaran en el archivo poo.py, 
# hay que llevarlas de vuelta para ese lado! 

class ClienteGold:
    def __init__(self):
        self.tarjeta_debito = 1
        self.cajas_ahorro = 2
        self.cuenta_corriente = 1
        self.cajas_ahorro_dolares_extras = 0
        self.extensiones_visa = 5
        self.extensiones_mastercard = 5
        self.limite_visa_pago = 150000
        self.limite_visa_cuotas = 100000
        self.limite_mastercard_pago = 150000
        self.limite_mastercard_cuotas = 100000
        self.retiro_diario_maximo = 20000
        self.retiros_sin_comision = True
        self.acceso_cuenta_inversion = True
        self.tiene_chequera = False

    def realizar_retiro(self, monto):
        if monto > self.retiro_diario_maximo and not self.retiros_sin_comision:
            print("Error: El monto excede el límite diario de retiro y se aplicará una comisión")
            return
        elif monto > self.retiro_diario_maximo and self.retiros_sin_comision:
            print(f"Retiro exitoso de ${monto}")
        else:
            comision = monto * 0.02  # Ejemplo: Comisión del 2%
            print(f"Se aplica una comisión de ${comision} por este retiro")

    def realizar_transferencia_saliente(self, monto):
        comision = monto * 0.005  # Comisión del 0.5%
        print(f"Se aplica una comisión de ${comision} por esta transferencia saliente")

    def realizar_transferencia_entrante(self, monto):
        comision = monto * 0.001  # Comisión del 0.1%
        print(f"Se aplica una comisión de ${comision} por esta transferencia entrante")

class ClienteBlack:
    def __init__(self):
        self.tarjetas_debito = 5
        self.cajas_ahorro_pesos = 5
        self.cajas_ahorro_dolares = 5
        self.cuentas_corrientes = 3
        self.extensiones_visa = 10
        self.extensiones_mastercard = 10
        self.extensiones_amex = 10
        self.limite_visa_pago = 500000
        self.limite_visa_cuotas = 600000
        self.limite_mastercard_pago = 500000
        self.limite_mastercard_cuotas = 600000
        self.limite_amex_pago = 500000
        self.limite_amex_cuotas = 600000
        self.retiro_diario_maximo = 100000
        self.retiros_sin_comision = True
        self.acceso_cuenta_inversion = True
        self.tiene_chequera = True
        self.chequeras = 2

    def realizar_retiro(self, monto):
        if monto > self.retiro_diario_maximo and not self.retiros_sin_comision:
            print("Error: El monto excede el límite diario de retiro y se aplicará una comisión")
            return
        elif monto > self.retiro_diario_maximo and self.retiros_sin_comision:
            print(f"Retiro exitoso de ${monto}")
        else:
            comision = monto * 0.02  # Ejemplo: Comisión del 2%
            print(f"Se aplica una comisión de ${comision} por este retiro")

    def realizar_transferencia_saliente(self, monto):
        print(f"Transferencia saliente exitosa de ${monto}")

    def realizar_transferencia_entrante(self, monto):
        print(f"Transferencia entrante exitosa de ${monto}")

def interactuar_con_cliente_gold():
    cliente = ClienteGold()
    while True:
        print("\nEscribe la opción que deseas utilizar (o '0' para salir):")
        print("1 - Tarjetas de débito")
        print("2 - Cajas de ahorro")
        print("3 - Cuentas corrientes")
        print("4 - Realizar retiro")
        print("5 - Realizar transferencia saliente")
        print("6 - Realizar transferencia entrante")
        print("7 - Chequeras")

        opcion = int(input(">> "))

        if opcion == 0:
            break
        elif opcion == 1:
            print(f"Tienes una tarjeta de débito.")
        elif opcion == 2:
            print(f"Tienes {cliente.cajas_ahorro} cajas de ahorro en pesos y {cliente.cajas_ahorro_dolares_extras} en dólares.")
        elif opcion == 3:
            print(f"Tienes {cliente.cuenta_corriente} cuenta corriente.")
        elif opcion == 4:
            monto = float(input("Ingrese el monto a retirar: $"))
            while monto <= 0:
                monto = float(input("El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"))  
            cliente.realizar_retiro(monto)
        elif opcion == 5:
            monto = float(input("Ingrese el monto a transferir: $"))
            while monto <= 0:
                monto = float(input("El monto a transferir no puede ser 0 o negativo. Ingreselo de nuevo: $"))  
            cliente.realizar_transferencia_saliente(monto)
        elif opcion == 6:
            monto = float(input("Ingrese el monto a recibir: $"))
            while monto <=0: 
                monto = float(input("El monto a solicitar no puede ser menor a 0. Ingreselo de nuevo: $"))  
            cliente.realizar_transferencia_entrante(monto)
        elif opcion == 7:
            if(cliente.tiene_chequera):
                print(f"Tienes una chequeras.")
            else:
                print(f"No tienes chequeras.")
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

def interactuar_con_cliente_black():
    cliente = ClienteBlack()
    while True:
        print("\nEscribe la opción que deseas utilizar (o '0' para salir):")
        print("1 - Tarjetas de débito")
        print("2 - Cajas de ahorro")
        print("3 - Cuentas corrientes")
        print("4 - Realizar retiro")
        print("5 - Realizar transferencia saliente")
        print("6 - Realizar transferencia entrante")
        print("7 - Chequeras")

        opcion = int(input(">> "))

        if opcion == 0:
            break
        elif opcion == 1:
            print(f"Tienes {cliente.tarjetas_debito} tarjetas de débito.")
        elif opcion == 2:
            print(f"Tienes {cliente.cajas_ahorro_pesos} cajas de ahorro en pesos y {cliente.cajas_ahorro_dolares} en dólares.")
        elif opcion == 3:
            print(f"Tienes {cliente.cuentas_corrientes} cuentas corrientes.")
        elif opcion == 4:
            monto = float(input("Ingrese el monto a retirar: $"))
            while monto <= 0:
                monto = float(input("El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"))  
            cliente.realizar_retiro(monto)
        elif opcion == 5:
            monto = float(input("Ingrese el monto a transferir: $"))
            while monto <= 0:
                monto = float(input("El monto a transferir no puede ser 0 o negativo. Ingreselo de nuevo: $"))  
            cliente.realizar_transferencia_saliente(monto)
        elif opcion == 6:
            monto = float(input("Ingrese el monto a recibir: $"))
            while monto <=0: 
               monto = float(input("El monto a solicitar por transferencia no puede ser menor a 0. Ingreselo de nuevo: $"))  
            cliente.realizar_transferencia_entrante(monto)
        elif opcion == 7:
            if(cliente.tiene_chequera):
                print(f"Tienes {cliente.chequeras} chequeras.")
            else:
                print(f"No tienes chequeras.")
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
