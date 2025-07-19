import pandas as pd
import click

@click.command()
@click.option('--duplicates_file', default='duplicates.txt', help='File with list of duplicate photos.')
@click.option('--flagged_drug_paraphernalia_file', default='flagged_drug_paraphernalia.txt', help='File with list of flagged drug paraphernalia photos.')
@click.option('--flagged_nudity_file', default='flagged_nudity.txt', help='File with list of flagged nudity photos.')
@click.option('--flagged_profanity_file', default='flagged_profanity.txt', help='File with list of flagged profanity photos.')
@click.option('--flagged_other_drugs_file', default='flagged_other_drugs.txt', help='File with list of flagged other drug photos.')
@click.option('--output_file', default='report.csv', help='The name of the output CSV file.')
def generate_report(duplicates_file, flagged_drug_paraphernalia_file, flagged_nudity_file, flagged_profanity_file, flagged_other_drugs_file, output_file):
    """Generates a CSV report of duplicate and flagged photos."""
    try:
        with open(duplicates_file, 'r') as f:
            duplicates = [line.strip() for line in f]
    except FileNotFoundError:
        duplicates = []

    try:
        with open(flagged_drug_paraphernalia_file, 'r') as f:
            flagged_drug_paraphernalia = [line.strip() for line in f]
    except FileNotFoundError:
        flagged_drug_paraphernalia = []

    try:
        with open(flagged_nudity_file, 'r') as f:
            flagged_nudity = [line.strip() for line in f]
    except FileNotFoundError:
        flagged_nudity = []

    try:
        with open(flagged_profanity_file, 'r') as f:
            flagged_profanity = [line.strip() for line in f]
    except FileNotFoundError:
        flagged_profanity = []

    try:
        with open(flagged_other_drugs_file, 'r') as f:
            flagged_other_drugs = [line.strip() for line in f]
    except FileNotFoundError:
        flagged_other_drugs = []

    all_files = set(duplicates + flagged_drug_paraphernalia + flagged_nudity + flagged_profanity + flagged_other_drugs)
    data = {
        'file_path': [],
        'is_duplicate': [],
        'is_drug_paraphernalia': [],
        'is_nudity': [],
        'is_profanity': [],
        'is_other_drugs': []
    }

    for file in all_files:
        data['file_path'].append(file)
        data['is_duplicate'].append(file in duplicates)
        data['is_drug_paraphernalia'].append(file in flagged_drug_paraphernalia)
        data['is_nudity'].append(file in flagged_nudity)
        data['is_profanity'].append(file in flagged_profanity)
        data['is_other_drugs'].append(file in flagged_other_drugs)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    click.echo(f"Report generated at {output_file}")

if __name__ == '__main__':
    generate_report()