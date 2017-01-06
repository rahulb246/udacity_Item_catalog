#Item Catalog(Algorithms Catalog)

###About
  This is a simple web application which consists of catalog of machine learning algorithms. Authentication and authorization is provided using Google+ signin.

###How to run
  vagrant container and virtual box are needed for this project.

  Clone or download the project from this repo.

  Execute the following commands within the `vagrant/` directory.
  - `vagrant up`
  - `vagrant ssh`

  Navigate to tournament folder
  - `cd /vagrant/p6`

  (Optional) You can create your own client_secrets by following the below steps.
   - Create a new project in https://console.developers.google.com
   - Create new oauth client ID
   - set javascript origins and redirect_uris and save it
   - download the client_secrets.json file
   - client_secrets.json file which is already present can be replaced with newly generated client_secrets.json file  

  Run the following command to setup the database
  - `python database_setup.py`

  Run the following command to populate sample machine learning algortihms into database.
  - `python populate_db.py`

  Finally run the app.py.
  - `python app.py`
