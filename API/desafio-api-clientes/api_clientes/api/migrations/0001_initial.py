# Generated by Django 3.1.7 on 2021-04-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo_cliente', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('numero_telefone', models.CharField(max_length=15)),
            ],
        ),
    ]