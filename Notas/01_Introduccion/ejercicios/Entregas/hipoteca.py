# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca


#Balance
saldo = 500_000.0
total_pagado = 0.0
tasa = 0.05

#Pago_extra
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

#Pago_mensual
mes_actual = 0
pago_mensual = 2684.11
monto_pago_mensual_total = 0

while saldo > 0.0:

    mes_actual += 1

    if mes_actual >= pago_extra_mes_comienzo and mes_actual <= pago_extra_mes_fin:
        monto_pago_mensual_total = pago_mensual + pago_extra
    else:
        monto_pago_mensual_total = pago_mensual

    saldo *= (1 + tasa / 12)

    if saldo <= monto_pago_mensual_total:
        monto_pago_mensual_total = saldo

    saldo -= monto_pago_mensual_total
    total_pagado += monto_pago_mensual_total

    print(mes_actual, round(total_pagado, 2), round(saldo, 2))

print(f'Total pagado: {round(total_pagado, 2)} \nMeses: {mes_actual}')