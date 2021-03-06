# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Rol(models.Model):
    idrol=models.AutoField(primary_key=True)
    roltipo = models.CharField(max_length=10)
    roldescripcion = models.CharField(max_length=50)

    def __str__(self):
        return '%s: %s' % (self.id_rol, self.tipo)

class Usuario(models.Model):
    idusuario= models.AutoField(primary_key=True)
    idrol= models.ForeignKey(Rol,on_delete=models.CASCADE)
    usuariopassword= models.CharField(max_length=65)
    usuarionombre= models.CharField(max_length=20)
    usuarioapellido= models.CharField(max_length=20)
    usuariomail= models.CharField(max_length=20)
    usuariodireccion=models.CharField(max_length=80)
    usuarionickname = models.CharField(max_length=20)
    usuariofoto = models.CharField(max_length=300)

    def __str__(self):
        return '%s: %s %s %s' % (self.idusuario, self.usuarionickname, self.usuariomail, self.usuariofoto)


class Raza(models.Model):
    idraza = models.AutoField(primary_key=True)
    razanombre = models.CharField(max_length=30)
    razadescripcion = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s %s' % (self.idraza, self.razanombre, self.razadescripcion)


class TipoMascota(models.Model):
    idtipo = models.AutoField(primary_key=True)
    tiponombre = models.CharField(max_length=30)
    tipodescripcion = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s %s' % (self.idtipo, self.tiponombre, self.tipodescripcion)


class Mascota(models.Model):
    idmascota = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    idraza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    idtipo = models.TipoMascota(TipoMascota, on_delete=models.CASCADE)
    mascotanombre = models.CharField(max_length=100)
    mascotaedad = models.IntegerField(default=None)
    mascotasexo = models.CharField(max_length=10)
    mascotafoto = models.CharField(max_length=300)
        
    def __str__(self):
        return '%s: %s %s %s %s %s %s %s' % (self.idmascota, self.idusuario, self.idraza, self.idtipo, self.mascotanombre, self.mascotaedad, self.mascotasexo, self.mascotafoto)


class Local(models.Model):
    idlocal = models.AutoField(primary_key=True)
    localnombre = models.CharField(max_length=20)
    localdireccion = models.CharField(max_length=50)
    localtelefono = models.CharField(max_length=10)
    localmail = models.CharField(max_length=20)
    localPropietario = models.CharField(max_length=50)
    locallike = models.IntegerField(default=None)
    localfoto = models.CharField(max_length=300)

    def __str__(self):
        return '%s: %s %s %s %s %s %s %s' % (self.idlocal, self.localnombre, self.localdireccion, self.localtelefono, self.localmail, self.localPropietario, self.locallike, self.localfoto)

class Recomendar(models.Model):
    idrecomendar = models.AutoField(primary_key=True)
    idlocal = models.ForeignKey(Local, on_delete=CASCADE)
    idusuario = models.ForeignKey(Usuario,on_delete=CASCADE)
    recomendarfecha = models.DateField(default=None)
    recomendardetalle = models.CharField(max_length=200)

    def __str__(self):
        return '%s: %s %s %s %s' % (self.idrecomendar, self.idlocal, self.idusuario, self.recomendarfecha, self.recomendardetalle)


class Cuidado(models.Model):
    idcuidado = models.AutoField(primary_key=True)
    idpusuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    cuidadofecha = models.DateField(default=None)
    cuidadodetalle = models.CharField(max_length=300)
    cuidadolike = models.IntegerField(default=None)

    def __str__(self):
        return '%s: %s %s %s %s' % (self.idcuidado, self.idusuario, self.cuidadofecha, self.cuidadodetalle, self.cuidadofecha)


class Planificacion(models.Model):
    idplanificacion = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey (Usuario, on_delete=CASCADE)
    idmascota = models.ForeingKey (Mascota, on_delete= CASCADE)
    planificacionfecha = models.DateField(default=None)
    planificaciondescripcion = models.CharField(max_length=150)

    def __str__(self):
        return '%s: %s %s %s %s' % (self.idplanificacion, self.idusuario, self.idmascota, self.planificacionfecha, self.planificaciondescripcion)
