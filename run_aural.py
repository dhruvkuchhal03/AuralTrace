from aural import Aural
from aural.logic.recognizer.file_recognizer import FileRecognizer
import pprint


def fingerprint_music(atr):
    # Step 4: Prompt user for the directory containing the music to be fingerprinted
    music_directory = input(
        "Enter the directory that contains the music to be fingerprinted:\n")

    # Step 5: Fingerprint the directory
    atr.fingerprint_directory(music_directory, [".mp3"], 3)
    print("Fingerprinting Done!\n")

    # Step 6: Print the number of fingerprints in the database
    # print(atr.db.get_num_fingerprints())


def recognize_song(atr):
    # Step 8: Prompt user for the directory containing the audio file to be recognized
    test_file = input(
        "Enter the file path of the audio file to be recognized:\n")

    # Step 9: Recognize the song
    song = atr.recognize(FileRecognizer, test_file)

    # Format and print the result
    print("\nRecognition Results:")
    print(f"Total Time: {song['total_time']} seconds")
    print(f"Fingerprint Time: {song['fingerprint_time']} seconds")
    print(f"Query Time: {song['query_time']} seconds")
    print(f"Align Time: {song['align_time']} seconds")
    print("Results:")
    for result in song['results']:
        print(f"  Song ID: {result['song_id']}")
        print(f"  Song Name: {result['song_name'].decode('utf-8')}")
        print(f"  Input Total Hashes: {result['input_total_hashes']}")
        print(f"  Fingerprinted Hashes in DB: {
              result['fingerprinted_hashes_in_db']}")
        print(f"  Hashes Matched in Input: {
              result['hashes_matched_in_input']}")
        print(f"  Input Confidence: {result['input_confidence']}")
        print(f"  Fingerprinted Confidence: {
              result['fingerprinted_confidence']}")
        print(f"  Offset: {result['offset']}")
        print(f"  Offset Seconds: {result['offset_seconds']}")
        print(f"  File SHA1: {result['file_sha1'].decode('utf-8')}\n")


def main():
    # Step 2: Configure database connection
    config = {
        "database": {
            "host": "127.0.0.1",
            "user": "root",
            "password": "Dhruv@2003",
            "database": "aural",
        }
    }

    # Step 3: Initialize Aural
    atr = Aural(config)

    # Ask the user whether they want to fingerprint music or go straight to recognition
    choice = input(
        "Do you want to fingerprint a directory of music files? (yes/no):\n").strip().lower()

    if choice == 'yes':
        fingerprint_music(atr)

    recognize_song(atr)


if __name__ == "__main__":
    main()
# api call wit arg
