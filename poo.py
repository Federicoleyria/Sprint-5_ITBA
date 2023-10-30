class Tarjeta:
    def __init__(self, tarjeta, caja_ahorro, retiro, comision):
        self.tarjeta = tarjeta
        self.caja_ahorro = caja_ahorro
        self.retiro = retiro
        self.comision = comision


class Classic(Tarjeta):
    def __init__(self, tarjeta, caja_ahorro, retiro, caja_dolar, tarjeta_credito, comision):
        super().__init__(tarjeta, caja_ahorro, retiro, comision)
        self.caja_dolar = caja_dolar
        self.tarjeta_credito = tarjeta_credito

    def __str__(self):
        return '1'


class Gold(Tarjeta):
    def __init__(self, tarjeta, caja_ahorro, retiro, cuentas_inversion, comision, tener_chequera):
        super().__init(tarjeta, caja_ahorro, retiro, comision)
        self.cuentas_inversion = cuentas_inversion
        self.tener_chequera = tener_chequera


class Black(Tarjeta):
    def __init__(self, tarjeta, caja_ahorro, retiro, cuentas_corrientes, cuentas_inversion, tener_chequera):
        super().__init(tarjeta, caja_ahorro, retiro)
        self.cuentas_corrientes = cuentas_corrientes
        self.cuentas_inversion = cuentas_inversion
        self.tener_chequera = tener_chequera


class Usuario:
    def __init__(self, nombre, tipo_tarjeta):
        self.nombre = nombre
        self.tipo_tarjeta = tipo_tarjeta
        self.tarjeta = None  # Inicialmente, el usuario no tiene una tarjeta asignada

    def asignar_tarjeta(self):
        if self.tipo_tarjeta == "Classic":
            self.tarjeta = Classic(self.tipo_tarjeta, 200, 500, 10, 400, 50)
        elif self.tipo_tarjeta == "Gold":
            self.tarjeta = Gold(self.tipo_tarjeta, 300, 1000, 5, 20, True)
        elif self.tipo_tarjeta == "Black":
            self.tarjeta = Black(self.tipo_tarjeta, 400, 1500, 2, 10, True, True)

    def realizar_transaccion(self, opcion):
        if opcion == '1':
            self.retirar_efectivo_cajero_automatico()
        elif opcion == '2':
            self.retirar_efectivo_por_caja()
        elif opcion == '3':
            self.comprar_en_cuotas_tarjeta_credito()
        elif opcion == '4':
            self.comprar_tarjeta_credito()
        elif opcion == '5':
            self.alta_tarjeta_credito()
        elif opcion == '6':
            self.alta_tarjeta_debito()
        elif opcion == '7':
            self.alta_chequera()
        elif opcion == '8':
            self.alta_cuenta_corriente()
        elif opcion == '9':
            self.alta_cuenta_cte_moneda()
        elif opcion == '10':
            self.alta_caja_ahorro_moneda()
        elif opcion == '11':
            self.alta_cuenta_inversion()
        elif opcion == '12':
            self.comprar_dolar()
        elif opcion == '13':
            self.venta_dolar()
        elif opcion == '14':
            self.transferencia_enviada_moneda()
        elif opcion == '15':
            self.transferencia_recibida_moneda()
        else:
            print("Opción no válida.")

    def retirar_efectivo_cajero_automatico(self):
        print("Has seleccionado RETIRO_EFECTIVO_CAJERO_AUTOMATICO")

    def retirar_efectivo_por_caja(self):
        print("Has seleccionado RETIRO_EFECTIVO_POR_CAJA")

    def comprar_en_cuotas_tarjeta_credito(self):
        print("Has seleccionado COMPRA_EN_CUOTAS_TARJETA_CREDITO")

    def comprar_tarjeta_credito(self):
        print("Has seleccionado COMPRA_TARJETA_CREDITO")

    def alta_tarjeta_credito(self):
        print("Has seleccionado ALTA_TARJETA_CREDITO")

    def alta_tarjeta_debito(self):
        print("Has seleccionado ALTA_TARJETA_DEBITO")

    def alta_chequera(self):
        print("Has seleccionado ALTA_CHEQUERA")

    def alta_cuenta_corriente(self):
        print("Has seleccionado ALTA_CUENTA_CORRIENTE")

    def alta_cuenta_cte_moneda(self):
        print("Has seleccionado ALTA_CUENTA_CTE_MONEDA")

    def alta_caja_ahorro_moneda(self):
        print("Has seleccionado ALTA_CAJA_DE_AHORRO_MONEDA")

    def alta_cuenta_inversion(self):
        print("Has seleccionado ALTA_CUENTA_DE_INVERSION")

    def comprar_dolar(self):
        monto_dolares = int(input("Ingresa el monto en dólares: "))
        monto_total = calcular_monto_total(precio_dolar, monto_dolares)
        print(f"Monto total a gastar: {monto_total} dólares")

    def venta_dolar(self):
        print("Has seleccionado VENTA_DOLAR")

    def transferencia_enviada_moneda(self):
        print("Has seleccionado TRANSFERENCIA_ENVIADA_MONEDA")

    def transferencia_recibida_moneda(self):
        print("Has seleccionado TRANSFERENCIA_RECIBIDA_MONEDA")

    def info_cliente(self):
        if self.tarjeta:
            print(f'''
                {'#' * 50}
                Bienvenido al banco Barro, {self.nombre},
                recuerda que cuentas con {self.tarjeta} ,
                cuenta con un monto de retiro de {self.tarjeta.retiro}.
                
                1. RETIRO_EFECTIVO_CAJERO_AUTOMATICO
                2. RETIRO_EFECTIVO_POR_CAJA
                3. COMPRA_EN_CUOTAS_TARJETA_CREDITO
                4. COMPRA_TARJETA_CREDITO
                5. ALTA_TARJETA_CREDITO
                6. ALTA_TARJETA_DEBITO
                7. ALTA_CHEQUERA
                8. ALTA_CUENTA_CORRIENTE
                9. ALTA_CUENTA_CTE_MONEDA
                10. ALTA_CAJA_DE_AHORRO_MONEDA
                11. ALTA_CUENTA_DE_INVERSION
                12. COMPRA_DOLAR
                13. VENTA_DOLAR
                14. TRANSFERENCIA_ENVIADA_MONEDA
                15. TRANSFERENCIA_RECIBIDA_MONEDA
                
                Para depositar dinero, ingresa 1.
                Para retirar dinero, ingresa 2.
                Para salir del programa, ingresa 3.
                {'#' * 50}
            ''')
            opcion = input("Selecciona una opción: ")  #aca son las opciones 1-15 son para las funciones
            self.realizar_transaccion(opcion)
        else:
            return "El usuario no tiene una tarjeta asignada."


# FUNCIONES PUNTO 3

def calcular_monto_total(precio_dolar, monto):
    impuesto_pais = 0.9
    ganancias = 0.21
    impuesto = monto * impuesto_pais
    ganancias = monto * ganancias
    monto_total = monto + impuesto + ganancias
    monto_total_en_pesos = monto_total * precio_dolar
    return monto_total_en_pesos

def descontar_comision(monto, comision_porcentaje):
    comision = monto * (comision_porcentaje / 100)
    monto_descontado = monto - comision
    return monto_descontado

def calcular_monto_plazo_fijo(monto, tasa_interes):
    monto_final = monto * (1 + (tasa_interes / 100))
    return monto_final


precio_dolar = 550
monto_dolares = 100000

usuario1 = Usuario("federico", "Classic")
usuario1.asignar_tarjeta()
print(usuario1.info_cliente())
