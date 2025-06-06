# Generated by Django 5.1.6 on 2025-03-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eyecraft', '0042_delete_contactlens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lensproduct',
            name='productCategory',
            field=models.CharField(choices=[('EYE_GLASSES', 'Eye Glasses'), ('POWER_GLASSES', 'Power Glasses'), ('SUN_GLASSES', 'Sun Glasses'), ('COMPUTER_GLASSES', 'Computer Glasses'), ('READING_GLASSES', 'Reading Glasses'), ('CONTACT_LENSES', 'Contact Lenses'), ('ACCESSORIES', 'Accessories'), ('k_EYE_GLASSES', 'K_Eye Glasses'), ('k_SUN_GLASSES', 'k_Sun Glasses')], default='EYE_GLASSES', max_length=50),
        ),
    ]
