# Generated by Django 3.0.3 on 2020-06-09 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0002_auto_20200609_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metasmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metas.MetasModel', verbose_name='上级分类'),
        ),
    ]
