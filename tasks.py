from invoke import task

@task
def build(c):
    c.run("docker-compose -p haproxy-test build")

@task
def run(c):
    c.run("docker-compose -p haproxy-test up")

@task
def query(c):
    c.run('curl -s -H "X-Something: yeah" localhost:10000')
