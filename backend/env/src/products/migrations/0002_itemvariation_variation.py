# Generated by Django 2.2.5 on 2019-10-02 06:47

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Item')),
            ],
            options={
                'unique_together': {('item', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ItemVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=5)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to=products.models.upload_attachment_path)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
    ]