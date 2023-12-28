
# Installation

Note is application was developed using the XAMP stack

There is a sql file included in the base directory you can simply import it in PHP myadmin this is just so you can have the data include you do not have the hardware.


Clone the project is desired directory
`
git clone 
`

Create a virtual env
`
python -m venv venv
`

Install the requirements
`
    pip install -r requirements.txt
`

run the django web application
`
 python .\manage.py runserver
`

If you do have the hardware the files for the Arduino and the Raspberry Pi 4 is in this directory  
`
/iot/pi_files
`

To run the server simply run the server.py file in the /iot/pi_files directory 
`
python /iot/pi_files/server.py
`

To perform the analytics run the analyzer.py file in the /iot/pi_files directory 
`
python /iot/pi_files/analyzer.py
`





