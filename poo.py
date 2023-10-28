#                            TIPOS DE CLIENTES: 
#CLASSIC          GOLD        BLACK
#                           TIPOS DE CUENTAS: 
#_CAJA DE AHORRO EN PESO
#_CAJA DE AHORRO EN DOLARES
#_CUENTA CORRIENTE EN DOLARES
#_CUENTA DE INVERSION
#                            TIPOS DE TARJETA DEBITO Y CREDITO
# MASTERCARD
#VISA
#AMERICAN EXPRESS
 

#OPCION DE DONDE DEBE ELEGIR EL USUARIO




VARIABLE=(
'''RETIRO_EFECTIVO_CAJERO_AUTOMATICO 
    RETIRO_EFECTIVO_POR_CAJA 
    COMPRA_EN_CUOTAS_TARJETA_CREDITO_<tipo de tarjeta> 
    COMPRA_TARJETA_CREDITO_<tipo de tarjeta> 
    ALTA_TARJETA_CREDITO_<Tipo de tarjeta> 
    ALTA_TARJETA_DEBITO 
    ALTA_CHEQUERA 
    ALTA_CUENTA_CTE_<Tipo de moneda> 
    ALTA_CAJA_DE_AHORRO_<Tipo de moneda> 
    ALTA_CUENTA_DE_INVERSION 
    COMPRA_DOLAR 
    VENTA_DOLAR 
    TRANSFERENCIA_ENVIADA_<Tipo moneda> 
    TRANSFERENCIA_RECIBIDA_<Tipo moneda''')


class Tarjeta:
    def __init__(self,tarjeta,caja_ahorro,retiro,comision):
        self.tarjeta= tarjeta
        self.caja_ahorro= caja_ahorro
        self.retiro = retiro
        self.comision = comision


class Classic(Tarjeta):
    def __init__(self, tarjeta, caja_ahorro,retiro,caja_dolar,tarjeta_credito,comision):
        super().__init__( tarjeta, caja_ahorro,retiro,comision)
        self.caja_dolar= caja_dolar
        self.tarjeta_credito = tarjeta_credito
        
    def __str__(self):
        return '1'

        
                
        


        
class Gold(Tarjeta):
    def __init__(self, tarjeta, caja_ahorro,retiro,cuentas_inversion,comision,tener_chequera):
        super().__init__( tarjeta, caja_ahorro,retiro,comision)
        self.cuentas_inversion=cuentas_inversion
        self.tener_chequera = tener_chequera

class Black(Tarjeta):
    def __init__(self, tarjeta, caja_ahorro, retiro,cuentas_corrientes,cuentas_inversion,tener_chequera):
        super().__init__(tarjeta, caja_ahorro, retiro)
        self.cuentas_corrientes = cuentas_corrientes
        self.cuentas_inversion = cuentas_inversion
        self.tener_chequera =tener_chequera



class Usuario:
    def __init__(self, nombre, tipo_tarjeta):
        self.nombre = nombre
        self.tipo_tarjeta = tipo_tarjeta
        self.tarjeta = None  # Inicialmente, el usuario no tiene una tarjeta asignada

    def asignar_tarjeta(self):
        if self.tipo_tarjeta == "Classic":
            self.tarjeta=1
            self.tarjeta = Classic(self.tipo_tarjeta, self.tarjeta, 500, 50, 200, 10)
            
        elif self.tipo_tarjeta == "Gold":
            self.tarjeta = Gold(self.nombre, 200, 1000, 500, 15, True)
        elif self.tipo_tarjeta == "Black":
            self.tarjeta = Black(self.nombre, 300, 1500, 3, 20, True, True)


    def info_cliente(self):
        while True:
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
                opcion = input("Selecciona una opción: ") #.aca van del 1 al 15 para las funciones y todo
                if opcion == '12':
                    monto_dolares = int(input("Ingresa el monto en dólares: "))
                    monto_total = calcular_monto_total(precio_dolar, monto_dolares)
                    print(f"Monto total a gastar: {monto_total} dólares")
            else:
                return "El usuario no tiene una tarjeta asignada."


# FUNCIONES PUNTO 3

def calcular_monto_total(precio_dolar, monto):
    impuesto_pais = 0.9  
    ganancias = 0.21 # se puede editar a gusto esto como el imp.pais
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

# aca tenemos que ver el monto que quieren retirar, habria que hacer una funcion para que ingrese el monto
precio_dolar = 550
monto_dolares = 100000 #esto es un ejemplo

# monto total con impuesto pais y ganancia
monto_total = calcular_monto_total(precio_dolar, monto_dolares)
print(f"Monto total a gastar: {monto_total} dólares")

# descuenta comision 
monto_descontado = descontar_comision(monto_dolares, 21) # creo que asi es, hay que ver cuanto % le ponemos de descuento, yo puse 21
print(f"Monto después de la comisión: {monto_descontado} dólares")

# el total de un plazo fijo con un interes, ahora tambien le puse 7, pero podemos cambiarlo
monto_plazo_fijo = calcular_monto_plazo_fijo(monto_dolares, 7)
print(f"Monto final después del plazo fijo: {monto_plazo_fijo} dólares")

# hay que editar los montos o los porcentajes para que no sea una locura el total de cada monto
#me queda ver que no se ejecute primero, porque apenas ejecutas el codigo te tira los resultados

usuario1 = Usuario("federico", "Classic")
usuario1.asignar_tarjeta()
print(usuario1.info_cliente())

