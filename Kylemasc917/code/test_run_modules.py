# Import the module
import unixtime_converter

# Specify the path to the metafile
metafile = '/workspaces/CP1-24-midterm/Kylemasc917/data/Kylemascmetafile0111.txt'

# Get the Unix time from the metafile and print it
try:
    unix_time = unixtime_converter.get_unix_time_from_metafile(metafile)
    print(f"Unix time: {unix_time}")
except Exception as e:
    print(f"Error: {e}")
