# Generated by Django 2.1.5 on 2020-06-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogcontent',
            fields=[
                ('blog_s_no', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
