import click
from models import Worker,Salary
from db import session

print("Getting the information from the database")

@click.group
def mycommands():
    pass

@click.command(short_help = 'adds a worker')
@click.argument('name')
@click.argument('age', type=int)
@click.argument('gender')
@click.argument('title')
def add_worker(name, age, gender, title):
    """Simple program that adds a new employee"""
    worker = Worker(name=name, age=age, gender=gender, title=title)
    session.add(worker)
    session.commit()
    click.echo(f'{name} has been added successfully')

@click.command()
@click.option("--status", type=bool, help="Salary status")
@click.option("--worker_id", type=int, help="Worker ID")
@click.option("--amount", type=int, help="Salary amount")
def update(status, worker_id, amount):
    """Simple program that adds the salary of workers"""
    # Check if the worker with the provided ID exists
    worker = session.query(Worker).get(worker_id)
    if worker is not None:
        salary = Salary(status=status, worker_id=worker_id, amount=amount)
        session.add(salary)
        session.commit()
        click.echo(f"Salary paid for worker: {worker.name}")
    else:
        click.echo(f"Worker with ID {worker_id} not found.")


@click.command()
@click.option("--name", help='filter the worker list by name')
@click.option("--status", type=bool, help="Filter workers by paid status (True/False)")
def list_workers(name, status):
    """List workers"""
    query = session.query(Worker)

    if name:
        # Filter by name if provided
        query = query.filter(Worker.name.ilike(f"%{name}%"))

    if status is not None:
        # Filter by paid status if provided
        query = query.join(Salary).filter(Salary.status == status)

    workers = query.all()

    if workers:
        click.echo("List of Workers:")
        for worker in workers:
            click.echo(f"{worker.id} {worker.name} {worker.age} {worker.gender} {worker.title}")
    else:
        click.echo("No workers found.")


@click.command()
@click.argument('idx', type=int, required=1)
def delete(idx):
        """deletes workers who no longer work at the site"""
        worker = session.query(Worker).get(idx)
        if worker is not None:
            session.delete(worker)
            session.commit()
            click.echo(f"Worker with ID {idx} has been deleted.")
        else:
            click.echo(f"No worker found with ID {idx}. Nothing to delete.")

mycommands.add_command(add_worker)
mycommands.add_command(update)
mycommands.add_command(list_workers)
mycommands.add_command(delete)

if __name__ == "__main__":
    mycommands()






