# Vending Maching Tracker App
Created by Mark Masenda, Ned Hammatt, and Zach Palacios

![Image of the group during the Showcase](https://i.ibb.co/pBdRyHzy/Board-Photo.jpg)

#### Description
This project uses a combination of the pyArduino, Django, and Pipenv libraries to test and display a frontend for the database involved in creating the simulation of a Vending Machine and its use. The website has a user side and a manufacturer side, along with functionality for real-time updates to the website. 

![Image of the Frontpage](https://i.ibb.co/dJt9tztK/Homepage.png)

## Installation
#### Requirements
- python3.12
- pip

#### Steps
For all future installations of the repository, use the libraries listed:
    # Install pipenv if you haven't done so already
    
    pip install pipenv
    
    pipenv install pyArduino django pillow pyArduino

#### If that does not work:

USE: where pipenv - put it into the path environment, then set the environment variable to that

OR: pipenv lock - to update the Pipfile

### Use this to start the virtual environment:

    Make Sure to run this:
        python manage.py migrate

    Then, to start the server, run this:
        python manage.py runserver

### Demonstration Photos

![User Side](https://i.ibb.co/whJqTxgk/Userpage.png)

![Vending Machine 1 - User](https://i.ibb.co/bjyjSW0B/Vending-Machine-1.png)

![Vending Machine 2 - User](https://i.ibb.co/JZGjrRy/Vending-Machine-2.png)

![Vending Machine 3 - User](https://i.ibb.co/wFzPFZzd/Vending-Machine-3.png)


![Manufacturer Side](https://i.ibb.co/dwpY838g/Vendingpage.png)

![Vending Machine 1 - Manufacturer](https://i.ibb.co/C5TbMpDs/Vendor-1.png)

![Vending Machine 2 - Manufactuerer](https://i.ibb.co/r2Bg9jS6/Vendor-2.png)

![Vending Machine 3 - Manufactuerer](https://i.ibb.co/Nn6P30Gh/Vendor-3.png)
