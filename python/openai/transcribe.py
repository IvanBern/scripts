import mimetypes
import os
import openai
import logging
import time

from dotenv import load_dotenv

import argparse


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def argumentParser():
    parser = argparse.ArgumentParser(description='Transcribes audio into the input language.')
    # Add the -file argument
    parser.add_argument('-f', '--file', metavar='PATH', type=str, help='Path to the audio file. to transcribe, '
                                                                       'in one of these formats: mp3, mp4, mpeg, '
                                                                       'mpga, m4a, wav, or webm.', required=True)
    # Add the -file argument
    parser.add_argument('-rf', '--response_format', default='text', metavar='FORMAT', type=str,
                        help='The format of the transcript '
                             'output, in one of these '
                             'options: json, text, srt, '
                             'verbose_json, or vtt.',
                        required=False)

    args = parser.parse_args()

    # Check if file exists
    file = args.file
    if not os.path.isfile(file):
        logging.warning(f"{file} does not exist.")
        exit(1)

    # Attempt to guess the file type
    type_guess = mimetypes.guess_type(file)[0]

    # Validate that the file is an audio file
    if type_guess is not None and 'audio' in type_guess:
        logging.info(f"{file} is an audio file.")
    else:
        logging.warning(f"{file} is not an audio file.")
        exit(0)
    return args


def getenv(name):
    # Get the value of the environment variable
    # Load environment variables from .env file
    load_dotenv()
    value = os.getenv(name)

    # Check if the environment variable is not found or empty
    if value is None or value.strip() == "":
        raise EnvironmentError(f"{name} environment variable is not found or is empty")
    # If the environment variable is valid, proceed with your logic
    return value


def transcribe(file, response_format):
    # Authentication to the OpenAI API
    openai.organization = getenv("OPENAI_ORGANIZATION")
    openai.api_key = getenv("OPENAI_API_KEY")
    max_file_size_kb = 25 * 1024
    # Get the size of the file in bytes
    file_size_bytes = os.path.getsize(file)
    # Convert bytes to megabytes
    file_size_mb = file_size_bytes / (1024)
    if file_size_mb <= max_file_size_kb:
        logging.info(
            f"{file} is an audio file, size {file_size_mb} KB is within the allowed limit of {max_file_size_kb} KB.")
    else:
        logging.warning(
            f"{file}is an audio file, size {file_size_mb} KB exceeds the allowed limit of {max_file_size_kb} KB.")
        exit(1)
    # Transcribe audio into the input language.
    audio_file = open(file, "rb")
    try:
        start_time = time.time()
        transcript = openai.Audio.transcribe(
            model='whisper-1',
            file=audio_file,
            response_format=response_format,
            temperature=0)
        end_time = time.time()
        response_time = end_time - start_time
        logging.info(f"Transcription took {response_time:.2f} seconds")
        return transcript
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def main():
    setup_logging()
    logging.info("Application started")
    args = argumentParser()
    file = args.file
    response_format = args.response_format
    transcript = transcribe(file, response_format)
    print(transcript)

if __name__ == '__main__':
    main()
