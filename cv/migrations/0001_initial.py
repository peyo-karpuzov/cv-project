# Generated by Django 2.2.1 on 2019-05-23 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=20)),
                ('name_last', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CVGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('pic', models.URLField()),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Non-disclose')], max_length=1)),
                ('applicant_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.ApplicantUser')),
            ],
        ),
        migrations.CreateModel(
            name='MotivationLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('applicant_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.ApplicantUser')),
                ('cv_general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CVGeneral')),
                ('job_offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emp.JobOffer')),
            ],
        ),
        migrations.CreateModel(
            name='CVWorkPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('cv_general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CVGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='CVLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('writing', models.CharField(choices=[('A1', "Beginner' level"), ('A2', 'Lower Intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], max_length=2)),
                ('speaking', models.CharField(choices=[('A1', "Beginner' level"), ('A2', 'Lower Intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], max_length=2)),
                ('reading', models.CharField(choices=[('A1', "Beginner' level"), ('A2', 'Lower Intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], max_length=2)),
                ('listening', models.CharField(choices=[('A1', "Beginner' level"), ('A2', 'Lower Intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], max_length=2)),
                ('cv_general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CVGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='CVEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('N', 'No education'), ('P', 'Primary education'), ('S', 'Secondary education'), ('HB', 'Higher education: BA'), ('HM', 'Higher education: MA'), ('PhD', 'Doctoral degree')], max_length=3)),
                ('institution', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('cv_general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CVGeneral')),
            ],
        ),
    ]
