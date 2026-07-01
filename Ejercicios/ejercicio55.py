# Ejercicio 55: Sistema Bancario Simple
banco = {}
historial_transacciones = []

def crear_cuenta(numero_cuenta, titular, saldo_inicial=0, tipo="Ahorros"):
    banco[numero_cuenta] = {"titular": titular, "saldo": saldo_inicial, "tipo": tipo}

def depositar(numero_cuenta, monto):
    if numero_cuenta in banco and monto > 0:
        banco[numero_cuenta]["saldo"] += monto
        historial_transacciones.append((numero_cuenta, "Depósito", monto))
        return True
    return False

def retirar(numero_cuenta, monto):
    if numero_cuenta in banco and 0 < monto <= banco[numero_cuenta]["saldo"]:
        banco[numero_cuenta]["saldo"] -= monto
        historial_transacciones.append((numero_cuenta, "Retiro", -monto))
        return True
    print("Fondos insuficientes o cuenta inválida")
    return False

def transferir(cuenta_origen, cuenta_destino, monto):
    if cuenta_origen in banco and cuenta_destino in banco and 0 < monto <= banco[cuenta_origen]["saldo"]:
        banco[cuenta_origen]["saldo"] -= monto
        banco[cuenta_destino]["saldo"] += monto
        historial_transacciones.append((cuenta_origen, "Transferencia", -monto))
        return True
    print("Fondos insuficientes o cuentas inválidas")
    return False

crear_cuenta(1001, "Juan Pérez", 1500)
crear_cuenta(1002, "Ana López", 800)

depositar(1001, 500)
retirar(1001, 200)
transferir(1001, 1002, 300)

cuenta = banco[1001]
print("Cuenta #1001:", cuenta["titular"])
print("Saldo: $", cuenta["saldo"])
print("Últimas transacciones:")
for num_cuenta, tipo, monto in historial_transacciones:
    if num_cuenta == 1001:
        if monto > 0:
            print("-", tipo, ": +$", monto)
        else:
            print("-", tipo, ": -$", abs(monto))
