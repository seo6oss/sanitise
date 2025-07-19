import click
import os
from icloud_photos_downloader import IcloudPhotosDownloader

@click.command()
@click.option('--apple_id', prompt='Your Apple ID', help='Your Apple ID for iCloud.')
@click.option('--download_dir', default='downloads', help='The directory to download photos to. Defaults to a 'downloads' folder in the current directory.')
def download_photos(apple_id, download_dir):
    """Downloads photos from iCloud."""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    icloud = IcloudPhotosDownloader(apple_id, None, download_dir)
    icloud.download_photos()

if __name__ == '__main__':
    download_photos()