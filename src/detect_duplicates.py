import os
import cv2
import click

@click.command()
@click.option('--download_dir', default='downloads', help='The directory where photos are downloaded.')
def detect_duplicates(download_dir):
    """Detects duplicate photos in the download directory."""
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(download_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(root, file)
                try:
                    image = cv2.imread(path)
                    if image is None:
                        continue
                    dhash = dhash(image)
                    if dhash in hashes:
                        duplicates.append(path)
                    else:
                        hashes[dhash] = path
                except cv2.error as e:
                    click.echo(f"Error processing {path}: {e}")

    click.echo(f"Found {len(duplicates)} duplicates.")
    # For now, just printing the duplicates
    for dup in duplicates:
        click.echo(dup)

if __name__ == '__main__':
    detect_duplicates()

def dhash(image, hash_size=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hash_size + 1, hash_size))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])