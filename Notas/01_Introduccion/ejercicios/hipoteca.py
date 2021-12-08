# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

#---------------------------------------------------- 1.8 --------------------------------------------------------------

'''saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0.0
pago_extra = 1000.0

while saldo > 0.0:
    mes += 1.0
    if mes <= 12.0:
        pago_extra = 1000.0
    else:
        pago_extra = 0
    saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
    total_pagado = total_pagado + pago_mensual + pago_extra

print('Total pagado', round(total_pagado, 2), mes)'''

#--------------------------- 1.9 ---------------------------------------------------------------------------------------

'''saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
monto_pago_extra = 0

while saldo > 0.0:
    mes += 1.0
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        monto_pago_extra = pago_extra
    else:
        monto_pago_extra = 0
    saldo = saldo * (1+tasa/12) - pago_mensual - monto_pago_extra
    total_pagado = total_pagado + pago_mensual + monto_pago_extra

print('Total pagado', round(total_pagado, 2), mes)'''

#--------------------------------------1.10-----------------------------------------------------------------------------

'''saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
monto_pago_extra = 0

while saldo > 0.0:
    mes += 1.0
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        monto_pago_extra = pago_extra
    else:
        monto_pago_extra = 0
    saldo = saldo * (1+tasa/12) - pago_mensual - monto_pago_extra
    total_pagado = total_pagado + pago_mensual + monto_pago_extra
    print("Mes:", mes, "/ Total pagado:", round(total_pagado, 2), "/ Saldo restante:", round(saldo, 2))

print('Total pagado:', round(total_pagado, 2), 'Meses:', mes)'''

#--------------------------------------1.11-----------------------------------------------------------------------------

'''saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
monto_pago_extra = 0

while saldo > 0.0:

    mes += 1

    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        monto_pago_extra = pago_extra
    else:
        monto_pago_extra = 0

    if saldo <= pago_mensual:
        pago_mensual = round(saldo)

    saldo = saldo * (1+tasa/12) - pago_mensual - monto_pago_extra

    total_pagado = total_pagado + pago_mensual + monto_pago_extra

    print("Mes:", mes, "/ Total pagado:", round(total_pagado, 2), "/ Saldo restante a pagar:", round(saldo, 2))

print('Total pagado:', round(total_pagado, 2), 'Meses:', mes)'''

# Juan 1.11

'''saldo = 500000.0
total_pagado = 0

tasa = 0.05

pago_mensual = 2684.11
pago_extra = 1000
monto_pago_total = 0

mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108


while saldo > 0.0:

    mes += 1

    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        monto_pago_extra = pago_extra
    else:
        monto_pago_extra = 0

    if saldo <= pago_mensual:
        saldo = saldo * (1 + tasa / 12)
        pago_mensual = saldo
        saldo = saldo - pago_mensual
    else:
        saldo = saldo * (1 + tasa / 12) - pago_mensual - monto_pago_extra

    total_pagado = total_pagado + pago_mensual + monto_pago_extra

    print("Mes:", mes, "/ Total pagado:", round(total_pagado, 2), "/ Saldo restante a pagar:", round(saldo, 2))

print('Total pagado:', round(total_pagado, 2), 'Meses:', mes)'''

#-----------------------------------------------------------------------------------------------------------------------

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

    print(f'Mes: {mes_actual} / Total pagado: {round(total_pagado, 2)} / Saldo restante a pagar: {round(saldo, 2)}')

print(f'Total pagado: {round(total_pagado, 2)} / Meses: {mes_actual}')