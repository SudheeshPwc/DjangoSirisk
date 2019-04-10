# Generated by Django 2.1.8 on 2019-04-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransRequest',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cafid', models.CharField(db_column='CAFID', max_length=100)),
                ('clientid', models.BigIntegerField(db_column='ClientID')),
                ('clientname', models.TextField(db_column='ClientName')),
                ('clienttype', models.CharField(db_column='ClientType', max_length=100)),
                ('clientsubtype', models.CharField(db_column='ClientSubType', max_length=100)),
                ('requesttype', models.IntegerField(db_column='RequestType')),
            ],
            options={
                'db_table': 'Trans_Request',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransResponse',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('requestid', models.BigIntegerField(blank=True, db_column='RequestID', null=True)),
                ('cafid', models.CharField(blank=True, db_column='CAFID', max_length=100, null=True)),
                ('clientid', models.BigIntegerField(blank=True, db_column='ClientID', null=True)),
                ('clientname', models.TextField(blank=True, db_column='ClientName', null=True)),
                ('filesharepath', models.TextField(blank=True, db_column='FileSharePath', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=10, null=True)),
                ('processedon', models.DateTimeField(blank=True, db_column='ProcessedOn', null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'Trans_Response',
                'managed': True,
            },
        ),
    ]