# Generated by Django 2.2.6 on 2020-03-10 07:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('persona_id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, null=True, unique=True)),
                ('edad', models.CharField(max_length=3, null=True)),
                ('fechaNacimiento', models.DateField(null=True)),
                ('direccion', models.TextField(default='sin direccion', max_length=200)),
                ('telefono', models.CharField(max_length=13)),
                ('foto', models.ImageField(null=True, upload_to='gallery')),
                ('isDecano', models.BooleanField(default=False)),
                ('isDocente', models.BooleanField(default=False)),
                ('isEstudiante', models.BooleanField(default=True)),
                ('isAbogado', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('archivo_id', models.AutoField(primary_key=True, serialize=False)),
                ('archivo', models.FileField(upload_to='archivos')),
                ('informePeticionario', models.FileField(null=True, upload_to='informes')),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('carrera_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('ciclo_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('docente_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Carrera')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MallaCurricular',
            fields=[
                ('mallaCurricular_id', models.AutoField(primary_key=True, serialize=False)),
                ('archivo', models.FileField(upload_to='mallas')),
                ('anio', models.CharField(max_length=5)),
                ('estado', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('materia_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('creditos', models.CharField(max_length=10)),
                ('codigo', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=10)),
                ('obligatoria', models.BooleanField(default=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='PeriodoAcademico',
            fields=[
                ('periodoAcademico_id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('mallaCurricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.MallaCurricular')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(choices=[('decano', 'Decano'), ('abogado', 'Abogado'), ('docente', 'Docente'), ('solicitante', 'Solicitante')], default='Solicitante', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('tramite_id', models.AutoField(primary_key=True, serialize=False)),
                ('registro', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=False)),
                ('tipo', models.CharField(choices=[('Homologacion', 'Homologacion')], max_length=200)),
                ('archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Archivo')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Carrera')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Docente')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Silabo',
            fields=[
                ('Silabo_id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True)),
                ('archivo', models.FileField(upload_to='silabos')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Docente')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Materia')),
                ('periodoAcademico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.PeriodoAcademico')),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('seguimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('revSolicitud', models.BooleanField(default=False)),
                ('revSellos', models.BooleanField(default=False)),
                ('asigDocente', models.BooleanField(default=False)),
                ('revDocumentacion', models.BooleanField(default=False)),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Tramite')),
            ],
        ),
        migrations.AddField(
            model_name='ciclo',
            name='mallaCurricular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.MallaCurricular'),
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Rol'),
        ),
        migrations.AddField(
            model_name='persona',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
