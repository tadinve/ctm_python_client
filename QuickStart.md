## Quick Start Guide

This guide is a quick start guide for you to tru ControlM_Python_Client. ControlM_Python_Client is a python library that can be used to define and run worlkflows in Control-M.

# Setup

The github repository has tutorial/example section. We will use this to quickly setup our library, test our connection to ControlM, deploy a simple "Hello World" example, and will also run it. Once we have this working, we can have define some other examples, with diffreent job types.

All examples and instructions given here are based on Unix based systems. Make suitable adjustments to run on Windows environment.

## Clone the git repo and setup virtual env

- cd working-directory # Go to a working directory.
- git clone https://github.com/tadinve/ctm_python_client.git
- cd ctm_python_client
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

## Try out the example file

There are three ways you can try out the examples files
1) **Vanilla Python**: Python script file (ctm_hello_world.py)
2) **Anaconda**: Jupyter notebook ctm_hello_world.ipynb. This file can be used in your own anaconda environment. Remember to create a virtual environment and use requirements.txt file to install required packages.
3) **Docker based Jupyter Notebook**: In examples folder in the Jupter Notebook folder, you would find a Dockerfile. this file can be used to build a docker image and run the docker environment. Example notebooks are also copied to this docker instance and can be used. Look at StartDocker.txt for instructions on starting the docker.

## Installing ctm_python_client.
As of now ctm_python_client is not availble for GA. Once ctm_python_client is available for GA, it will be available via pip install. Till then we install using **pip install git+https://github.com/controlm/ctm_python_client.git**

## Setting up your connection profile

You need to define the ctm_URI variable and the ctm_user and password to authenticate. To ensure security, password is not hardcoded, but the user is prompted to enter the password.

## Execute the Program 

Once you have configured the connection and are ready, run the whole script or notebook. 



# Next Steps

1) Once you have successfully completed the Hello World Program, try out the other examples.
2) In addition to trying out the examples, look in the tests directory of repositories. There are many individual tests for each job type. Make a copy of the tests and try them out.
3) If you need any help or have suggestions please post on the Forum, and someone will get back to you.




  
