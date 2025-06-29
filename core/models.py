from django.db import models

# Create your models here.


from django.db import models

# -------------------- PLANES Y SUSCRIPCIONES --------------------

class PlanSuscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='logos/')
    rfc = models.CharField(max_length=13)
    direccion = models.TextField()
    email_contacto = models.EmailField()
    telefono_contacto = models.CharField(max_length=15)
    fecha_registro = models.DateField()
    status = models.BooleanField(default=True)
    administrador = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, related_name='empresas_admin')

class SuscripcionEmpresa(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    status = models.BooleanField(default=True)
    plan_suscripcion = models.ForeignKey(PlanSuscripcion, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Pago(models.Model):
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    transaccion_id = models.CharField(max_length=100)
    suscripcion_empresa = models.ForeignKey(SuscripcionEmpresa, on_delete=models.CASCADE)

# -------------------- USUARIOS Y PLANTAS --------------------

class Usuario(models.Model):
    apellido_materno = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_registro = models.DateField()
    nivel_usuario = models.IntegerField()
    status = models.BooleanField(default=True)
    admin_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    fecha_creacion = models.DateField()
    status = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class AdminPlanta(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    access_status = models.BooleanField(default=True)

# -------------------- ESTRUCTURA EMPRESARIAL --------------------

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_registro = models.DateField()
    status = models.BooleanField(default=True)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    antiguedad = models.IntegerField()
    status = models.BooleanField(default=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

# -------------------- EVALUACIONES --------------------

class TipoEvaluacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Evaluacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    status = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_evaluacion = models.ForeignKey(TipoEvaluacion, on_delete=models.CASCADE)

class SeccionEvaluacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    numero_orden = models.IntegerField()
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

class ConjuntoOpciones(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    predefinida = models.BooleanField(default=False)

class OpcionConjunto(models.Model):
    texto_opcion = models.CharField(max_length=200)
    valor_booleano = models.BooleanField(null=True, blank=True)
    valor_numerico = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    puntaje_escala = models.IntegerField(null=True, blank=True)
    numero_orden = models.IntegerField()
    conjunto_opciones = models.ForeignKey(ConjuntoOpciones, on_delete=models.CASCADE)

class Pregunta(models.Model):
    texto_pregunta = models.TextField()
    tipo_respuesta = models.CharField(max_length=50)
    es_obligatoria = models.BooleanField(default=True)
    pregunta_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    activador_padre = models.BooleanField(default=False)

class SeccionPregunta(models.Model):
    seccion = models.ForeignKey(SeccionEvaluacion, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    numero_orden = models.IntegerField()
    opcion_conjunto = models.ForeignKey(ConjuntoOpciones, on_delete=models.SET_NULL, null=True, blank=True)

# -------------------- ASIGNACIONES Y RESPUESTAS --------------------

class Asignacion(models.Model):
    token_acceso = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    status = models.BooleanField(default=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='empleado_asignado')
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    evaluado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='empleado_evaluado')

class ResultadoEvaluacion(models.Model):
    puntaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_registro = models.DateField()
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)

class Respuesta(models.Model):
    respuesta_abierta = models.TextField(null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_id = models.IntegerField(null=True, blank=True)  # Se puede usar para relación con opción
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    evaluacion_asignada = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
