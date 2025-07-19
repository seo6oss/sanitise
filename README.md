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

# Filter content for drug paraphernalia, nudity, profanity, and other drugs
# Ensure PICPURIFY_API_KEY, REKOGNITION_API_KEY, and SIGHTENGINE_API_KEY are set in your .env file
python src/main.py filter-content

# Generate a CSV report with all flagged content
python src/main.py generate-report

# Visualize the workflow
python src/main.py visualize-workflow

# Delete photos (use --dry-run to simulate)
python src/main.py delete --dry-run
python src/main.py delete

# Advanced: Upload random garbage to iCloud to overwrite storage (conceptual)
python src/main.py upload-garbage-to-icloud --num_uploads 15 --garbage_size_mb 100

# Advanced: Re-upload cleaned photos to iCloud (conceptual)
python src/main.py reupload-cleaned-photos-to-icloud
```

## Advanced Features

### Expanded Content Filtering

This tool now incorporates advanced content moderation capabilities, leveraging conceptual integrations with industry-leading AI APIs (such as PicPurify, Amazon Rekognition, and Sightengine) to identify and flag a wider range of undesirable content:

*   **Drug Paraphernalia:** Detects items associated with drug use (e.g., bongs, pipes, syringes).
*   **Nudity:** Identifies explicit or suggestive imagery.
*   **Profanity:** Recognises offensive text within images (e.g., hate speech, slurs).
*   **Other Drugs:** Flags images containing various types of illicit substances (e.g., cannabis, cocaine, alcohol in illegal contexts).

While the API keys are placeholders for demonstration purposes, the underlying code structure is designed to be fully functional upon provision of valid API credentials.

### iCloud Storage Sanitisation (Conceptual)

To ensure maximum data privacy and recoverability control, this tool introduces a conceptual iCloud storage sanitisation mechanism, adhering to a "Department of Defense" standard for data overwriting.

**How it works (conceptually):**

1.  **Upload Random Garbage:** The `upload-garbage-to-icloud` command simulates uploading multiple large files of random, meaningless data to your iCloud storage. This process is designed to overwrite the physical storage blocks that previously held your deleted photos, making them irrecoverable. This is akin to securely wiping a hard drive.
2.  **Deletion of Garbage:** After the conceptual upload, the garbage data is conceptually deleted, freeing up space.
3.  **Re-upload Cleaned Photos:** Once your iCloud storage has been "sanitised" and any potentially recoverable "dirty" photos are overwritten, the `reupload-cleaned-photos-to-icloud` command simulates re-uploading your curated collection back to iCloud. This ensures that only your desired, clean photos reside on your cloud storage.

**Important Note:** Direct programmatic access to iCloud for arbitrary file uploads and deletions at this granular level is highly restricted by Apple for security and privacy reasons. This feature is implemented conceptually to demonstrate an advanced data security workflow and would require specific iCloud API access or manual intervention in a real-world application.

## Important Considerations

### iCloud Advanced Data Protection

If you have **iCloud Advanced Data Protection** enabled, automatic downloading and uploading of photos via third-party tools may be restricted or require additional manual authorisation steps. This is a security feature designed by Apple to protect your data. In such cases, you may need to manually download your photos from iCloud.com and upload the cleaned photos back.

### API Key Management

All API keys (PicPurify, Amazon Rekognition, Sightengine) should be stored securely as environment variables in a `.env` file and **never** committed directly to your repository. This project demonstrates the use of environment variables for secure credential management.

