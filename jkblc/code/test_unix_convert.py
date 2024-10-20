# test_metafile_reader.py
from unix_convert import convert_to_unix_time, read_metafile_and_extract_unix
import tempfile

def test_convert_to_unix_time():
    unix_time = convert_to_unix_time("2024-10-20 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert unix_time == 1729416000  # Expected Unix timestamp

def test_read_metafile_and_extract_unix():
    # Create a temporary metafile for testing
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write("2024-10-20 12:00:00\n2024-10-21 13:30:00\n")
        temp_file_path = temp_file.name

    unix_times = list(read_metafile_and_extract_unix(temp_file_path))
    assert unix_times == [1729416000, 1729507800]
