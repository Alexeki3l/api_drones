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

    - PostgreSQL : Relational database management system.

    - pgAdmin : Tool to manage and administer PostgreSQL.

## Installation of tools and dependencies:

Python: [Download](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)

    After you have installed the Python interpreter. You must install the 'PIP' package to be able to install the python packages and tools.

pip: [Download](https://bootstrap.pypa.io/get-pip.py)
    
- Abra el símbolo del sistema y navegue hasta el archivo get-pip.py. 
- Ejecute el siguiente comando:  
`python get-pip.py`

To install Django:
    
    1. pip install Django==4.0.3
    2. pip install Pillow==9.0.0 [In order not to have problems with the images of the table medications]
    3. pip install djangorestframework [To work with the APIs in DJANGO]
    4. pip install psycopg2==2.9.3 [To connect Django with PostgreSQL. This is the version I use.]

PostgreSQL: [Download](https://drive.google.com/file/d/1-X7NaErDjU8fNLx56Cmass9j-7jmPmBO/view?usp=sharing)

And finally. Install pgAdmin optionally as a DB manager.

PgAdmin: [Download](https://drive.google.com/file/d/1-D3_40XOkO0V7kw_A0C02t-eulUJyMpU/view?usp=sharing)


# Configure and get up and running.:

After finishing the installation process. Configure the pgAdmin following these steps:

- Create in the pgAdmin a Database named 'api_drones'. As shown in the image. 

<p align="center">
  <img src="https://github.com/Alexeki3l/api_drones/blob/master/tools/create_db.jpg?raw=true" width="350" title="hover text">
  
</p>

- Right click on our new Database and select the 'Restore' option.

<p align="center">
  <img src="https://drive.google.com/file/d/1NoaaiCgsHkM2xTi9nKXNwom2eMOwEHRV/view" width="350" title="hover text">
</p>

- When finished you will have the data loaded into your new Database. Next, open a terminal in the path where you have the project and type the following command:  

        python manage.py runserver