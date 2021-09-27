# car hiring system
## content.

* Create DB
* How to run app
* Api Documentaion


Create DB
=====================================
1. clone git repo https://github.com/sfwat/car_hiring.git
2. In mysql shell run source car_hiring/car_hiring.sql

How to run
=====================================
1. Create and activate Virual enviroment **$virtualenv venv**    **source/venv/bin/activate**
2. Move to car_hiring dir and install packages from requirments file $ pip install -r requirments.txt
3. Run the run.py file


Apis
=====================================
## add customer [/customer] [POST]

+ Request

  + Body
    
             {
                    "username": "test",
                    "email": "test@test.com",
                    "phone": "123211456"
             }
  + Response
  
             {
                "message": "successfully created"            
             }
  + status code 201

## add customer [/customer/<id>] [GET]

+ Request

  + Response
  
             {
               "customer": [
                    2,
                    "test",
                    "test@test.com",
                    "123211456"
                ] 
             }


  + status code 200

## remove customer [/customer/<id>] [DELETE]

+ Request

  + Response
  
             {
                "message": "successfully deleted"            
             }
  + status code 200
