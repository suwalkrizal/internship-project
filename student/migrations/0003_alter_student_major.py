# Generated by Django 5.0.6 on 2024-05-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('IT', 'B.Sc.CSIT'), ('Engineer', 'Computer Engineer'), ('Engineer', 'Civil Engineer'), ('Engineer', 'Electronic Engineer')], max_length=20),
        ),
    ]
