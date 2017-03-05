# Create your models here.

from pymongo import TEXT
from pymongo.operations import IndexModel
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel


# Connect to MongoDB first. PyMODM supports all URI options supported by
# PyMongo. Make sure also to specify a database in the connection string:
connect('mongodb://localhost:27017/quant')

class Exchange(MongoModel):
    name = fields.CharField()

class Security(MongoModel):
    exchange = fields.ReferenceField(Exchange)
    name = fields.CharField()
    code = fields.CharField()
    industry = fields.CharField()

class PriceEvent(MongoModel):
	security = fields.ReferenceField(Security)
	event_type = fields.IntegerField()
	change_at = fields.IntegerField()
	price_before = fields.FloatField()
	price_after = fields.FloatField()
	ratio = fields.FloatField()

