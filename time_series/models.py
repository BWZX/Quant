# Create your models here.

from pymongo import TEXT
from pymongo.operations import IndexModel
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel

from securities.models import Security


# Connect to MongoDB first. PyMODM supports all URI options supported by
# PyMongo. Make sure also to specify a database in the connection string:
connect('mongodb://localhost:27017/quant')

class TimeSeries(MongoModel):
	security = fields.ReferenceField(Security)
	metric = fields.CharField()
	tag = fields.CharField()
	start_at = fields.IntegerField()
	end_at = fields.IntegerField()
