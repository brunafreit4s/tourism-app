# Generated by Django 4.2.3 on 2023-07-20 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('core', '0004_pontoturistico_avaliacoes_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
            preserve_default=False,
        ),
    ]