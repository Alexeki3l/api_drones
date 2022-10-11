# Introduction.

As part of a task it was decided to create this REST API service that allows customers to communicate with drones. Specific communication with the drone is outside the scope of this task.

    The service should allow:

        - Register a drone;
        - Load a drone with medication items
        - Check the medication items loaded for a given drone; 
        - Check the drones available for loading;
        - Check the battery level of a given drone;
        - Introduce a periodic task to check drone battery levels and create a history/event log for it.

# Requirements.

The tools used to solve the problem are highlighted below. 

    - Python interpretive language

    - Django: Framework

    - SQLite3

# Installation of tools and dependencies.

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
    
After installing the above files. Just open the terminal on the path where the project is and run the following command:

        python manage.py runserver

And if all goes well and open a tab in your browser and type the root address of the APIs. That would be:

        http://http://localhost:8000/api/

Perfect!.


# About the code.
## APIs:
        dron_register/: Register a new drone to the system.
        add_medications_drone/<int:pk>: Add medicines to a drone. The id of the drone must be specified.
        check_items_drone/<int:pk>: Checks if a specific drone has medical items loaded on it.
        drones_available/: Check the drones available for loading.
        drone_check_baterry/<int:pk>: Check the battery level of a given drone.
        drones/log: Displays a history of all drones with respect to their battery level and status change.

## Tests:
The unit tests performed on the system can be found in the file
<code>tests.py</code>. To test or run such tests. You must stop the application in Django if you have it running. And run in console the following command:

        python manage.py test

NOTE: 

    Before executing the above command. Go to the serializers.py file and comment the code line 66, 67 and 68.
    Why? 
    Because to create an effect where each drone changes state simultaneously without hindering the execution line of the project. I used a Python package where it creates multithreading. Which calls a function that only takes care of changing the states every so often.
    So, if it is not commented out these lines when you test you will get an error. Saying that the database is being used.

## Logs:
![](https://github.com/Alexeki3l/api_drones/blob/master/media/logs.jpg?raw=true)