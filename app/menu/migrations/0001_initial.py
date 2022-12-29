# Generated by Django 4.1.4 on 2022-12-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Имя меню')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1000, verbose_name='Сссылка на ресурс(возможны пространства имен)')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='menu.menu', verbose_name='Является элементом меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.resource', verbose_name='Родительский ресурс(пустой = верхний уровень меню)')),
            ],
        ),
    ]