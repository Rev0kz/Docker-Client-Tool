import click 
import subprocess   

@click.group() 
def cli(): 
  """A client tool written in python to allow Ops engineers to work on Docker images""" 
  pass


@click.command()  
def docker_login():
      """A python function to login to DockerHub from the terminal"""
      click.echo(subprocess.call("docker login", shell=True))    


@click.command()
@click.argument('image')   
def search_image(image):  
     """A simple CLI program to search for docker images on DockerHub"""
     click.echo(subprocess.call("docker search {image}", shell=True))


@click.command()
@click.argument('image')
def push_image(image):  
    """A python function to push Docker images to DockerHub"""  
    click.echo(subprocess.call("docker push {image}", shell=True))  


@click.command()
@click.argument('image') 
def pull_image(image):  
    """A python function to pull Docker images from DockerHub"""
    click.echo(subprocess.call("docker pull {image}", shell=True))


cli.add_command(docker_login) 
cli.add_command(search_image)
cli.add_command(push_image) 
cli.add_command(pull_image)

if __name__ == '__main__': 
    cli()

