calificacionAlumno = [8, 7, 9, 10]
calificacionTotal=0
numeroParciales = len(calificacionAlumno)
for calificacionParciales in calificacionAlumno: 
    calificacionTotal=calificacionTotal+calificacionParciales
p=calificacionTotal/numeroParciales
print("El promedio fue : "+ str(p))