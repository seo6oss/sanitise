import os
import click
import pandas as pd

@click.command()
@click.option('--report_file', default='report.csv', help='The report file to use for deletion.')
@click.option('--dry-run', is_flag=True, help="Simulate deletion without actually deleting files.")
def delete_photos(report_file, dry_run):
    """Deletes photos listed in the report."""
    try:
        df = pd.read_csv(report_file)
    except FileNotFoundError:
        click.echo(f"Error: Report file not found at {report_file}")
        return

    files_to_delete = df['file_path'].tolist()

    if not files_to_delete:
        click.echo("No files to delete.")
        return

    if dry_run:
        click.echo("Dry run enabled. The following files would be deleted:")
        for file_path in files_to_delete:
            click.echo(file_path)
        return

    if click.confirm(f"Are you sure you want to delete {len(files_to_delete)} files? This action cannot be undone."):
        for file_path in files_to_delete:
            try:
                os.remove(file_path)
                click.echo(f"Deleted {file_path}")
            except OSError as e:
                click.echo(f"Error deleting {file_path}: {e}")
        click.echo("Deletion complete.")
    else:
        click.echo("Deletion cancelled.")

if __name__ == '__main__':
    delete_photos()