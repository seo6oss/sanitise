import pandas as pd
import click

@click.command()
@click.option('--duplicates_file', default='duplicates.txt', help='File with list of duplicate photos.')
@click.option('--content_file', default='content.txt', help='File with list of flagged content.')
@click.option('--output_file', default='report.csv', help='The name of the output CSV file.')
def generate_report(duplicates_file, content_file, output_file):
    """Generates a CSV report of duplicate and flagged photos."""
    try:
        with open(duplicates_file, 'r') as f:
            duplicates = [line.strip() for line in f]
    except FileNotFoundError:
        duplicates = []

    try:
        with open(content_file, 'r') as f:
            flagged_content = [line.strip() for line in f]
    except FileNotFoundError:
        flagged_content = []

    all_files = set(duplicates + flagged_content)
    data = {
        'file_path': [],
        'is_duplicate': [],
        'is_paraphernalia': []
    }

    for file in all_files:
        data['file_path'].append(file)
        data['is_duplicate'].append(file in duplicates)
        data['is_paraphernalia'].append(file in flagged_content)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    click.echo(f"Report generated at {output_file}")

if __name__ == '__main__':
    generate_report()