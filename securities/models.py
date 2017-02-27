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
    name = fields.CharField()
    code = fields.CharField()
    industry = fields.CharField()
    exchange = fields.ReferenceField(Exchange)
