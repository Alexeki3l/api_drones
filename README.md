# Introduction

As part of a task it was decided to create this REST API service that allows customers to communicate with drones. Specific communication with the drone is outside the scope of this task.

    The service should allow:

        - Register a drone;
        - Load a drone with medication items
        - Check the medication items loaded for a given drone; 
        - Check the drones available for loading;
        - Check the battery level of a given drone;
        - Introduce a periodic task to check drone battery levels and create a history/event log for it.

# Requirements

The tools used to solve the problem are highlighted below. 

    - Python interpretive language

    - Django: Framework

    - SQLite3

# Installation of tools and dependencies:

Python: [Download](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)

    After you have installed the Python interpreter. You must install the 'PIP' package to be able to install the python packages and tools.

pip: [Download](https://bootstrap.pypa.io/get-pip.py)
    
- Open the command prompt and navigate to the get-pip.py file. 
- Run the following command: 
`python get-pip.py`

To install Django:
    
    1. pip install Django==4.0.3
    2. pip install Pillow==9.0.0 [In order not to have problems with the images of the table medications]
    3. pip install djangorestframework [To work with the APIs in DJANGO]
    


# Configure and get up and running.:

After finishing the installation process. Configure the pgAdmin following these steps:

- Create in the pgAdmin a Database named 'api_drones'. As shown in the image. 

<p align="center">
  <img src="https://github.com/Alexeki3l/api_drones/blob/master/tools/create_db.jpg?raw=true" width="350" title="hover text">
  
</p>

- Right click on our new Database and select the 'Restore' option.

<p align="center">
  <img src="https://github.com/Alexeki3l/api_drones/blob/master/tools/restore_db.jpg?raw=true" width="350" title="hover text">
</p>

- When finished you will have the data loaded into your new Database. Next, open a terminal in the path where you have the project and type the following command:  

        python manage.py runserver