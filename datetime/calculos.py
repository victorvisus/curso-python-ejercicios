from datetime import date, datetime, timedelta

# Calcular la diferencia entre dos puntos en el tiempo
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Tiempo hasta año nuevo:  27 days, 0:00:00
print("Tiempo hasta año nuevo: ", time_left_for_newyear)

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
t3 = datetime.now()
diff = t2 - t1
diff = t3 - t1
print("Tiempo hasta año nuevo:", diff)  # Tiempo hasta año nuevo: 26 days, 23:01:00

# Calcular diferencias con timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

# cuanto falta a que acabe el curso
findeCurso = datetime(year=2026, month=6, day=19, hour=14, minute=30, second=0)
hoy = datetime.now()
print("Dias restantes para el curso:", findeCurso - hoy)
# cuantas semanas es

print("Semanas restantes para el curso:", (findeCurso - hoy) / timedelta(weeks=1))
"""
Cómo funciona: Aquí estás dividiendo un objeto timedelta (la duración total) entre otro objeto timedelta (una semana exacta).
Ventaja: Es muy legible. Si mañana quieres saber los meses (aunque timedelta no tiene meses por su duración variable), o las horas, solo cambias el divisor: / timedelta(hours=1).
Resultado: Te dará un número decimal (float) muy preciso, incluyendo los días y horas sobrantes como parte decimal.
"""
print("Semanas restantes para el curso:", (findeCurso - hoy).days / 7)
"""

"""
print("Test --------------------------------------------------")
diffTiempo = findeCurso - hoy
print(diffTiempo)
semanas = diffTiempo // timedelta(weeks=1)
semanasResto = diffTiempo % timedelta(weeks=1)
print("Teimpo: ", semanas, " semanas y ", semanasResto)

print("Test - UNIX ---------------------------------------------")
unixTiempoDiasDif = diffTiempo.total_seconds()
print("Tiempo en dias: ", unixTiempoDiasDif)
delta = timedelta(seconds=unixTiempoDiasDif)
print(delta)
semanas = delta.days // 7
dias_restantes = delta.days % 7
print("Teimpo: ", semanas, " semanas y ", dias_restantes, " dias")
horas = delta.seconds // 3600
minutos = (delta.seconds % 3600) // 60
segundos = (delta.seconds % 3600) % 60
print(
    f"Tiempo: {semanas} semanas y {dias_restantes} dias y {horas} horas y {minutos} minutos y {segundos} segundos"
)
