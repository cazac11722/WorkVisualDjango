from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_projecttask_end_time_projecttask_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttask',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
