import click 
import subprocess  
import docker

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
     click.echo(client.images.search(image))


@click.command()
@click.argument('image')
def push_image(image):  
    """A python function to push Docker images to DockerHub"""  
    click.echo(client.images.push(image)) 


@click.command()
@click.argument('image') 
def pull_image(image):  
    """A python function to pull Docker images from DockerHub"""
    click.echo(client.images.pull(image))

cli.add_command(docker_login) 
cli.add_command(search_image)
cli.add_command(push_image) 
cli.add_command(pull_image)

if __name__ == '__main__': 
    cli()

