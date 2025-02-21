class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario

    def mostrar_horarios (self, dia, hora_inicio, hora_fin):
        print (f'Dia: {self.dia}, Horario de inicio: {self.hora_inicio}, Horario fin: {self.hora_fin}')


    def modificar_horario (self, dia, hora_inicio, hora_fin):


    def __str__(self):
        return f"{self.curso}, {self.dia} / {self.hora_inicio}, {self.hora_fin}"

    def __repr__(self):
        return (
            f"Curso: {self.curso}"
            f"Dia: {self.dia}"
            f"Hora de inicio: {self.hora_inicio}"
            f"HOra fin: {self.hora_fin}"
        )

    def desde_tupla ():


    def es_horario_valido ():