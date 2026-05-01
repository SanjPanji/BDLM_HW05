import click
from .core import pipeline


@click.command()
@click.option("--count", default=1000, help="Number of prime numbers to generate")
@click.option("--seed", default=100, help="Random seed for shuffling")
def main(count: int, seed: int):
    print(pipeline(count=count, seed=seed))


if __name__ == "__main__":
    main()
