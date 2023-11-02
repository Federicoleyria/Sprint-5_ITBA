import datetime as date
import json

class ClienteClassic:
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero
        self.dni = dni
        self.transacciones = []
        self.monto_ars = 250
        self.monto_usd = 100
        self.tarjeta_debito = 0
        self.caja_ahorro_pesos = 0
        self.caja_ahorro_dolares = 0
        self.retiro_diario_maximo = 10000
        self.retiros_sin_comision = 5
        self.numero_transaccion = 0
        
        fecha = date.datetime.now()
        self.dia = fecha.day
        self.mes = fecha.month
        self.anio = fecha.year
        self.hora = fecha.hour
        self.minuto = fecha.minute
        self.segundo = fecha.second
        self.now = f"{self.dia}/{self.mes}/{self.anio} {self.hora}:{self.minuto}:{self.segundo}"

    def salida_resumen(self):
        salida = {
                  "numero": self.numero_cuenta,
                  "nombre": self.nombre,
                  "apellido": self.apellido,
                  "dni": self.dni,
                  "tipo": "CLASSIC",
                  "transacciones": self.transacciones
                  }
        with open('resumen.html', 'w') as archivo:
            json.dump(salida, archivo)  

    def realizar_retiro(self, opcion):
        transaccion = {}
        monto_retiro = float(input("Ingrese el monto a retirar: $"))
        while monto_retiro <= 0:
            monto_retiro = float(
                input(
                    "El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"
                )
            )

        if opcion == 1:
            #retiro por cajero
            if monto_retiro > self.monto_ars:
                print("Error: El monto a retirar excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif monto_retiro <= self.monto_ars:
                if monto_retiro > self.retiro_diario_maximo:                    
                    print(f"Error: El monto a retirar excede el límite diario de retiro de ${self.retiro_diario_maximo}.")
                    self.numero_transaccion += 1
                    transaccion = {
                        "estado": "RECHAZADA",
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                        "cuentaNumero": self.numero_cuenta,
                        "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                        "monto": None,
                        "fecha": self.now,
                        "numero": self.numero_transaccion
                    }
                else:
                    if self.retiros_sin_comision in [1,2,3,4,5]:
                        self.retiros_sin_comision -= 1
                        self.monto_ars -= monto_retiro
                        print(f"Retiro exitoso de ${monto_retiro}")
                        print(f"Saldo actual: ${self.monto_ars}")
                        self.numero_transaccion += 1
                        transaccion = {
                            "estado": "ACEPTADA",
                            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                            "cuentaNumero": self.numero_cuenta,
                            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                            "monto": monto_retiro,
                            "fecha": self.now,
                            "numero": self.numero_transaccion
                        }
                    elif self.retiros_sin_comision not in [1,2,3,4,5]:
                        comision = monto_retiro * 0.02
                        self.retiros_sin_comision -= 1
                        self.monto_ars -= monto_retiro
                        self.monto_ars -= comision
                        print(f"Ha excedido sus 5 retiros sin cargo. A partir de ahora se aplicará una comisión de ${comision} a las futuras operaciones")
                        print(f"Retiro exitoso de ${monto_retiro}")
                        print(f"Saldo actual: ${self.monto_ars}")
                        self.numero_transaccion += 1
                        transaccion = {
                            "estado": "ACEPTADA",
                            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                            "cuentaNumero": self.numero_cuenta,
                            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                            "monto": monto_retiro,
                            "fecha": self.now,
                            "numero": self.numero_transaccion
                        }
        elif opcion == 2:
            # retiro por caja
            if monto_retiro > self.monto_ars:
                print("Error: El monto a retirar excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_POR_CAJA",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                if self.retiros_sin_comision > 0:
                    self.retiros_sin_comision -= 1
                    self.monto_ars -= monto_retiro
                    print(f"Retiro exitoso de ${monto_retiro}")
                    print(f"Saldo actual: ${self.monto_ars}")
                    self.numero_transaccion += 1
                    transaccion = {
                        "estado": "ACEPTADA",
                        "tipo": "RETIRO_EFECTIVO_POR_CAJA",
                        "cuentaNumero": self.numero_cuenta,
                        "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                        "monto": monto_retiro,
                        "fecha": self.now,
                        "numero": self.numero_transaccion
                    }
        else:
            pass
        self.transacciones.append(transaccion)

        transaccion = {}
        moneda = int(input(
            "Seleccione la moneda en la que quiere realizar la transferencia 1-USD / 2-ARS: "))
        while moneda not in [1, 2]:
            moneda = int(
                input("Moneda incorrecta. Elija una de estas dos opciones: 1-USD / 2-ARS: "))

        if moneda == 2:
            monto_saliente = float(
    def compra_cuotas_credito(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "COMPRA_EN_CUOTAS_TARJETA_CREDITO_<none>",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": self.now,
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
            "fecha": self.now,
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
            "fecha": self.now,
            "numero": self.numero_transaccion
        }
        print(
            "Tu plan actual no incluye tarjetas de crédito. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
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
                "fecha": self.now,
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
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        self.transacciones.append(transaccion)

    def alta_chequera(self):
        transaccion = {
            "estado": "RECHAZADA",
            "tipo": "ALTA_CHEQUERA",
            "cuentaNumero": self.numero_cuenta,
            "permitidoActualParaTransaccion": self.retiro_diario_maximo,
            "monto": 1000,
            "fecha": self.now,
            "numero": self.numero_transaccion
        }
        print(
            "Tu plan actual no incluye chequeras. Actualizalo para poder disfrutar de este beneficio y muchos más."
        )
        self.transacciones.append(transaccion)

    def alta_cuenta_corriente(self, moneda):
        transaccion = {}
        if moneda == 1:
            # cuenta corriente usd
            print(
                "Tu plan actual no incluye cuentas corrientes en dolares. Actualizalo para poder disfrutar de este beneficio y muchos más."
            )
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_CUENTA_CTE_<USD>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        elif moneda == 2:
            # cuenta corriente ars
            print(
                "Tu plan actual no incluye cuentas corrientes en pesos. Actualizalo para poder disfrutar de este beneficio y muchos más."
            )
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_CUENTA_CTE_<ARS>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }

        self.transacciones.append(transaccion)

    def alta_caja_ahorro(self, moneda):
        transaccion = {}
        if moneda == 1:
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
                    "fecha": self.now,
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
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }     
        elif moneda == 2:
            if self.caja_ahorro_pesos == 0:
                print("Felicitaciones! Ya cuentas con una caja de ahorro en pesos")
                self.caja_ahorro_pesos = 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": 1000,
                    "fecha": self.now,
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
                    "fecha": self.now,
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
            "fecha": self.now,
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
                "fecha": self.now,
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
                "fecha": self.now,
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
                "fecha": self.now,
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
                "fecha": self.now,
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
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_ars -= monto_saliente
                self.monto_ars -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": self.now,
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
                    "fecha": self.now,
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
                    "fecha": self.now,
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
            print(
                f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia entrante")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": self.now,
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
                "fecha": self.now,
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
        self.monto_ars = 2500000
        self.monto_usd = 1000
        self.tarjeta_debito = 0
        self.caja_ahorro_pesos = 0
        self.caja_ahorro_dolares = 0
        self.retiro_diario_maximo = 20000
        self.retiros_sin_comision = 10000000  # numero "infinito"
        self.numero_transaccion = 0
        self.tarjetas_credito = []
        self.chequera = 0
        self.cuenta_corriente_ars = 0
        self.cuenta_corriente_usd = 0
        self.cuenta_de_inversion = False

        fecha = date.datetime.now()
        self.dia = fecha.day
        self.mes = fecha.month
        self.anio = fecha.year
        self.hora = fecha.hour
        self.minuto = fecha.minute
        self.segundo = fecha.second
        self.now = f"{self.dia}/{self.mes}/{self.anio} {self.hora}:{self.minuto}:{self.segundo}"
        
    def salida_resumen(self):
        salida = {"numero": self.numero_cuenta,
                  "nombre": self.nombre,
                  "apellido": self.apellido,
                  "dni": self.dni,
                  "tipo": "GOLD",
                  "transacciones": self.transacciones
                  }
        with open('resumen.html', 'w') as archivo:
            json.dump(salida, archivo)  

    def realizar_retiro(self, opcion):
        transaccion = {}
        monto_retiro = float(input("Ingrese el monto a retirar: $"))
        while monto_retiro <= 0:
            monto_retiro = float(
                input(
                    "El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"
                )
            )
        if opcion == 1:
            # retiro por cajero
            if monto_retiro > self.monto_ars:
                print("Error: El monto a retirar excede sus fondos.")
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif monto_retiro > self.retiro_diario_maximo:
                comision = monto_retiro * 0.02  # Comisión del 2%
                if self.retiros_sin_comision > 0:
                    self.retiros_sin_comision -= 1
                    self.monto_ars -= monto_retiro
                    self.monto_ars -= comision
                    print(
                        f"El monto a retirar excede el límite diario de retiro de ${self.retiro_diario_maximo}. Se aplicará una comisión de ${comision} a la operación")
                    print(f"Retiro exitoso de ${monto_retiro}")
                    print(f"Saldo actual: ${self.monto_ars}")
                    self.numero_transaccion += 1
                    transaccion = {
                        "estado": "ACEPTADA",
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                        "cuentaNumero": self.numero_cuenta,
                        "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                        "monto": monto_retiro,
                        "fecha": self.now,
                        "numero": self.numero_transaccion
                    }
        elif opcion == 2:
            # retiro por caja
            if monto_retiro > self.monto_ars:
                print("Error: El monto a retirar excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_POR_CAJA",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                if self.retiros_sin_comision > 0:
                    self.retiros_sin_comision -= 1
                    self.monto_ars -= monto_retiro
                    print(f"Retiro exitoso de ${monto_retiro}")
                    print(f"Saldo actual: ${self.monto_ars}")
                    self.numero_transaccion += 1
                    transaccion = {
                        "estado": "ACEPTADA",
                        "tipo": "RETIRO_EFECTIVO_POR_CAJA",
                        "cuentaNumero": self.numero_cuenta,
                        "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                        "monto": monto_retiro,
                        "fecha": self.now,
                        "numero": self.numero_transaccion
                    }
        else:
            pass
        self.transacciones.append(transaccion)

    def compra_cuotas_credito(self):
        transaccion = {}
        if len(self.tarjetas_credito) == 0:
            print(
                "No posees ninguna tarjeta de credito. Selecciona la opción '5' para dar de alta una.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_EN_CUOTAS_TARJETA_CREDITO_<None>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            for tarjeta in self.tarjetas_credito:
                print(tarjeta)
            numero_tarjeta = int(
                input("Selecciona una de tus tarjetas para pagar: "))
            monto = float(input("Monto a pagar: $"))
            cuotas = int(input("Cantidad de cuotas: "))
            if monto > 100000:
                print("El monto excede el límite de $100000 para pagos en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"¡Transacción exitosa! Se ha realizado una compra de ${monto} en {cuotas} cuotas con una tarjeta {self.tarjetas_credito[(numero_tarjeta-1)]}."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta-1]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        self.transacciones.append(transaccion)

    def compra_credito(self):
        transaccion = {}
        if len(self.tarjetas_credito) == 0:
            print(
                "No posees ninguna tarjeta de credito. Selecciona la opción '5' para dar de alta una.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_TARJETA_CREDITO_<None>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            for tarjeta in self.tarjetas_credito:
                print(tarjeta)
            numero_tarjeta = int(
                input("Selecciona una de tus tarjetas para pagar: "))
            monto = float(input("Monto a pagar: $"))
            if monto > 150000:
                print("El monto excede el límite de $150000 para pagos en una sola vez.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": f"COMPRA_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"¡Transacción exitosa! Se ha realizado una compra de ${monto} con una tarjeta {self.tarjetas_credito[numero_tarjeta -1]}."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta-1]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        self.transacciones.append(transaccion)

    def alta_tarjeta_credito(self):
        transaccion = {}
        if len(self.tarjetas_credito) >= 2:
            print("Ya tienes el máximo de 5 tarjetas de crédito.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_TARJETA_CREDITO_<None>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
            pass
        else:
            tipo_tarjeta = int(input(
                "Selecciona la tarjeta que quieras dar de alta: 1-Mastercard, 2-VISA\n>> "))
            while tipo_tarjeta not in [1, 2]:
                tipo_tarjeta = input(
                    "Opción inválida, por favor selecciona una de estas 3 tarjetas: 1-Mastercard, 2-VISA, 3-American Express\n>> ")
            if tipo_tarjeta == 1:
                # tarjeta MASTER
                self.tarjetas_credito.append(
                    {"tarjeta": "MASTER", "limite_un_pago": 150000, "limite_cuotas": 100000})
                print(
                    f"Felicidades! Se ha agregado una tarjeta de crédito MASTER con límites de $150000 en un pago y $100000 en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "APROBADA",
                    "tipo": f"ALTA_TARJETA_CREDITO_<MASTER>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif tipo_tarjeta == 2:
                # tarjeta VISA
                self.tarjetas_credito.append(
                    {"tarjeta": "VISA", "limite_un_pago": 150000, "limite_cuotas": 100000})
                print(
                    f"Felicidades! Se ha agregado una tarjeta de crédito VISA con límites de $150000 en un pago y $100000 en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "APROBADA",
                    "tipo": f"ALTA_TARJETA_CREDITO_<VISA>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }

        self.transacciones.append(transaccion)

    def alta_tarjeta_debito(self):
        transaccion = {}
        if self.tarjeta_debito == 0:
            print("Felicitaciones! Ya cuentas con una tarjeta de débito")
            self.tarjeta_debito = 1
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": 1000,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        elif self.tarjeta_debito == 1:
            print(
                "No puedes dar de alta mas tarjetas de débito. El límite de tu cuenta es de 1 tarjeta. Actualiza tu plan para extender este límite."
            )
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": 1000,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        self.transacciones.append(transaccion)

    def alta_chequera(self):
        transaccion = {}
        if self.chequera == 0:
            print("Felicitaciones! Se ha dado de alta una chequera.")
            self.chequera += 1
            self.numero_transaccion += 1
            transaccion = {
                "estado": "APROBADA",
                "tipo": "ALTA_CHEQUERA",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        elif self.chequera == 1:
            print("No puedes dar de alta mas chequeras. El límite de tu cuenta es de 1 chequera. Actualiza tu plan para extender este límite.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_CHEQUERA",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        self.transacciones.append(transaccion)

    def alta_cuenta_corriente(self, moneda):
        transaccion = {}
        if moneda == 1:
            # cuenta corriente usd
            if self.cuenta_corriente_usd == 0:
                print(
                    "Felicitaciones! Ya cuentas con una cuenta corriente en dolares. Se aplicará un cargo mensual de 10USD para mantenerla."
                )
                print(f"Cuentas corrientes: {self.cuenta_corriente_usd}")

                self.cuenta_corriente_usd += 1
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CUENTA_CTE_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        elif moneda == 2:
            # cuenta corriente ars
            if self.cuenta_corriente_ars < 2:
                print("Felicitaciones! Ya cuentas con una cuenta corriente en pesos")
                print(f"Cuentas corrientes: {self.cuenta_corriente_ars}")
                self.cuenta_corriente_ars += 1
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CUENTA_CTE_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif self.cuenta_corriente_ars == 2:
                print(
                    "No puedes dar de alta mas cuentas corrientes en pesos. El límite de tu cuenta es de 2 cuentas. Actualiza tu plan para extender este límite."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CUENTA_CTE_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }

        self.transacciones.append(transaccion)

    def alta_caja_ahorro(self, moneda):
        transaccion = {}
        if moneda == 1:
            #caja ahorro dolares
            if self.caja_ahorro_dolares >= 0:
                print(
                    "Felicitaciones! Ya cuentas con una caja de ahorro en dolares. Se aplicará un cargo mensual de 10USD para mantenerla."
                )
                self.caja_ahorro_dolares += 1
                print(f"Cajas de ahorro: {self.caja_ahorro_dolares}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        elif moneda == 2:
            #caja ahorro pesos
            if self.caja_ahorro_pesos < 2:
                print("Felicitaciones! Ya cuentas con una caja de ahorro en pesos")
                self.caja_ahorro_pesos += 1
                print(f"Cajas de ahorro: {self.caja_ahorro_pesos}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif self.caja_ahorro_pesos == 2:
                print(
                    "No puedes dar de alta mas cajas de ahorro en pesos. El límite de tu cuenta es de 2 cajas de ahorro. Actualiza tu plan para extender este límite."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        
        self.transacciones.append(transaccion)

    def alta_cuenta_de_inversion(self):
        transaccion = {}
        if not self.cuenta_de_inversion:
            self.numero_transaccion += 1
            transaccion = {
                "estado": "APROBADA",
                "tipo": "ALTA_CUENTA_DE_INVERSION",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
            print(
                "Felicidades! Has dado de alta cuenta de inversión."
            )
            self.cuenta_de_inversion = True
        else:
            print("Ya tienes una cuenta de inversion")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_CUENTA_DE_INVERSION",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        
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
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            print("El monto de dolares que desea comprar excede sus fondos en ARS.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": self.now,
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
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            dolar = 1000
            self.monto_usd -= monto_dolar
            self.monto_ars += monto_dolar * dolar
            print("Venta exitosa.")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": self.now,
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
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_ars -= monto_saliente
                self.monto_ars -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": self.now,
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
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia saliente")
                self.monto_usd -= monto_saliente
                self.monto_usd -= comision
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": self.now,
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
            print(
                f"Transferencia exitosa! Se ha aplicado una comisión de ${comision} por esta transferencia entrante")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": self.now,
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
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_RECIBIDA_<USD>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }

        self.transacciones.append(transaccion)

class ClienteBlack:
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero
        self.dni = dni
        self.transacciones = []
        self.monto_ars = 2500000
        self.monto_usd = 1000
        self.tarjeta_debito = 0
        self.caja_ahorro_pesos = 0
        self.caja_ahorro_dolares = 0
        self.retiro_diario_maximo = 100000
        self.retiros_sin_comision = 10000000  # numero "infinito"
        self.numero_transaccion = 0
        self.tarjetas_credito = []
        self.chequera = 0
        self.cuenta_corriente_ars = 0
        self.cuenta_corriente_usd = 0
        self.cuenta_de_inversion = False

        fecha = date.datetime.now()
        self.dia = fecha.day
        self.mes = fecha.month
        self.anio = fecha.year
        self.hora = fecha.hour
        self.minuto = fecha.minute
        self.segundo = fecha.second
        self.now = f"{self.dia}/{self.mes}/{self.anio} {self.hora}:{self.minuto}:{self.segundo}"
        
    def salida_resumen(self):
        salida = {"numero": self.numero_cuenta,
                  "nombre": self.nombre,
                  "apellido": self.apellido,
                  "dni": self.dni,
                  "tipo": "BLACK",
                  "transacciones": self.transacciones
                  }
        
        with open('resumen.html', 'w') as archivo:
            json.dump(salida, archivo)           

    def realizar_retiro(self, opcion):
        transaccion = {}
        monto_retiro = float(input("Ingrese el monto a retirar: $"))
        while monto_retiro <= 0:
            monto_retiro = float(input("El monto a retirar no puede ser 0 o negativo. Ingreselo de nuevo: $"))
        if opcion == 1:
            # retiro por caja
            if monto_retiro > self.monto_ars:
                print("Error: El monto a retirar excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_POR_CAJA",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                if self.retiros_sin_comision > 0:
                    self.retiros_sin_comision -= 1
                    self.monto_ars -= monto_retiro
                    print(f"Retiro exitoso de ${monto_retiro}")
                    print(f"Saldo actual: ${self.monto_ars}")
                    self.numero_transaccion += 1
                    transaccion = {
                        "estado": "ACEPTADA",
                        "tipo": "RETIRO_EFECTIVO_POR_CAJA",
                        "cuentaNumero": self.numero_cuenta,
                        "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                        "monto": monto_retiro,
                        "fecha": self.now,
                        "numero": self.numero_transaccion
                    }
        elif opcion == 2:
            # retiro por cajero
            if monto_retiro > self.monto_ars:
                print("Error: El monto a retirar excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif monto_retiro > self.retiro_diario_maximo:
                comision = monto_retiro * 0.02  # Comisión del 2%
                if self.retiros_sin_comision > 0:
                    self.retiros_sin_comision -= 1
                    self.monto_ars -= monto_retiro
                    self.monto_ars -= comision
                    print(
                        f"El monto a retirar excede el límite diario de retiro de ${self.retiro_diario_maximo}. Se aplicará una comisión de ${comision} a la operación")
                    print(f"Retiro exitoso de ${monto_retiro}")
                    print(f"Saldo actual: ${self.monto_ars}")
                    self.numero_transaccion += 1
                    transaccion = {
                        "estado": "ACEPTADA",
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                        "cuentaNumero": self.numero_cuenta,
                        "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                        "monto": monto_retiro,
                        "fecha": self.now,
                        "numero": self.numero_transaccion
                    }
            else:
                print(f"Retiro exitoso de ${monto_retiro}")
                print(f"Saldo actual: ${self.monto_ars}")
                self.monto_ars -= monto_retiro
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_retiro,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        self.transacciones.append(transaccion)

    def compra_cuotas_credito(self):
        transaccion = {}
        if len(self.tarjetas_credito) == 0:
            print(
                "No posees ninguna tarjeta de credito. Selecciona la opción '5' para dar de alta una.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_EN_CUOTAS_TARJETA_CREDITO_<None>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            for tarjeta in self.tarjetas_credito:
                print(tarjeta)
            numero_tarjeta = int(
                input("Selecciona una de tus tarjetas para pagar: "))
            monto = float(input("Monto a pagar: $"))
            cuotas = int(input("Cantidad de cuotas: "))
            if monto > 600000:
                print("El monto excede el límite de $600000 para pagos en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"¡Transacción exitosa! Se ha realizado una compra de ${monto} en {cuotas} cuotas con una tarjeta {self.tarjetas_credito[(numero_tarjeta-1)]}."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta-1]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        self.transacciones.append(transaccion)

    def compra_credito(self):
        transaccion = {}
        if len(self.tarjetas_credito) == 0:
            print(
                "No posees ninguna tarjeta de credito. Selecciona la opción '5' para dar de alta una.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_TARJETA_CREDITO_<None>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            for tarjeta in self.tarjetas_credito:
                print(tarjeta)
            numero_tarjeta = int(
                input("Selecciona una de tus tarjetas para pagar: "))
            monto = float(input("Monto a pagar: $"))
            if monto > 500000:
                print("El monto excede el límite de $500000 para pagos en una sola vez.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": f"COMPRA_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"¡Transacción exitosa! Se ha realizado una compra de ${monto} con una tarjeta {self.tarjetas_credito[numero_tarjeta -1]}."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_<{self.tarjetas_credito[numero_tarjeta-1]}>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        self.transacciones.append(transaccion)

    def alta_tarjeta_credito(self):
        transaccion = {}
        if len(self.tarjetas_credito) >= 10:
            print("Error: El límite de tarjetas de crédito es de 10.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_TARJETA_CREDITO_<None>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
            pass
        else:
            tipo_tarjeta = int(input(
                "Selecciona la tarjeta que quieras dar de alta: 1-Mastercard, 2-VISA, 3-American Express\n>> "))
            while tipo_tarjeta not in [1, 2, 3]:
                tipo_tarjeta = input(
                    "Opción inválida, por favor selecciona una de estas 3 tarjetas: 1-Mastercard, 2-VISA, 3-American Express\n>> ")
            if tipo_tarjeta == 1:
                # tarjeta MASTER
                self.tarjetas_credito.append(
                    {"tarjeta": "MASTER", "limite_un_pago": 500000, "limite_cuotas": 600000})
                print(
                    f"Felicidades! Se ha agregado una tarjeta de crédito MASTER con límites de $150000 en un pago y $100000 en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "APROBADA",
                    "tipo": f"ALTA_TARJETA_CREDITO_<MASTER>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif tipo_tarjeta == 2:
                # tarjeta VISA
                self.tarjetas_credito.append(
                    {"tarjeta": "VISA", "limite_un_pago": 500000, "limite_cuotas": 600000})
                print(
                    f"Felicidades! Se ha agregado una tarjeta de crédito VISA con límites de $150000 en un pago y $100000 en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "APROBADA",
                    "tipo": f"ALTA_TARJETA_CREDITO_<VISA>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif tipo_tarjeta == 3:
                # tarjeta AMEX
                self.tarjetas_credito.append(
                    {"tarjeta": "AMEX", "limite_un_pago": 500000, "limite_cuotas": 600000})
                print(
                    f"Felicidades! Se ha agregado una tarjeta de crédito American Express con límites de $500000 en un pago y $600000 en cuotas.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "APROBADA",
                    "tipo": f"ALTA_TARJETA_CREDITO_<VISA>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }

        self.transacciones.append(transaccion)

    def alta_tarjeta_debito(self):
        transaccion = {}
        if self.tarjeta_debito <= 4:
            print("Felicitaciones! Se ha dado de alta una nueva tarjeta de débito.")
            self.tarjeta_debito += 1
            print(f"Tarjetas de debito: {self.tarjeta_debito}")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            print("Error: Solo puedes dar de alta 5 tarjetas de débito")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_TARJETA_DEBITO",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        self.transacciones.append(transaccion)

    def alta_chequera(self):
        transaccion = {}
        if self.chequera < 2:
            print("Felicitaciones! Se ha dado de alta una chequera.")
            self.chequera += 1
            self.numero_transaccion += 1
            transaccion = {
                "estado": "APROBADA",
                "tipo": "ALTA_CHEQUERA",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        elif self.chequera == 2:
            print("No puedes dar de alta mas chequeras. El límite de tu cuenta es de 2 chequeras.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_CHEQUERA",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        self.transacciones.append(transaccion)

    def alta_cuenta_corriente(self, moneda):
        transaccion = {}
        if moneda == 1:
            # cuenta corriente usd
            if self.cuenta_corriente_usd < 3:
                print(
                    "Felicitaciones! Ya cuentas con una cuenta corriente en dolares. Se aplicará un cargo mensual de 10USD para mantenerla."
                )
                self.cuenta_corriente_usd += 1
                print(f"Cuentas corrientes: {self.cuenta_corriente_usd}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CUENTA_CTE_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif self.cuenta_corriente_usd == 3:
                print(
                    "No puedes dar de alta mas cuentas corrientes en dolares. El límite de tu cuenta es de 3 cuentas. Actualiza tu plan para extender este límite."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CUENTA_CTE_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        elif moneda == 2:
            # cuenta corriente ars
            if self.cuenta_corriente_ars < 3:
                print("Felicitaciones! Ya cuentas con una cuenta corriente en pesos")
                self.cuenta_corriente_ars += 1
                print(f"Cuentas corrientes: {self.cuenta_corriente_ars}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CUENTA_CTE_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif self.cuenta_corriente_ars == 3:
                print(
                    "No puedes dar de alta mas cuentas corrientes en pesos. El límite de tu cuenta es de 3 cuentas. Actualiza tu plan para extender este límite."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CUENTA_CTE_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }

        self.transacciones.append(transaccion)

    def alta_caja_ahorro(self, moneda):
        transaccion = {}
        if moneda == 1:
            #caja ahorro dolares
            if self.caja_ahorro_dolares < 5:
                print(
                    "Felicitaciones! Ya cuentas con una caja de ahorro en dolares."
                )
                self.caja_ahorro_dolares += 1
                print(f"Cajas de ahorro: {self.caja_ahorro_dolares}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif self.caja_ahorro_dolares >= 5:
                print("Felicitaciones! Ya cuentas con una caja de ahorro en dolares. Se aplicará un cargo mensual de 10USD para mantenerla.")
                self.caja_ahorro_dolares += 1
                print(f"Cajas de ahorro: {self.caja_ahorro_dolares}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
                
        elif moneda == 2:
            #caja ahorro pesos
            if self.caja_ahorro_pesos < 5:
                print("Felicitaciones! Ya cuentas con una caja de ahorro en pesos")
                self.caja_ahorro_pesos += 1
                print(f"Cajas de ahorro: {self.caja_ahorro_pesos}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            elif self.caja_ahorro_pesos == 5:
                print(
                    "No puedes dar de alta mas cajas de ahorro en pesos. El límite de tu cuenta es de 5 cajas de ahorro."
                )
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "ALTA_CAJA_DE_AHORRO_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        
        self.transacciones.append(transaccion)

    def alta_cuenta_de_inversion(self):
        transaccion = {}
        if not self.cuenta_de_inversion:
            self.numero_transaccion += 1
            transaccion = {
                "estado": "APROBADA",
                "tipo": "ALTA_CUENTA_DE_INVERSION",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
            print(
                "Felicidades! Has dado de alta cuenta de inversión."
            )
            self.cuenta_de_inversion = True
        else:
            print("Ya tienes una cuenta de inversion.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "ALTA_CUENTA_DE_INVERSION",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        
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
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            print("El monto de dolares que desea comprar excede sus fondos en ARS.")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": self.now,
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
            self.numero_transaccion += 1
            transaccion = {
                "estado": "RECHAZADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": None,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        else:
            dolar = 1000
            self.monto_usd -= monto_dolar
            self.monto_ars += monto_dolar * dolar
            print("Venta exitosa.")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "COMPRA_DOLAR",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_dolar,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        self.transacciones.append(transaccion)

    def realizar_transferencia_saliente(self):
        transaccion = {}
        moneda = int(input("Seleccione la moneda en la que quiere realizar la transferencia 1-USD / 2-ARS: "))
        while moneda not in [1, 2]:
            moneda = int(
                input("Moneda incorrecta. Elija una de estas dos opciones: 1-USD / 2-ARS: "))

        if moneda == 1:
            monto_saliente = float(
                input("Ingrese el monto que desea transferir en USD: $"))
            while monto_saliente <= 0:
                monto_saliente = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))

            if monto_saliente > self.monto_usd:
                print("El monto que desea transferir excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print("Transferencia exitosa!")
                self.monto_usd -= monto_saliente
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<USD>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
        elif moneda == 2:
            monto_saliente = float(
                input("Ingrese el monto que desea transferir en ARS: $"))
            while monto_saliente <= 0:
                monto_saliente = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))

            if monto_saliente > self.monto_ars:
                print("El monto que desea transferir excede sus fondos.")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "RECHAZADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": None,
                    "fecha": self.now,
                    "numero": self.numero_transaccion
                }
            else:
                print(
                    f"Transferencia exitosa!")
                self.monto_ars -= monto_saliente
                print(f"Saldo actual en ARS: ${self.monto_ars}")
                print(f"Saldo actual en USD: ${self.monto_usd}")
                self.numero_transaccion += 1
                transaccion = {
                    "estado": "ACEPTADA",
                    "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                    "cuentaNumero": self.numero_cuenta,
                    "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                    "monto": monto_saliente,
                    "fecha": self.now,
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
            self.monto_ars += monto_entrante
            print(
                f"Transferencia exitosa!")
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_ENVIADA_<ARS>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }
        elif moneda == 1:
            monto_entrante = float(
                input("Ingrese el monto que desea recibir en USD: $"))
            while monto_entrante <= 0:
                monto_entrante = float(
                    input("El monto no puede ser 0 o negativo. Ingreselo de nuevo: $"))
            print(
                f"Transferencia exitosa!")
            self.monto_usd += monto_entrante
            print(f"Saldo actual en ARS: ${self.monto_ars}")
            print(f"Saldo actual en USD: ${self.monto_usd}")
            self.numero_transaccion += 1
            transaccion = {
                "estado": "ACEPTADA",
                "tipo": "TRANSFERENCIA_RECIBIDA_<USD>",
                "cuentaNumero": self.numero_cuenta,
                "permitidoActualParaTransaccion": self.retiro_diario_maximo,
                "monto": monto_entrante,
                "fecha": self.now,
                "numero": self.numero_transaccion
            }

        self.transacciones.append(transaccion)

def interactuar_con_cliente(tipo_cliente):
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    numero = int(input("Numero: "))
    dni = str(input("Dni: "))
    if tipo_cliente == 1:
        cliente = ClienteClassic(nombre, apellido, numero, dni)
    elif tipo_cliente  == 2:
        cliente = ClienteGold(nombre, apellido, numero, dni)
    elif tipo_cliente  == 3:
        cliente = ClienteBlack(nombre, apellido, numero, dni)
    while True:
        print("\nEscribe la opción que deseas utilizar (o '0' para salir):")
        print("1 - Retirar efectivo desde un cajero")
        print("2 - Retirar efectivo desde caja")
        print("3 - Compra en cuotas con tarjeta de crédito")
        print("4 - Compra con tarjeta de crédito")
        print("5 - Alta tarjeta de crédito")
        print("6 - Alta tarjeta de debito")
        print("7 - Alta chequera")
        print("8 - Alta cuenta corriente en pesos")
        print("9 - Alta cuenta corriente en dolares")
        print("10 - Alta caja de ahorro en pesos")
        print("11 - Alta caja de ahorro en dolares")
        print("12 - Alta cuenta de inversion")
        print("13 - Compra dólar")
        print("14 - Venta dólar")
        print("15 - Transferencia saliente")
        print("16 - Transferencia entrante")

        opcion = int(input(">> "))

        if opcion == 0:
            break
        elif opcion == 1:
            cliente.realizar_retiro(1)
        elif opcion == 2:
            cliente.realizar_retiro(2)
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
            cliente.alta_cuenta_corriente(2)
        elif opcion == 9:
            cliente.alta_cuenta_corriente(1)
        elif opcion == 10:
            cliente.alta_caja_ahorro(2)
        elif opcion == 11:
            cliente.alta_caja_ahorro(1)
        elif opcion == 12:
            cliente.alta_cuenta_de_inversion()
        elif opcion == 13:
            cliente.compra_dolar()
        elif opcion == 14:
            cliente.venta_dolar()
        elif opcion == 15:
            cliente.realizar_transferencia_saliente()
        elif opcion == 16:
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
            interactuar_con_cliente(1)
            print("El resumen con las operaciones realizadas ha sido exportado!")
            op = 0
        elif op == 2:
            interactuar_con_cliente(2)
            print("El resumen con las operaciones realizadas ha sido exportado!")
            op = 0
        elif op == 3:
            interactuar_con_cliente(3)
            print("El resumen con las operaciones realizadas ha sido exportado!")
            op = 0
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            op = input(
                "1 - Cliente Classic \n2 - Cliente Gold\n3 - Cliente Black\n>>")
