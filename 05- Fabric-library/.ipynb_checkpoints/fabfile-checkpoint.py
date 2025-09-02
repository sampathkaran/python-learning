from fabric import task

@task

def hello(c):
    c.run("hostname")