# Generated by Django 4.0.2 on 2022-05-24 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCondominio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casa',
            name='agua',
        ),
        migrations.RemoveField(
            model_name='casa',
            name='id_casa',
        ),
        migrations.RemoveField(
            model_name='casa',
            name='luz',
        ),
        migrations.RemoveField(
            model_name='casa',
            name='saldo',
        ),
        migrations.RemoveField(
            model_name='condominio',
            name='id_condominio',
        ),
        migrations.RemoveField(
            model_name='condominio',
            name='mantencion',
        ),
        migrations.RemoveField(
            model_name='condominio',
            name='num_casas',
        ),
        migrations.RemoveField(
            model_name='condominio',
            name='num_casas_ocupadas',
        ),
        migrations.RemoveField(
            model_name='espacios_comunes',
            name='aforo',
        ),
        migrations.RemoveField(
            model_name='espacios_comunes',
            name='costo_arriendo',
        ),
        migrations.RemoveField(
            model_name='espacios_comunes',
            name='id_condominio',
        ),
        migrations.RemoveField(
            model_name='espacios_comunes',
            name='id_espacio',
        ),
        migrations.RemoveField(
            model_name='espacios_comunes',
            name='mantencion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='casa',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
    ]
