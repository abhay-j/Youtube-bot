# YouTube Transcript Embedding Generator

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Fetching Transcripts](#1-fetching-transcripts)
  - [2. Cleaning Data](#2-cleaning-data)
  - [3. Generating Embeddings](#3-generating-embeddings)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The **YouTube Transcript Embedding Generator** is a Python-based project designed to fetch, clean, and generate vector embeddings from YouTube video transcripts. These embeddings can be utilized for various applications, such as building a question-answering system, semantic search, or recommendation engines.

## Features

- **Transcript Fetching:** Retrieve transcripts from YouTube videos using YouTube Data API and `youtube_transcript_api`.
- **Data Cleaning:** Process and clean raw transcript data to ensure consistency and quality.
- **Embedding Generation:** Utilize Sentence Transformers to convert cleaned transcripts into high-dimensional vector embeddings.
- **Data Storage:** Store raw, cleaned, and embedded data in JSON files for easy access and further processing.

## Prerequisites

Before setting up the project, ensure you have the following installed on your machine:

- **Python 3.7 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually comes with Python)
- **YouTube Data API Key**: Required to fetch video transcripts. [Get an API Key](https://developers.google.com/youtube/v3/getting-started)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/youtube-transcript-embedding-generator.git
   cd youtube-transcript-embedding-generator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Upgrade `pip`**

   ```bash
   python3 -m pip install --upgrade pip
   ```

4. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

   *If you don't have a `requirements.txt`, you can install the necessary packages individually:*

   ```bash
   pip install google-api-python-client youtube-transcript-api sentence-transformers
   ```

## Usage

The project consists of three main scripts:

1. **`fetch_transcripts.py`**: Fetches transcripts from YouTube videos.
2. **`dataCleaner.py`**: Cleans the raw transcript data.
3. **`generateEmbeddings.py`**: Generates vector embeddings from the cleaned data.

### 1. Fetching Transcripts

This script retrieves transcripts for a list of YouTube video IDs and saves the raw data to `transcripts.json`.

**Steps:**

1. **Prepare a List of YouTube Video IDs**

   Create a `video_ids.txt` file in the project directory with one YouTube video ID per line. Example:

   ```
   qOECpFrwv-g
   dGxuH-eaADo
   Ghpb-hZF5gs
   ```

2. **Run the Script**

   ```bash
   python3 fetch_transcripts.py
   ```

   **Output:**

   - `transcripts.json`: Contains raw transcripts fetched from YouTube.

**Note:** Ensure that your YouTube Data API key is correctly set (see [Configuration](#configuration)).

### 2. Cleaning Data

This script processes the raw transcript data to remove unnecessary characters, timestamps, and other inconsistencies, saving the cleaned data to `cleaned_data.json`.

**Run the Script:**

```bash
python3 dataCleaner.py
```

**Output:**

- `cleaned_data.json`: Contains cleaned and processed transcript data.

### 3. Generating Embeddings

This script uses Sentence Transformers to convert the cleaned transcripts into vector embeddings, storing them in `embeddings.json`.

**Run the Script:**

```bash
python3 generateEmbeddings.py
```

**Output:**

- `embeddings.json`: Contains vector embeddings for each YouTube video.

**Example Output Structure:**

```json
[
  {
    "id": "qOECpFrwv-g",
    "embedding": [0.0123, -0.0456, ..., 0.0789],
    "url": "https://www.youtube.com/watch?v=qOECpFrwv-g",
    "published_at": "2024-02-02T10:35:44Z",
    "title": "Will Perplexity AI takeover Google?"
  },
  ...
]
```

## Project Structure

```
youtube-transcript-embedding-generator/
│
├── fetch_transcripts.py       # Script to fetch YouTube transcripts
├── dataCleaner.py             # Script to clean raw transcript data
├── generateEmbeddings.py      # Script to generate embeddings using Sentence Transformers
├── transcripts.json           # Raw transcript data (auto-generated)
├── cleaned_data.json          # Cleaned transcript data (auto-generated)
├── embeddings.json            # Generated vector embeddings (auto-generated)
├── video_ids.txt              # List of YouTube video IDs to process
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

## Dependencies

The project relies on the following Python libraries:

- **google-api-python-client**: Interact with YouTube Data API.
- **youtube-transcript-api**: Fetch transcripts from YouTube videos.
- **sentence-transformers**: Generate vector embeddings from text.
- **Other Libraries**: `json`, `os`, etc. (standard libraries)

*Ensure all dependencies are installed via `pip install -r requirements.txt`.*

**Example `requirements.txt`:**

```
google-api-python-client==2.70.0
youtube-transcript-api==0.5.3
sentence-transformers==2.2.2
```

*(Replace version numbers with the latest or preferred versions.)*

## Configuration

### 1. **YouTube Data API Key**

To fetch transcripts, you need a valid YouTube Data API key.

**Steps:**

1. **Obtain an API Key:**

   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Navigate to **APIs & Services > Credentials**.
   - Click on **Create Credentials > API key**.
   - Restrict the API key to **YouTube Data API v3** for security.

2. **Set the API Key as an Environment Variable**

   It's recommended to store sensitive information like API keys as environment variables.

   ```bash
   export YOUTUBE_API_KEY='YOUR_API_KEY_HERE'
   ```

   *To make this persistent, add the above line to your shell's configuration file (e.g., `.bashrc`, `.zshrc`).*

3. **Modify `fetch_transcripts.py` to Use the API Key**

   Ensure that `fetch_transcripts.py` reads the API key from the environment variable.

   **Example Snippet:**

   ```python
   import os
   from googleapiclient.discovery import build
   from youtube_transcript_api import YouTubeTranscriptApi

   API_KEY = os.getenv('YOUTUBE_API_KEY')

   if not API_KEY:
       raise ValueError("Please set the YOUTUBE_API_KEY environment variable.")
   
   youtube = build('youtube', 'v3', developerKey=API_KEY)
   
   # Rest of your code...
   ```

## Future Work

The current project setup handles fetching, cleaning, and embedding YouTube transcripts. Future enhancements can include:

- **Vector Database Integration:**
  - Store embeddings in a vector database like Pinecone, FAISS, or Weaviate for efficient similarity searches.
  
- **Question-Answering Application:**
  - Develop a user interface where users can input queries and retrieve relevant YouTube videos based on transcript embeddings.
  
- **Automated Pipeline:**
  - Implement automation scripts to handle new video additions, periodic updates, and embedding regeneration.
  
- **Advanced Data Cleaning:**
  - Incorporate more sophisticated NLP techniques for data preprocessing, such as named entity recognition, sentiment analysis, or summarization.
  
- **Scalability:**
  - Optimize scripts for handling larger datasets, possibly leveraging multiprocessing or distributed computing.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

**Steps to Contribute:**

1. **Fork the Repository**
2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Changes and Commit**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

## License

<!-- This project is licensed under the [MIT License](LICENSE). -->

## Contact

For any questions or suggestions, please contact:

- **Name:** Abhay Joshi
- **Email:** abhayjoshi@example.com
- **LinkedIn:** [linkedin.com/in/abhayjoshi](https://www.linkedin.com/in/abhay-joshi99/)

---

*Happy Coding! 🚀*