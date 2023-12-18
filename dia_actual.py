import datetime

def pedir_dia_actual():
    dia = datetime.date.today()
    dia = dia.weekday()
    # print(type(dia))
    dicc_dias = { 0 : "lunes",
                 1: "martes",
                 2: "miércoles",
                 3: "jueves",
                 4: "viernes",
                 5: "sábado",
                 6: "domingo"}
    return f"Hoy es {dicc_dias[dia]}"
    

pedir_dia_actual()