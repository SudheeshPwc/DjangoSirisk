
from django.db import models,connection
# Create your views here.
class TransRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    cafid = models.CharField(db_column='CAFID', max_length=100)  # Field name made lowercase.
    clientid = models.BigIntegerField(db_column='ClientID')  # Field name made lowercase.
    clientname = models.TextField(db_column='ClientName')  # Field name made lowercase.
    clienttype = models.CharField(db_column='ClientType', max_length=100)  # Field name made lowercase.
    clientsubtype = models.CharField(db_column='ClientSubType', max_length=100)  # Field name made lowercase.
    requesttype = models.IntegerField(db_column='RequestType')  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'Trans_Request'

class TransResponse(models.Model):
    id = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    requestid = models.BigIntegerField(db_column='RequestID', blank=True, null=True)  # Field name made lowercase.
    cafid = models.CharField(db_column='CAFID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clientid = models.BigIntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    clientname = models.TextField(db_column='ClientName', blank=True, null=True)  # Field name made lowercase.
    filesharepath = models.TextField(db_column='FileSharePath', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    processedon = models.DateTimeField(db_column='ProcessedOn', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Trans_Response'

