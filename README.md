# Docker-Client-Tool   

This project shows developers how to make use of Click framework to build a client tool perform Docker operations. You can
refer to the tutorial on Pusher.   


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequsites  

Things you need to install the software and how to install them  

- [Click framework]( https://click.palletsprojects.com/en/7.x/)
- [Docker CE](https://docs.docker.com/install/)

You can install Click by using the following command:  

`pip install Click`   

Follow this [documentation](https://docs.docker.com/install/) to install Docker CE on Linux or Windows  

For example, you can then run the tool by executing the command below to search for elasticsearch images

`python client.py --search elasticsearch`    

To run the tool to pull Docker images from DockerHub, execute the following command 

`python client.py pull-image nginx`         ` 

To run the tool to push Docker images to DockerHub, execute the following command

`python client.py push-image nginx`           

## Built With  

- [Click](https://click.palletsprojects.com/en/7.x/) - A python framework to build commandline tools.
