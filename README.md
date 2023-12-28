# Installation

This application was developed using the XAMPP stack.

### Prerequisites

Ensure you have the following installed:

- **XAMPP**: Set up XAMPP on your system to manage Apache, MySQL, and PHP.
- **Python**: Ensure Python is installed on your machine.

### Database Setup

1. **Import SQL File**: Locate the SQL file included in the base directory and import it into PHPMyAdmin. This file contains necessary data for the application, excluding hardware-specific details.

### Setting Up the Application

Follow these steps to set up the application:

1. **Clone the Project**:
    ```
    git clone https://github.com/ReinerYaeger/MpWsn
    ```
    Clone the project into your desired directory.

2. **Create a Virtual Environment**:
    ```
    python -m venv venv
    ```
    This will create a virtual environment for isolating the project's dependencies.

3. **Install Requirements**:
    ```
    pip install -r requirements.txt
    ```
    This command will install all the required Python packages specified in the `requirements.txt` file.

### Running the Application

After completing the installation steps, you're ready to run the application. Make sure XAMPP is running to support the application's database functionalities.

### Hardware Files

If you possess the required hardware, find the necessary files for the Arduino and Raspberry Pi 4 in this directory:

### Running the Server

To run the server, execute the `server.py` file located in the `/iot/pi_files` directory using the following command:


### Performing Analytics

For performing analytics, run the `analyzer.py` file in the `/iot/pi_files` directory using the command:


### Running the Application

After completing the installation steps, you're ready to run the application. Make sure XAMPP is running to support the application's database functionalities.
