from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Product(Model):
    __keyspace__ = "nosql"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()


data = {
    "asin": "123",
    "title": "456"
}