# Generated by Django 2.2.5 on 2019-10-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190928_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliation',
            name='current',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='scientific_area',
            field=models.CharField(choices=[('agricultura', 'Agricultura'), ('artes', 'Artes'), ('biologia', 'Biología'), ('biotecnologia_agricola', 'Biotecnología Agrícola'), ('biotecnologia_ambiente', 'Biotecnología del Ambiente'), ('biotecnologia_industrial', 'Biotecnología Industrial'), ('biotecnologia_medica', 'Biotecnología Médica'), ('educacion', 'Ciencias de la Educación'), ('ciencias_politicas', 'Ciencias Políticas'), ('ciencias_salud', 'Ciencias de la Salud'), ('comunicaciones', 'Comunicaciones'), ('economia', 'Economía'), ('filosofia', 'Filosofía'), ('fisica', 'Fisica'), ('ganaderia', 'Ganadería'), ('geografia', 'Geografía'), ('historia', 'Historia y Arqueología'), ('informatica', 'Informática'), ('ing_ambiente', 'Ingenieria del Ambiente'), ('ing_civil', 'Ingenieria Civil'), ('ing_electronica', 'Ingenieria Electrónica'), ('ing_materiales', 'Ingenieria de Materiales'), ('ing_mecanica', 'Ingenieria Mecánica'), ('ing_quimica', 'Ingenieria Química'), ('lengua_literatura', 'Lengua y Literatura'), ('leyes', 'Leyes'), ('matematica', 'Matemática'), ('medician_basica', 'Medicina Básica'), ('medician_clinica', 'Medicina Clínica'), ('nano_tecnologia', 'Nano-Tecnología'), ('psicologia', 'Psicología'), ('quimica', 'Quimica'), ('religion', 'Religión'), ('sociologia', 'Sociología'), ('veterinara', 'Veterinaria'), ('otro', 'Otro')], default='', max_length=100),
        ),
    ]
