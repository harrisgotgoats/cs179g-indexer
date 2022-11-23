# Generated by Django 3.2.9 on 2021-12-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('availability', models.TextField(blank=True, null=True)),
                ('upc', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'output',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OutputTrimmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'output_trimmed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('product_id', models.TextField(blank=True, null=True)),
                ('selected_product_id', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('seller', models.TextField(blank=True, null=True)),
                ('review_count', models.TextField(blank=True, null=True)),
                ('rating', models.TextField(blank=True, null=True)),
                ('currency', models.TextField(blank=True, null=True)),
                ('sale_price', models.TextField(blank=True, null=True)),
                ('regular_price', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('available_in_store', models.TextField(blank=True, null=True)),
                ('available_online', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('attributes', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('size', models.TextField(blank=True, null=True)),
                ('is_sponsored', models.TextField(blank=True, null=True)),
                ('product_information', models.TextField(blank=True, null=True)),
                ('image_urls', models.TextField(blank=True, null=True)),
                ('variations', models.TextField(blank=True, null=True)),
                ('product_variants', models.TextField(blank=True, null=True)),
                ('rating_histogram', models.TextField(blank=True, null=True)),
                ('store_id', models.TextField(blank=True, null=True)),
                ('store_location', models.TextField(blank=True, null=True)),
                ('store_telephone', models.TextField(blank=True, null=True)),
                ('store_address', models.TextField(blank=True, null=True)),
                ('search_input', models.TextField(blank=True, null=True)),
                ('search_zipcode', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'target',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Totaloutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'totaloutput',
                'managed': False,
            },
        ),
    ]
