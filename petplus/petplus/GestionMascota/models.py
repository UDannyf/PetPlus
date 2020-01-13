# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CuidadoMascota(models.Model):
    idcuidado_mascota = models.IntegerField(db_column='idCuidado_Mascota', primary_key=True)  # Field name made lowercase.
    cuidadopropietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='cuidadoPropietario')  # Field name made lowercase.
    fechacuidado = models.DateTimeField(db_column='fechaCuidado', blank=True, null=True)  # Field name made lowercase.
    detallecuidado = models.CharField(db_column='detalleCuidado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    likecuidado = models.IntegerField(db_column='likeCuidado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuidado_mascota'
        unique_together = (('idcuidado_mascota', 'cuidadopropietario'),)


class Local(models.Model):
    idlocal = models.IntegerField(db_column='idLocal', primary_key=True)  # Field name made lowercase.
    localdireccion = models.CharField(db_column='localDireccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    localtelefono = models.CharField(db_column='localTelefono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    localmail = models.CharField(db_column='localMail', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'local'


class Mascota(models.Model):
    idmascota = models.IntegerField(db_column='idMascota', primary_key=True)  # Field name made lowercase.
    nombremascota = models.CharField(db_column='nombreMascota', max_length=45, blank=True, null=True)  # Field name made lowercase.
    propietariomascota = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='propietarioMascota')  # Field name made lowercase.
    edadmascota = models.IntegerField(db_column='edadMascota', blank=True, null=True)  # Field name made lowercase.
    razamascota = models.ForeignKey('Raza', models.DO_NOTHING, db_column='razaMascota')  # Field name made lowercase.
    tipomascota = models.ForeignKey('TipoMascota', models.DO_NOTHING, db_column='tipoMascota')  # Field name made lowercase.
    sexomascota = models.CharField(db_column='sexoMascota', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alimentacionmascota = models.CharField(db_column='alimentacionMascota', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mascota'
        unique_together = (('idmascota', 'razamascota', 'tipomascota', 'propietariomascota'),)


class Persona(models.Model):
    idpersona = models.IntegerField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    usuariopersona = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioPersona')  # Field name made lowercase.
    nombrepersona = models.CharField(db_column='nombrePersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidopersona = models.CharField(db_column='apellidoPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccionpersona = models.CharField(db_column='direccionPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mailpersona = models.CharField(db_column='mailPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    generopersona = models.CharField(db_column='generoPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    edadpersona = models.IntegerField(db_column='edadPersona', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'
        unique_together = (('idpersona', 'usuariopersona'),)


class Planificacionvacuna(models.Model):
    idplanificacionvacuna = models.IntegerField(db_column='idPlanificacionVacuna', primary_key=True)  # Field name made lowercase.
    vacunamascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='vacunaMascota')  # Field name made lowercase.
    fechavacuna = models.DateTimeField(db_column='fechaVacuna')  # Field name made lowercase.
    vacunaplanificacion = models.ForeignKey('Vacuna', models.DO_NOTHING, db_column='vacunaPlanificacion')  # Field name made lowercase.
    dosisvacuna = models.DecimalField(db_column='dosisVacuna', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descripcionplanificacion = models.CharField(db_column='descripcionPlanificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicadavacuna = models.IntegerField(db_column='aplicadaVacuna', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planificacionvacuna'
        unique_together = (('idplanificacionvacuna', 'vacunamascota', 'fechavacuna', 'vacunaplanificacion'),)


class Propietario(models.Model):
    idpropietario = models.IntegerField(db_column='idPropietario', primary_key=True)  # Field name made lowercase.
    propetariopersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='propetarioPersona')  # Field name made lowercase.
    numeromascotas = models.IntegerField(db_column='numeroMascotas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propietario'
        unique_together = (('idpropietario', 'propetariopersona'),)


class Raza(models.Model):
    idraza = models.IntegerField(db_column='idRaza', primary_key=True)  # Field name made lowercase.
    razanombre = models.CharField(db_column='razaNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    razadescripcion = models.CharField(db_column='razaDescripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'raza'


class Recomendarlugar(models.Model):
    idrecomendarlugar = models.IntegerField(db_column='idRecomendarLugar', primary_key=True)  # Field name made lowercase.
    recomendacionlocal = models.ForeignKey('Local', models.DO_NOTHING, db_column='recomendacionLocal')  # Field name made lowercase.
    recomendacionpropietario = models.ForeignKey(Propietario, models.DO_NOTHING, db_column='recomendacionPropietario')  # Field name made lowercase.
    recomendacionfecha = models.DateTimeField(db_column='recomendacionFecha', blank=True, null=True)  # Field name made lowercase.
    recomnedacionlike = models.IntegerField(db_column='recomnedacionLike', blank=True, null=True)  # Field name made lowercase.
    recomendaciondescripcion = models.CharField(db_column='recomendacionDescripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recomendarlugar'
        unique_together = (('idrecomendarlugar', 'recomendacionpropietario', 'recomendacionlocal'),)


class TipoMascota(models.Model):
    idtipo = models.IntegerField(db_column='idTipo', primary_key=True)  # Field name made lowercase.
    nombretipo = models.CharField(db_column='nombreTipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciontipo = models.CharField(db_column='descripcionTipo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_mascota'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    user = models.CharField(max_length=45, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=65, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'usuario'


class Vacuna(models.Model):
    idvacuna = models.IntegerField(db_column='idVacuna', primary_key=True)  # Field name made lowercase.
    nombrevacuna = models.CharField(db_column='nombreVacuna', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fabricantevacuna = models.CharField(db_column='fabricanteVacuna', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcionvacuna = models.CharField(db_column='descripcionVacuna', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vacuna'


class Veterinario(models.Model):
    idveterinario = models.IntegerField(db_column='idVeterinario', primary_key=True)  # Field name made lowercase.
    veterinariopersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='veterinarioPersona')  # Field name made lowercase.
    veterinariolocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='veterinarioLocal')  # Field name made lowercase.
    veterinariotitulo = models.CharField(db_column='veterinarioTitulo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'veterinario'
        unique_together = (('idveterinario', 'veterinariopersona', 'veterinariolocal'),)


class VisitaVeterinario(models.Model):
    idvisita_veterinario = models.IntegerField(db_column='idVisita_Veterinario', primary_key=True)  # Field name made lowercase.
    visitamascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='visitaMascota')  # Field name made lowercase.
    visitaveterinario = models.ForeignKey(Veterinario, models.DO_NOTHING, db_column='visitaVeterinario')  # Field name made lowercase.
    fechavisita = models.DateTimeField(db_column='fechaVisita')  # Field name made lowercase.
    descripcionvisita = models.CharField(db_column='descripcionVisita', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visita_veterinario'
        unique_together = (('idvisita_veterinario', 'visitamascota', 'fechavisita', 'visitaveterinario'),)
