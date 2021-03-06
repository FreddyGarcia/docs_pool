# Generated by Django 2.2.5 on 2019-10-03 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc_registration', '0003_auto_20191001_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'área', 'verbose_name_plural': '  Áreas'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoría', 'verbose_name_plural': ' Categorías'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'documento', 'verbose_name_plural': ' Documentos'},
        ),
        migrations.AlterModelOptions(
            name='documentdetails',
            options={'verbose_name': 'Detalle del documento', 'verbose_name_plural': ' Detalle de los Documentos'},
        ),
        migrations.AlterModelOptions(
            name='mandate',
            options={'verbose_name': 'mandato', 'verbose_name_plural': 'Mandatos'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name': 'origen', 'verbose_name_plural': ' Origenes'},
        ),
        migrations.RemoveField(
            model_name='mandate',
            name='area',
        ),
        migrations.AddField(
            model_name='mandate',
            name='areas',
            field=models.ManyToManyField(to='doc_registration.Area'),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='document',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doc_registration.Source', verbose_name='Origen'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='documentdetails',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doc_registration.Document'),
        ),
        migrations.AlterField(
            model_name='documentdetails',
            name='file_name',
            field=models.CharField(max_length=300, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='documentdetails',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mandate',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doc_registration.Category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='mandate',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='mandate',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doc_registration.Document', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]
