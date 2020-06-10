# Generated by Django 3.0.3 on 2020-06-10 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0008_auto_20200610_0806'),
        ('metas', '0009_auto_20200610_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationshipsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.ContentsModel')),
                ('meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metas.MetasModel')),
            ],
            options={
                'verbose_name': '关系表',
                'verbose_name_plural': '关系表',
                'db_table': 'marilyn_relationships',
            },
        ),
    ]