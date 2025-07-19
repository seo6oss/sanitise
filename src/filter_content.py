import os
import click
import requests

@click.command()
@click.option('--download_dir', default='downloads', help='The directory where photos are downloaded.')
@click.option('--api_key', envvar='PICPURIFY_API_KEY', required=True, help='Your PicPurify API key (set as PICPURIFY_API_KEY environment variable).')
def filter_content(download_dir, api_key):
    """Filters content using the PicPurify API."""
    flagged_files = []
    for root, _, files in os.walk(download_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'rb') as f:
                        response = requests.post(
                            'https://www.picpurify.com/analyse/1.1',
                            files={'file_image': f},
                            data={'API_KEY': api_key, 'task': 'drug_detection'}
                        )
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('drug_detection', {}).get('drug_detected'):
                            flagged_files.append(path)
                except requests.exceptions.RequestException as e:
                    click.echo(f"Error processing {path}: {e}")

    click.echo(f"Found {len(flagged_files)} files with potential drug paraphernalia.")
    # For now, just printing the flagged files
    for flagged in flagged_files:
        click.echo(flagged)

if __name__ == '__main__':
    filter_content()