"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# <Brand id=8 name=Austin founded=1905, headquarters=Longbridge, England, discontinued=1987>


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name = 'Corvette', brand_name = 'Chevrolet').all()

# [<Model id=4 year=1953 brand=Chevrolet name=Corvette>, <Model id=5 year=1954 brand=Chevrolet name=Corvette>, <Model id=7 year=1955 brand=Chevrolet name=Corvette>, <Model id=9 year=1956 brand=Chevrolet name=Corvette>, <Model id=10 year=1957 brand=Chevrolet name=Corvette>, <Model id=12 year=1958 brand=Chevrolet name=Corvette>, <Model id=16 year=1959 brand=Chevrolet name=Corvette>, <Model id=19 year=1960 brand=Chevrolet name=Corvette>, <Model id=25 year=1961 brand=Chevrolet name=Corvette>, <Model id=27 year=1962 brand=Chevrolet name=Corvette>, <Model id=37 year=1963 brand=Chevrolet name=Corvette>, <Model id=38 year=1964 brand=Chevrolet name=Corvette>]


# Get all models that are older than 1960.
db.session.query(Model).filter(Model.year < 1960).all()

# [<Model id=1 year=1909 brand=Ford name=Model T>, <Model id=2 year=1926 brand=Chrysler name=Imperial>, <Model id=3 year=1950 brand=Hillman name=Minx Magnificent>, <Model id=4 year=1953 brand=Chevrolet name=Corvette>, <Model id=5 year=1954 brand=Chevrolet name=Corvette>, <Model id=6 year=1954 brand=Cadillac name=Fleetwood>, <Model id=7 year=1955 brand=Chevrolet name=Corvette>, <Model id=8 year=1955 brand=Ford name=Thunderbird>, <Model id=9 year=1956 brand=Chevrolet name=Corvette>, <Model id=10 year=1957 brand=Chevrolet name=Corvette>, <Model id=11 year=1957 brand=BMW name=600>, <Model id=12 year=1958 brand=Chevrolet name=Corvette>, <Model id=13 year=1958 brand=BMW name=600>, <Model id=14 year=1958 brand=Ford name=Thunderbird>, <Model id=15 year=1959 brand=Austin name=Mini>, <Model id=16 year=1959 brand=Chevrolet name=Corvette>, <Model id=17 year=1959 brand=BMW name=600>]


# Get all brands that were founded after 1920.
db.session.query(Brand).filter(Brand.founded > 1920).all()

# [<Brand id=2 name=Chrysler founded=1925, headquarters=Auburn Hills, Michigan, discontinued=None>, <Brand id=9 name=Fairthorpe founded=1954, headquarters=Chalfont St Peter, Buckinghamshire, discontinued=1976>, <Brand id=11 name=Pontiac founded=1926, headquarters=Detroit, MI, discontinued=2010>, <Brand id=14 name=Plymouth founded=1928, headquarters=Auburn Hills, Michigan, discontinued=2001>, <Brand id=15 name=Tesla founded=2003, headquarters=Palo Alto, CA, discontinued=None>]


# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# [<Model id=4 year=1953 brand=Chevrolet name=Corvette>, <Model id=5 year=1954 brand=Chevrolet name=Corvette>, <Model id=7 year=1955 brand=Chevrolet name=Corvette>, <Model id=9 year=1956 brand=Chevrolet name=Corvette>, <Model id=10 year=1957 brand=Chevrolet name=Corvette>, <Model id=12 year=1958 brand=Chevrolet name=Corvette>, <Model id=16 year=1959 brand=Chevrolet name=Corvette>, <Model id=18 year=1960 brand=Chevrolet name=Corvair>, <Model id=19 year=1960 brand=Chevrolet name=Corvette>, <Model id=25 year=1961 brand=Chevrolet name=Corvette>, <Model id=27 year=1962 brand=Chevrolet name=Corvette>, <Model id=36 year=1963 brand=Chevrolet name=Corvair 500>, <Model id=37 year=1963 brand=Chevrolet name=Corvette>, <Model id=38 year=1964 brand=Chevrolet name=Corvette>]


# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter_by(founded = 1903, discontinued = None).all()

# [<Brand id=1 name=Ford founded=1903, headquarters=Dearborn, MI, discontinued=None>, <Brand id=12 name=Buick founded=1903, headquarters=Detroit, MI, discontinued=None>]


# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# [<Brand id=1 name=Ford founded=1903, headquarters=Dearborn, MI, discontinued=None>, <Brand id=2 name=Chrysler founded=1925, headquarters=Auburn Hills, Michigan, discontinued=None>, <Brand id=3 name=Citroen founded=1919, headquarters=Saint-Ouen, France, discontinued=None>, <Brand id=4 name=Hillman founded=1907, headquarters=Ryton-on-Dunsmore, England, discontinued=1981>, <Brand id=5 name=Chevrolet founded=1911, headquarters=Detroit, Michigan, discontinued=None>, <Brand id=6 name=Cadillac founded=1902, headquarters=New York City, NY, discontinued=None>, <Brand id=7 name=BMW founded=1916, headquarters=Munich, Bavaria, Germany, discontinued=None>, <Brand id=8 name=Austin founded=1905, headquarters=Longbridge, England, discontinued=1987>, <Brand id=9 name=Fairthorpe founded=1954, headquarters=Chalfont St Peter, Buckinghamshire, discontinued=1976>, <Brand id=10 name=Studebaker founded=1852, headquarters=South Bend, Indiana, discontinued=1967>, <Brand id=11 name=Pontiac founded=1926, headquarters=Detroit, MI, discontinued=2010>, <Brand id=12 name=Buick founded=1903, headquarters=Detroit, MI, discontinued=None>, <Brand id=13 name=Rambler founded=1901, headquarters=Kenosha, Washington, discontinued=1969>, <Brand id=14 name=Plymouth founded=1928, headquarters=Auburn Hills, Michigan, discontinued=2001>]


# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# [<Model id=1 year=1909 brand=Ford name=Model T>, <Model id=2 year=1926 brand=Chrysler name=Imperial>, <Model id=3 year=1950 brand=Hillman name=Minx Magnificent>, <Model id=6 year=1954 brand=Cadillac name=Fleetwood>, <Model id=8 year=1955 brand=Ford name=Thunderbird>, <Model id=11 year=1957 brand=BMW name=600>, <Model id=13 year=1958 brand=BMW name=600>, <Model id=14 year=1958 brand=Ford name=Thunderbird>, <Model id=15 year=1959 brand=Austin name=Mini>, <Model id=17 year=1959 brand=BMW name=600>, <Model id=20 year=1960 brand=Fillmore name=Fillmore>, <Model id=21 year=1960 brand=Fairthorpe name=Rockette>, <Model id=22 year=1961 brand=Austin name=Mini Cooper>, <Model id=23 year=1961 brand=Studebaker name=Avanti>, <Model id=24 year=1961 brand=Pontiac name=Tempest>, <Model id=26 year=1962 brand=Pontiac name=Grand Prix>, <Model id=28 year=1962 brand=Studebaker name=Avanti>, <Model id=29 year=1962 brand=Buick name=Special>, <Model id=30 year=1963 brand=Austin name=Mini>, <Model id=31 year=1963 brand=Austin name=Mini Cooper S>, <Model id=32 year=1963 brand=Rambler name=Classic>, <Model id=33 year=1963 brand=Ford name=E-Series>, <Model id=34 year=1963 brand=Studebaker name=Avanti>, <Model id=35 year=1963 brand=Pontiac name=Grand Prix>, <Model id=39 year=1964 brand=Ford name=Mustang>, <Model id=40 year=1964 brand=Ford name=Galaxie>, <Model id=41 year=1964 brand=Pontiac name=GTO>, <Model id=42 year=1964 brand=Pontiac name=LeMans>, <Model id=43 year=1964 brand=Pontiac name=Bonneville>, <Model id=44 year=1964 brand=Pontiac name=Grand Prix>, <Model id=45 year=1964 brand=Plymouth name=Fury>, <Model id=46 year=1964 brand=Studebaker name=Avanti>, <Model id=47 year=1964 brand=Austin name=Mini Cooper>]


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter_by(year=year).options(db.joinedload('brand')).all()

    for model in models:
    	model_name = model.name
    	brand_name = model.brand_name
    	brand_headquarters = model.brand.headquarters
    	print model_name, brand_name, brand_headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

	brands =  db.session.query(Brand, Model).outerjoin(Model).all()

	brands_sum = {}

	for brand, model in brands:
		if model and brand.name not in brands_sum:
			brands_sum[brand.name] = [model.name]
		elif model and brand.name in brands_sum:
			brands_sum[brand.name].append(model.name)
		elif model is None:
			brands_sum[brand.name] = None
	return brands_sum

	for brand, model in brands_sum.items():
		if model:
			print brand, "--", ", ".join(models)
		else:
			print brand, "-- No models"


	# model_brands = db.session.query(Model.brand_name).group_by(Model.brand_name)


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The returned value is the 'Ford' row in the brands table, and the datatype is a query object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is similar to a middle table in that it connects two other tables. However, it's different because association tables
# have no purpose other than to connect the other two tables--there's no meaningful information in them other than the two foreign keys that connect
# those other tables. Association tables manage many to many relationships where there's no obvious way to connect the two tables.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
	"""Returns brand objects where the brand name matches the whole or part of the string passed in the function."""

	Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()


def get_models_between(start_year, end_year):
	"""Returns model objects with years starting at start_year and up to (not including) end_year. """

	Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
