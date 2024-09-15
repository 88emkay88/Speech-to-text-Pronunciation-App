# Speech-to-text-Pronunciation-App
# Speech-to-Text API Project

This project uses Google's Speech-to-Text API to transcribe audio files into text.

## Setup Instructions

1. **Create a Google Cloud Project and Enable Speech-to-Text API**
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Enable the Speech-to-Text API.
   - Create a service account and download the JSON key file.

2. **Set up the `.env` file**
   - In the root of this project, create a file named `.env`.
   - Add the following line, replacing `<path_to_your_json>` with the actual path to the JSON key file:
     ```plaintext
     GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_json>
     ```

3. **Install Dependencies**
   - Run the following command to install the necessary Python packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application**
   - Once set up, you can run the Python scripts as needed.

