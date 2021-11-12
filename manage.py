from flask.cli import FlaskGroup
from app import create_app, db
from flask import current_app
import os

from app.models.users import Users
from app.models.products import Products

cli = FlaskGroup(create_app=create_app)

user_json = [
  {
    "name": "Apoorv Goyal",
    "email": "apoorv.goyal@whitehatjr.com",
    "password": "hello_apoorv",
    "contact": "+91 9910402957"
  },
  {
    "name": "Saurabh Aswani",
    "email": "saurabh.aswani@whitehatjr.com",
    "password": "hello_saurabh",
    "contact": "+91 8844669900"
  },
  {
    "name": "Vishal Gaddam",
    "email": "vishal.gaddam@whitehatjr.com",
    "password": "hello_vishal",
    "contact": "+91 3355779911"
  },
  {
    "name": "Preeti Sharma",
    "email": "preeti.sharma@whitehatjr.com",
    "password": "hello_preeti",
    "contact": "+91 1133557799"
  },
  {
    "name": "Abhijeet Holkar",
    "email": "abhijeet.holkar@whitehatjr.com",
    "password": "hello_abhijeet",
    "contact": "+91 4455667788"
  }
]

product_json = [
  {
    "name": "Sergeant Rodog AI",
    "image": "/static/images/toy1.png",
    "rating": "5",
    "marked_price": "99.99",
    "selling_price": "94.99"
  },
  {
    "name": "Captain Underpants AI",
    "image": "/static/images/toy2.png",
    "rating": "5",
    "marked_price": "99.99",
    "selling_price": "94.99"
  },
  {
    "name": "RC Race Car - Mercedes",
    "image": "/static/images/toy3.png",
    "rating": "5",
    "marked_price": "49.99",
    "selling_price": "39.99"
  },
  {
    "name": "Hoblox - Build Houses",
    "image": "/static/images/toy4.png",
    "rating": "4",
    "marked_price": "29.99",
    "selling_price": "24.99"
  },
  {
    "name": "Kidzz Car",
    "image": "/static/images/toy5.png",
    "rating": "3",
    "marked_price": "19.99",
    "selling_price": "18.99"
  },
  {
    "name": "Toy Plain - Hoblox Edition",
    "image": "/static/images/toy6.png",
    "rating": "5",
    "marked_price": "19.99",
    "selling_price": "18.99"
  },
  {
    "name": "Crained - Hoblox Edition",
    "image": "/static/images/toy7.png",
    "rating": "5",
    "marked_price": "19.99",
    "selling_price": "16.99"
  },
  {
    "name": "Dumber - Hoblox Edition",
    "image": "/static/images/toy8.png",
    "rating": "5",
    "marked_price": "19.99",
    "selling_price": "17.99"
  },
  {
    "name": "Super Train - Hoblox Edition",
    "image": "/static/images/toy9.png",
    "rating": "4",
    "marked_price": "29.99",
    "selling_price": "24.99"
  },
  {
    "name": "Rubber Fish",
    "image": "/static/images/toy10.png",
    "rating": "5",
    "marked_price": "14.99",
    "selling_price": "12.99"
  },
  {
    "name": "Roller Bunny (Pink)",
    "image": "/static/images/toy11.png",
    "rating": "4",
    "marked_price": "9.99",
    "selling_price": "9.49"
  }
]

def recreate_db():
  db.drop_all()
  db.create_all()
  db.session.commit()

def seeder():
  for user in user_json:
    Users.create(user.get("name"), user.get("email"), user.get("password"), user.get("contact"))

  for product in product_json:
    Products.create(product.get("name"), product.get("image"), product.get("rating"), product.get("marked_price"), product.get("selling_price"))

@cli.command()
def rsd():
  # if current_app.config.get('ENV') not in ('development', 'test', 'testing'):
  #   print("ERROR: seed-db only allowed in development and testing env.")
  #   return
  recreate_db()
  seeder()

if __name__ == '__main__':
  cli()
