# Generated by Django 2.0.6 on 2018-06-30 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20180627_0913'),
        ('vacancies', '0002_auto_20180628_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='employment_patterns',
            new_name='employment_type',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='headhunter',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='vacancy_id',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='hh_payment_type',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='request_id',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='topic',
        ),
        migrations.AddField(
            model_name='publication',
            name='vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='publications', to='vacancies.Vacancy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='request',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='vacancies', to='requests.Request'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='work_conditions',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]