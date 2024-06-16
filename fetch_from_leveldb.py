import os
import plyvel
import json

# Path to Chrome's LevelDB storage directory
path_to_leveldb = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Local Storage/leveldb')

def parse_chrome_storage_value(value):
    # This function parses the LevelDB value according to Chrome's storage format
    try:
        return value.decode('utf-8')
    except UnicodeDecodeError:
        return value

def fetch_values():
    db = plyvel.DB(path_to_leveldb, compression=None)
    for key, value in db:
        parsed_value = parse_chrome_storage_value(value)
        try:
            json_value = json.loads(parsed_value)
        except json.JSONDecodeError:
            json_value = parsed_value
        print(f"Key: {key.decode('utf-8')}, Value: {json.dumps(json_value, indent=2)}")
    db.close()

if __name__ == '__main__':
    fetch_values()

