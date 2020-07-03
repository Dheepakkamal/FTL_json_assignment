# FTL_json_assignment
This application is created using Django and python.

This has the api that creates the json with the data given.

Install the required packaged for this project from requirements.txt

Setup DB and the project accordingly.

There is a custom management command for populating dummy data.

Command for populating database is,  python manage.py populateDatabase

There is a test_json.json file which has the data to be added by running the above command.

Then go to the localhost_url/UserActivityApi  You can find the json in which has User and Activity period data.

Since the database is populated using static data in the json file. We have to add new data or delete the DB.

There is another custom management command to delete i.e

python manage.py deleteDatabase

After deletion the DB will be emptied and it has to be filled with data using the populating command.


