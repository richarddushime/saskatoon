# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Content')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('description_fr', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('description_en', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('shared', models.BooleanField(default=b'False', help_text='Can be used in harvests outside of property', verbose_name='Shared')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Actor', verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'equipment',
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_fr', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'equipment type',
                'verbose_name_plural': 'equipment types',
            },
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('nb_required_pickers', models.IntegerField(default=3, verbose_name='Number of required pickers')),
                ('owner_present', models.BooleanField(default=b'True', verbose_name='Owner wants to be present')),
                ('owner_help', models.BooleanField(default=b'False', verbose_name='Owner wants to participate')),
                ('owner_fruit', models.BooleanField(default=b'True', verbose_name='Owner wants his share of fruits')),
                ('about', models.TextField(blank=True, max_length=1000, null=True, verbose_name='About')),
                ('equipment_reserved', models.ManyToManyField(blank=True, to='harvest.Equipment', verbose_name='Reserve equipment')),
                ('pick_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Pick leader')),
                ('pickers', models.ManyToManyField(blank=True, related_name='harvests', to='member.Person', verbose_name="Pickers' names")),
            ],
            options={
                'verbose_name': 'harvest',
                'verbose_name_plural': 'harvests',
            },
        ),
        migrations.CreateModel(
            name='HarvestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=30, verbose_name='Short name')),
                ('short_name_fr', models.CharField(max_length=30, null=True, verbose_name='Short name')),
                ('short_name_en', models.CharField(max_length=30, null=True, verbose_name='Short name')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('description_fr', models.CharField(max_length=150, null=True, verbose_name='Description')),
                ('description_en', models.CharField(max_length=150, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'harvest status',
                'verbose_name_plural': 'harvest statuses',
            },
        ),
        migrations.CreateModel(
            name='HarvestYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_in_lb', models.FloatField(verbose_name='Total yield (lb)')),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.Harvest', verbose_name='Harvest')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Actor', verbose_name='Recipient')),
            ],
            options={
                'verbose_name': 'harvest yield',
                'verbose_name_plural': 'harvest yields',
            },
        ),
        migrations.CreateModel(
            name='HistoricalHarvest',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('nb_required_pickers', models.IntegerField(default=3, verbose_name='Number of required pickers')),
                ('owner_present', models.BooleanField(default=b'True', verbose_name='Owner wants to be present')),
                ('owner_help', models.BooleanField(default=b'False', verbose_name='Owner wants to participate')),
                ('owner_fruit', models.BooleanField(default=b'True', verbose_name='Owner wants his share of fruits')),
                ('about', models.TextField(blank=True, max_length=1000, null=True, verbose_name='About')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('pick_leader', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical harvest',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProperty',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('trees_location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Trees location')),
                ('avg_nb_required_pickers', models.IntegerField(default=1, verbose_name='Required pickers on average')),
                ('public_access', models.BooleanField(default=b'False', verbose_name='Publicly accessible')),
                ('neighbor_access', models.BooleanField(default=b'False', verbose_name='Access to neighboring terrain if needed')),
                ('compost_bin', models.BooleanField(default=b'False', verbose_name='Compost bin closeby')),
                ('street_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Number')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Street')),
                ('complement', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complement')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal code')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('about', models.CharField(blank=True, max_length=1000, null=True, verbose_name='About')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('city', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='member.City')),
                ('country', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='member.Country')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('neighborhood', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='member.Neighborhood')),
                ('owner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='member.Actor')),
                ('state', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='member.State')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical property',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('trees_location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Trees location')),
                ('avg_nb_required_pickers', models.IntegerField(default=1, verbose_name='Required pickers on average')),
                ('public_access', models.BooleanField(default=b'False', verbose_name='Publicly accessible')),
                ('neighbor_access', models.BooleanField(default=b'False', verbose_name='Access to neighboring terrain if needed')),
                ('compost_bin', models.BooleanField(default=b'False', verbose_name='Compost bin closeby')),
                ('street_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Number')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Street')),
                ('complement', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complement')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal code')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('about', models.CharField(blank=True, max_length=1000, null=True, verbose_name='About')),
                ('city', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.City', verbose_name='City')),
                ('country', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Country', verbose_name='Country')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Neighborhood', verbose_name='Neighborhood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Actor', verbose_name='Owner')),
                ('state', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.State', verbose_name='State')),
            ],
            options={
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='harvest.Property')),
            ],
        ),
        migrations.CreateModel(
            name='RequestForParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picker', models.EmailField(max_length=254, verbose_name='Email of contact person')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone of contact person')),
                ('number_of_people', models.IntegerField(default=0, verbose_name='How many people are you?')),
                ('first_time_picker', models.BooleanField(default=False, verbose_name='Is this your first pick with us?')),
                ('helper_picker', models.BooleanField(default=False, verbose_name='Can you help with equipment transportation?')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('confirmation_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Confirmed on')),
                ('showed_up', models.BooleanField(default=True, verbose_name='Showed up')),
                ('is_cancelled', models.BooleanField(default=False, verbose_name='Canceled')),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.Harvest', verbose_name='Harvest')),
            ],
            options={
                'verbose_name': 'request for participation',
                'verbose_name_plural': 'requests for participation',
            },
        ),
        migrations.CreateModel(
            name='TreeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=20, verbose_name='Name')),
                ('name_fr', models.CharField(default=b'', max_length=20, null=True, verbose_name='Name')),
                ('name_en', models.CharField(default=b'', max_length=20, null=True, verbose_name='Name')),
                ('fruit_name', models.CharField(max_length=20, verbose_name='Fruit name')),
                ('fruit_name_fr', models.CharField(max_length=20, null=True, verbose_name='Fruit name')),
                ('fruit_name_en', models.CharField(max_length=20, null=True, verbose_name='Fruit name')),
                ('season_start', models.DateField(blank=True, null=True, verbose_name='Season start date')),
            ],
            options={
                'verbose_name': 'tree type',
                'verbose_name_plural': 'tree types',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='trees',
            field=models.ManyToManyField(to='harvest.TreeType', verbose_name='Fruit trees'),
        ),
        migrations.AddField(
            model_name='historicalharvest',
            name='property',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='harvest.Property'),
        ),
        migrations.AddField(
            model_name='historicalharvest',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='harvest.HarvestStatus'),
        ),
        migrations.AddField(
            model_name='harvestyield',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.TreeType', verbose_name='Tree'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='harvest.Property', verbose_name='Property'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='harvest.HarvestStatus', verbose_name='Harvest status'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='trees',
            field=models.ManyToManyField(to='harvest.TreeType', verbose_name='Trees'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='harvest.Property', verbose_name='Property'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.EquipmentType', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='comment',
            name='harvest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='harvest.Harvest', verbose_name='harvest'),
        ),
    ]
