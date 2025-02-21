class Profesor:
    total_profesores = 0

    def __init__(self, nombre, especialidad, cursos_asignados):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        Profesor.total_profesores += 1
    def asignar_curso(self,curso):
        self.cursos_asignados.append(curso)
    def mostrar_informacion(self):
        print(self.nombre)
        print(self.especialidad)
        for i in range(0,len(self.cursos_asignados)):
            print(self.cursos_asignados[i])
    def __str__(self):
        return f"{self.nombre},{self.especialidad},{self.cursos_asignados}"
    def __repr__(self):
        return(
            f"{type(self).__name__}"
            f"(nombre={self.nombre}, "
            f"especialidad={self.especialidad}, "
            f"cursos_asisgnados={self.cursos_asignados}. "
            )
    @classmethod
    def desde_tupla(cls,tupla):
        return cls(*tupla)

    def esta_disponible_para_nuevo_curso(self):
        return print("SI")