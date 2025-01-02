
from django.db import migrations, models
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat, Replace


from migrations_app.models import Cake


def alter_names_of_sauces(apps,schema_editor):
    '''A function to add ' Sauce' to end of all sauces in Cake objects.'''

    Cake = apps.get_model('migrations_app', 'Cake') 

    Cake.objects.annotate(
        new_sauce_name = Concat(
            F('sauce'), Value(' Sauce'), output_field=CharField()
        )
    ).update(sauce = F('new_sauce_name'))


def reverse_alter_names_of_sauces(apps,schema_editor):
    '''Reverse of above function.'''

    Cake = apps.get_model('migrations_app', 'Cake')

    Cake.objects.update(
        sauce=Replace('sauce', text=Value(' Sauce'), replacement=Value(''))
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('migrations_app', '0001_initial'), # just one before migration.
    ]

    operations = [
        migrations.RunPython(
            alter_names_of_sauces,
            reverse_code=reverse_alter_names_of_sauces,
        ),
    ]