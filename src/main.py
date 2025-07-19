import click
from src.download_photos import download_photos
from src.detect_duplicates import detect_duplicates
from src.filter_content import filter_content
from src.generate_report import generate_report
from src.delete_photos import delete_photos
from src.visualize_workflow import visualize_workflow

@click.group()
def cli():
    """A command-line tool to manage iCloud photos."""
    pass

cli.add_command(download_photos)
cli.add_command(detect_duplicates)
cli.add_command(filter_content)
cli.add_command(generate_report)
cli.add_command(delete_photos)
cli.add_command(visualize_workflow)

if __name__ == '__main__':
    cli()