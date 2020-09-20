# import psycopg2
# conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
# cur = conn.cursor()
# with open('user_accounts.csv', 'r') as f:
#     # Notice that we don't need the `csv` module.
#     next(f) # Skip the header r
     #cur.copy_from(f, 'users', sep=',')
# = gp_conn.fetchall()

# conn.commit()
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nearby_resturantes.settings'

import django
django.setup()
import psycopg2
import psycopg2.extras
from django.contrib.gis.geos import Point
from main.models import Resturent

#from forms import SearchForm

conn = psycopg2.connect(database='my_db',
                        host='db2',
                        user='user2',
                        password='123456789',
                        cursor_factory=psycopg2.extras.RealDictCursor)

cur = conn.cursor()
query = "select * from main_raw_resturent offset 1 limit 10000;"
cur.execute(query)
result = cur.fetchall()
for data in result:
	longitude = float(data['longitude'])
	latitude = float(data['latitude'])	
	point_object = Point(longitude, latitude,srid=4326)
	p = Resturent(
	location_id = data['raw_id'],
	location = point_object,
	address = data['address'],
	categories =data['categories'],
	primaryCategories =data['primarycategories'],
	city =data['city'],
	country =data['country'],
	keys =data['keys'],
	latitude =data['latitude'],
	longitude =data['longitude'],
	name =data['name'],
	postalCode =data['postalcode'],
	province = data['province'],
	sourceURLs= data['sourceurls'],
	websites = data['websites'] if data['websites'] else ''
	)
	p.save()
