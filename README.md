# iCloud Photo Manager

A command-line tool to manage iCloud photos. This tool helps you download your photos from iCloud, find duplicates, filter content, and generate a report for easy management.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/seo6oss/sanitise.git
    cd sanitise
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the root of the project and add your PicPurify API key:

    ```
    PICPURIFY_API_KEY=your_api_key
    ```

## Usage

```bash
# Download photos from iCloud
python src/main.py download

# Detect duplicate photos
python src/main.py detect-duplicates

# Filter content for drug paraphernalia
python src/main.py filter-content

# Generate a CSV report
python src/main.py generate-report

# Visualize the workflow
python src/main.py visualize-workflow

# Delete photos (use --dry-run to simulate)
python src/main.py delete --dry-run
python src/main.py delete
```


