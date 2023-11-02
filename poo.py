import datetime


class ClienteClassic:
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero
        self.dni = dni
        self.transacciones = []
        self.monto_ars = 250000
        self.monto_usd = 100
        self.tarjeta_debito = 0
        self.caja_ahorro_pesos = 0
        self.caja_ahorro_dolares = 0
        self.retiro_diario_maximo = 10000
        self.retiros_sin_comision = 5
        self.numero_transaccion = 0 

    def salida_resumen(self):
        salida = {"numero": self.numero_cuenta, 
                  "nombre": self.nombre,
                  "apellido": self.apellido, 
                  "dni": self.dni, 
                  "tipo": "CLASSIC",
                  "transacciones": self.transacciones
                  }
        print (salida)
        return salida

    def realizar_retiro(self):
        transaccion = {}
        monto_retiro = float(input("Ingrese el monto a retirar: $"))
        while monto_retiro <= 0:
            monto_retiro = float(
                input(
                    "El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"
                )
            )

        if monto_retiro > self.retiro_diario_maximo:
            print("Error: El monto excede el límite diario de retiro")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        elif monto_retiro > self.monto_ars:
            print("Error: El monto a retirar excede sus fondos.")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        else:
            if self.retiros_sin_comision > 0:
                self.retiros_sin_comision -= 1
                self.monto_ars -= monto_retiro
                print(f"Retiro exitoso de ${monto_retiro}")
                print(f"Saldo actual: ${self.monto_ars}")
                self.numero_transaccion +=1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_retiro,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion
                }
            else:
                comision = monto_retiro * 0.02  # Comisión del 2%
                print(
                    f"Ha excedido los 5 retiros sin comisión. Se aplica una comisión de ${comision} por este retiro"
                )
                self.monto_ars -= monto_retiro
                self.monto_ars -= comision
                print(f"Saldo actual: ${self.monto_ars}")
                self.numero_transaccion + 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_retiro,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        self.transacciones.append(transaccion)

    def realizar_transferencia_saliente(self):
        transaccion = {}
        moneda = int(input(
            "Seleccione la moneda en la que quiere realizar la transferencia 1-USD / 2-ARS: "))
        while moneda not in [1, 2]:
            moneda = int(
                input("Moneda incorrecta. Elija una de estas dos opciones: 1-USD / 2-ARS: "))

        if moneda == 2:
            monto_saliente = float(
                input("Ingrese el monto que desea transferir en ARS: $"))
            while monto_saliente <= 0:
                monto_saliente = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_saliente * 0.01  # Comisión del 1%

            if monto_saliente > self.monto_ars:
                print("El monto que desea transferir excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_ars -= monto_saliente
                self.monto_ars -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion + 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        elif moneda == 1:
            monto_saliente = float(
                input("Ingrese el monto que desea transferir en USD: $"))
            while monto_saliente <= 0:
                monto_saliente = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_saliente * 0.01  # Comisión del 1%

            if monto_saliente > self.monto_usd:
                print("El monto que desea transferir excede sus fondos.")
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_usd -= monto_saliente
                self.monto_usd -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        self.transacciones.append(transaccion)

    def realizar_transferencia_entrante(self):
        transaccion = {}
        moneda = int(input(
            "Seleccione la moneda en la que quiere realizar la transferencia 1-USD / 2-ARS: "))

        while moneda not in [1, 2]:
            moneda = int(
                input("Moneda incorrecta. Elija una de estas dos opciones: 1- USD / 2 - ARS: "))

        if moneda == 2:
            monto_entrante = float(
                input("Ingrese el monto que desea transferir en ARS: $"))
            while monto_entrante <= 0:
                monto_entrante = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_entrante * 0.005  # Comisión del 0.5%
            self.monto_ars += monto_entrante
            self.monto_ars -= comision
            print(f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia entrante")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        elif moneda == 1:
            monto_entrante = float(
                input("Ingrese el monto que desea recibir en USD: $"))
            while monto_entrante <= 0:
                monto_entrante = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_entrante * 0.005  # Comisión del 0.5%
            print(
                f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia entrante")
            self.monto_usd += monto_entrante
            self.monto_usd -= comision
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_RECIBIDA_<USD>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }

        self.transacciones.append(transaccion)

    def alta_tarjeta_debito(self):
        transaccion = {}
        if self.tarjeta_debito == 0:
            print("Felicitaciones! Ya cuentas con una tarjeta de débito")
            self.tarjeta_debito = 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": 1000,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        elif self.tarjeta_debito == 1:
            print(
                "No puedes dar de alta mas tarjetas de débito. El límite de tu cuenta es de 1 tarjeta. Actualiza tu plan para extender este límite."
            )
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": 1000,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        self.transacciones.append(transaccion)

    def compra_cuotas_credito(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "COMPRA_EN_CUOTAS_TARJETA_CREDITO_<none>",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Tu plan actual no incluye tarjetas de crédito. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def compra_credito(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "COMPRA_TARJETA_CREDITO_<none>",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Tu plan actual no incluye tarjetas de crédito. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def alta_tarjeta_credito(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "ALTA_TARJETA_CREDITO_<none>",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Tu plan actual no incluye tarjetas de crédito. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def alta_chequera(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "ALTA_CHEQUERA",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Tu plan actual no incluye chequeras. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def alta_cuenta_corriente(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "ALTA_CUENTA_CTE_<none>",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Tu plan actual no incluye cuentas corrientes. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def alta_caja_ahorro(self, moneda):
        transaccion = {}
        if moneda == 2:
            if self.caja_ahorro_pesos == 0:
                print("Felicitaciones! Ya cuentas con una caja de ahorro en pesos")
                self.caja_ahorro_pesos = 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            elif self.caja_ahorro_pesos == 1:
                print(
                    "No puedes dar de alta mas cajas de ahorro en pesos. El límite de tu cuenta es de 1 caja de ahorro. Actualiza tu plan para extender este límite."
                )
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        elif moneda == 1:
            if self.caja_ahorro_dolares == 0:
                print(
                    "Felicitaciones! Ya cuentas con una caja de ahorro en dolares. Se aplicará un cargo mensual de 10USD para mantenerla."
                )
                self.caja_ahorro_dolares = 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            elif self.caja_ahorro_dolares == 1:
                print(
                    "No puedes dar de alta mas cajas de ahorro en dolares. El límite de tu cuenta es de 1 caja de ahorro. Actualiza tu plan para extender este límite."
                )
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        self.transacciones.append(transaccion)

    def alta_cuenta_de_inversion(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "ALTA_CUENTA_DE_INVERSION",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Tu plan actual no incluye cuentas de inversión. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def compra_dolar(self):
        # cotizacion de dolar ficticia :(
        dolar = 1000
        monto_dolar = float(
            input("Ingrese el monto de dólares que desea comprar: $"))
        if monto_dolar * dolar <= self.monto_ars:
            while monto_dolar <= 0:
                monto_dolar = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $")
                )
            self.monto_ars -= monto_dolar * dolar
            self.monto_usd += monto_dolar
            print("Compra exitosa.")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        else:
            print("El monto de dolares que desea comprar excede sus fondos en ARS.")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        self.transacciones.append(transaccion)

    def venta_dolar(self):
        transaccion = {}
        monto_dolar = float(
            input("Ingrese el monto de dólares que desea vender: $")
        )
        while monto_dolar <= 0:
            monto_dolar = float(
                input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $")
            )
        if monto_dolar > self.monto_usd:
            print("El monto que desea vender excede sus fondos.")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        else:
            dolar = 1000
            self.monto_usd -= monto_dolar
            self.monto_ars += monto_dolar * dolar
            print("Venta exitosa.")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        self.transacciones.append(transaccion)



class ClienteGold:
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero
        self.dni = dni
        self.transacciones = []
        self.monto_ars = 250000
        self.monto_usd = 100
        self.tarjeta_debito = 0
        self.caja_ahorro_pesos = 0
        self.caja_ahorro_dolares = 0
        self.retiro_diario_maximo = 20000
        self.retiros_sin_comision = 10000000 #numero "infinito"
        self.numero_transaccion = 0 
        self.tarjeta_credito = []
        self.chequera_agregada = False
        self.cuenta_corriente_agregada = False

    def salida_resumen(self):
        salida = {"numero": self.numero_cuenta, 
                  "nombre": self.nombre,
                  "apellido": self.apellido, 
                  "dni": self.dni, 
                  "tipo": "CLASSIC",
                  "transacciones": self.transacciones
                  }
        print (salida)
        return salida

    def realizar_retiro(self):
        transaccion = {}
        monto_retiro = float(input("Ingrese el monto a retirar: $"))
        while monto_retiro <= 0:
            monto_retiro = float(
                input(
                    "El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"
                )
            )

        if monto_retiro > self.monto_ars:
            print("Error: El monto a retirar excede sus fondos.")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        else:
            if self.retiros_sin_comision > 0:
                self.retiros_sin_comision -= 1
                self.monto_ars -= monto_retiro
                print(f"Retiro exitoso de ${monto_retiro}")
                print(f"Saldo actual: ${self.monto_ars}")
                self.numero_transaccion +=1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_retiro,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion
                }
                self.monto_ars -= monto_retiro
                self.monto_ars -= comision
                print(f"Saldo actual: ${self.monto_ars}")
                self.numero_transaccion + 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_retiro,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        self.transacciones.append(transaccion)

    def realizar_transferencia_saliente(self):
        transaccion = {}
        moneda = int(input(
            "Seleccione la moneda en la que quiere realizar la transferencia 1-USD / 2-ARS: "))
        while moneda not in [1, 2]:
            moneda = int(
                input("Moneda incorrecta. Elija una de estas dos opciones: 1-USD / 2-ARS: "))

        if moneda == 2:
            monto_saliente = float(
                input("Ingrese el monto que desea transferir en ARS: $"))
            while monto_saliente <= 0:
                monto_saliente = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_saliente * 0.005  # Comisión del 0.5%

            if monto_saliente > self.monto_ars:
                print("El monto que desea transferir excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_ars -= monto_saliente
                self.monto_ars -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion + 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        elif moneda == 1:
            monto_saliente = float(
                input("Ingrese el monto que desea transferir en USD: $"))
            while monto_saliente <= 0:
                monto_saliente = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_saliente * 0.01  # Comisión del 1%

            if monto_saliente > self.monto_usd:
                print("El monto que desea transferir excede sus fondos.")
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_usd -= monto_saliente
                self.monto_usd -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        self.transacciones.append(transaccion)

    def realizar_transferencia_entrante(self):
        transaccion = {}
        moneda = int(input(
            "Seleccione la moneda en la que quiere realizar la transferencia 1-USD / 2-ARS: "))

        while moneda not in [1, 2]:
            moneda = int(
                input("Moneda incorrecta. Elija una de estas dos opciones: 1- USD / 2 - ARS: "))

        if moneda == 2:
            monto_entrante = float(
                input("Ingrese el monto que desea transferir en ARS: $"))
            while monto_entrante <= 0:
                monto_entrante = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_entrante * 0.001  # Comisión del 0.1%
            self.monto_ars += monto_entrante
            self.monto_ars -= comision
            print(f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia entrante")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        elif moneda == 1:
            monto_entrante = float(
                input("Ingrese el monto que desea recibir en USD: $"))
            while monto_entrante <= 0:
                monto_entrante = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            comision = monto_entrante * 0.005  # Comisión del 0.5%
            print(
                f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia entrante")
            self.monto_usd += monto_entrante
            self.monto_usd -= comision
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_RECIBIDA_<USD>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }

        self.transacciones.append(transaccion)

    def alta_tarjeta_debito(self):
        transaccion = {}
        if self.tarjeta_debito == 0:
            print("Felicitaciones! Ya cuentas con una tarjeta de débito")
            self.tarjeta_debito = 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": 1000,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        elif self.tarjeta_debito == 1:
            print(
                "No puedes dar de alta mas tarjetas de débito. El límite de tu cuenta es de 1 tarjeta. Actualiza tu plan para extender este límite."
            )
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": 1000,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        self.transacciones.append(transaccion)

    def compra_cuotas_credito(self,tipo_tarjeta,cuotas,monto):
        if tipo_tarjeta not in ["Visa", "Mastercard"]:
            print("Solo se aceptan tarjetas Visa y Mastercard.")
            return
        if monto > 100000 and cuotas > 1:
                print("El monto excede el límite de 100,000 para pagos en cuotas.")
                return
        transaccion = {
            "estado": "APROBADA",
            "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_{tipo_tarjeta}",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": monto,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            f"¡Transacción exitosa! Se ha realizado una compra de {monto} en {cuotas} cuotas con una tarjeta {tipo_tarjeta}."
        )
        self.transacciones.append(transaccion)

    def compra_credito(self,tipo_tarjeta,cuotas,monto):
        if tipo_tarjeta not in ["Visa", "Mastercard"]:
            print("Solo se aceptan tarjetas Visa y Mastercard.")
            return

        if monto > 150000 and cuotas == 1:
            print("El monto excede el límite de 150,000 para un pago.")
            return
        transaccion = {
            "estado": "APROBADA",
            "tipo": f"COMPRA_TARJETA_CREDITO_{tipo_tarjeta}",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": monto,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            f"¡Transacción exitosa! Se ha realizado una compra de {monto} en {cuotas} cuotas con una tarjeta {tipo_tarjeta}."
        )
        self.transacciones.append(transaccion)

    def alta_tarjeta_credito(self,tipo_tarjeta,monto):
        if len(self.tarjetas_credito) >= 5:
            print("Ya tienes el máximo de 5 tarjetas de crédito.")
            return
        if tipo_tarjeta not in ["Visa", "Mastercard"]:
            print("Solo se aceptan tarjetas Visa y Mastercard.")
            return
        transaccion = {
            "estado": "APROBADA",
            "tipo": f"ALTA_TARJETA_CREDITO_{tipo_tarjeta}",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": monto,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
    
        self.transacciones.append(transaccion)

        self.tarjetas_credito.append({"tipo": tipo_tarjeta, "monto": monto})

        print(f"Felicidades! Se ha agregado una tarjeta de crédito {tipo_tarjeta} con un límite de {monto}.")
    
    def alta_chequera(self):
        if self.chequera_agregada:
            print("Ya tienes una chequera agregada.")
            return
        transaccion = {
            "estado": "APROBADA",
            "tipo": "ALTA_CHEQUERA",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }

        self.transacciones.append(transaccion)

        self.chequera_agregada = True

        print("Felicidades! Se ha agregado una chequera.")

    def alta_cuenta_corriente(self):
        if self.cuenta_corriente_agregada:
            print("Ya tienes una cuenta corriente agregada.")
            return

        transaccion = {
            "estado": "APROBADA",
            "tipo": "ALTA_CUENTA_CTE_SIN_CARGO",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }

        self.transacciones.append(transaccion)

        self.cuenta_corriente_agregada = True

        print("Felicidades! Se ha agregado una cuenta corriente sin cargo adicional.")

    def alta_caja_ahorro(self, moneda):
        transaccion = {}
        if moneda == 2:
            if self.caja_ahorro_pesos == 0:
                print("Felicitaciones! Ya cuentas con una caja de ahorro en pesos")
                self.caja_ahorro_pesos = 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
            elif self.caja_ahorro_pesos == 2:
                print(
                    "No puedes dar de alta mas cajas de ahorro en pesos. El límite de tu cuenta es de 2 cajas de ahorro. Actualiza tu plan para extender este límite."
                )
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        elif moneda == 1:
            if self.caja_ahorro_dolares == 0:
                print(
                    "Felicitaciones! Ya cuentas con una caja de ahorro en dolares. Se aplicará un cargo mensual de 10USD para mantenerla."
                )
                self.caja_ahorro_dolares = 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": datetime.datetime.now(),
                    "numero": self.numero_transaccion 
                }
        self.transacciones.append(transaccion)

    def alta_cuenta_de_inversion(self):
        transaccion = {
            "estado": "APROBADO",
            "tipo": "ALTA_CUENTA_DE_INVERSION",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": datetime.datetime.now(),
            "numero": self.numero_transaccion 
        }
        print(
            "Felicidades! Ya cuentas con una caja de inversión."
        )
        self.transacciones.append(transaccion)

    def compra_dolar(self):
        # cotizacion de dolar ficticia :(
        dolar = 1000
        monto_dolar = float(
            input("Ingrese el monto de dólares que desea comprar: $"))
        if monto_dolar * dolar <= self.monto_ars:
            while monto_dolar <= 0:
                monto_dolar = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $")
                )
            self.monto_ars -= monto_dolar * dolar
            self.monto_usd += monto_dolar
            print("Compra exitosa.")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        else:
            print("El monto de dolares que desea comprar excede sus fondos en ARS.")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        self.transacciones.append(transaccion)

    def venta_dolar(self):
        transaccion = {}
        monto_dolar = float(
            input("Ingrese el monto de dólares que desea vender: $")
        )
        while monto_dolar <= 0:
            monto_dolar = float(
                input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $")
            )
        if monto_dolar > self.monto_usd:
            print("El monto que desea vender excede sus fondos.")
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        else:
            dolar = 1000
            self.monto_usd -= monto_dolar
            self.monto_ars += monto_dolar * dolar
            print("Venta exitosa.")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": datetime.datetime.now(),
                "numero": self.numero_transaccion 
            }
        self.transacciones.append(transaccion)

def interactuar_con_cliente_classic():
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    numero = int(input("Numero: "))
    dni = str(input("Dni: "))
    cliente = ClienteClassic(nombre, apellido, numero, dni)
    while True:
        print("\nEscribe la opción que deseas utilizar (o '0' para salir):")
        print("1 - Retirar efectivo desde un cajero")
        print("2 - Retirar efectivo desde caja")
        print("3 - Compra en cuotas con tarjeta de crédito")
        print("4 - Compra con tarjeta de crédito")
        print("5 - Alta tarjeta de crédito")
        print("6 - Alta tarjeta de debito")
        print("7 - Alta chequera")
        print("8 - Alta cuenta corriente")
        print("9 - Alta caja de ahorro en pesos")
        print("10 - Alta caja de ahorro en dolares")
        print("11 - Alta cuenta de inversion")
        print("12 - Compra dólar")
        print("13 - Venta dólar")
        print("14 - Transferencia saliente")
        print("15 - Transferencia entrante")

        opcion = int(input(">> "))

        if opcion == 0:
            break
        elif opcion == 1:
            cliente.realizar_retiro()
        elif opcion == 2:
            cliente.realizar_retiro()
        elif opcion == 3:
            cliente.compra_cuotas_credito()
        elif opcion == 4:
            cliente.compra_credito()
        elif opcion == 5:
            cliente.alta_tarjeta_credito()
        elif opcion == 6:
            cliente.alta_tarjeta_debito()
        elif opcion == 7:
            cliente.alta_chequera()
        elif opcion == 8:
            cliente.alta_cuenta_corriente()
        elif opcion == 9:
            cliente.alta_caja_ahorro(2)
        elif opcion == 10:
            cliente.alta_caja_ahorro(1)
        elif opcion == 11:
            cliente.alta_cuenta_de_inversion()
        elif opcion == 12:
            cliente.compra_dolar()
        elif opcion == 13:
            cliente.venta_dolar()
        elif opcion == 14:
            cliente.realizar_transferencia_saliente()
        elif opcion == 15:
            cliente.realizar_transferencia_entrante()
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
    cliente.salida_resumen()


# ***************************************************************************************************** #
if __name__ == "__main__":
    print("Bienvenido, por favor, seleccione una de las siguientes opciones:")
    op = int(input("1 - Cliente Classic \n2 - Cliente Gold\n3 - Cliente Black\n>> "))
    while op in [1, 2, 3]:
        if op == 1:
            interactuar_con_cliente_classic()
            op = 0
        # elif op == 2:
        #     interactuar_con_cliente_gold()
        #     op = 0
        # elif op == 3:
        #     interactuar_con_cliente_black()
        #     op = 0
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            op = input(
                "1 - Cliente Classic \n2 - Cliente Gold\n3 - Cliente Black\n>>")
