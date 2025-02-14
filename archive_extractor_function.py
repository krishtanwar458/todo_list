import zipfile

def extract_archive(archive_filepath, destination_filepath):
    with zipfile.ZipFile(archive_filepath, 'r') as file:
        file.extractall(destination_filepath)

if __name__ == '__main__':
    extract_archive('/Users/krishtanwar/Desktop/Python/app/Other Projects/compressed.zip', '/Users/krishtanwar/Desktop/Python/app')
