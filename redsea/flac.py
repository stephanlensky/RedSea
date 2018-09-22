import os
import subprocess


def recompress_flac(flac_file, compression_level):
    '''
    Accepts flac file path and recompresses it
    to the specified compression level.

    Warning: This will overwrite the original flac!
    '''

    # Check if flac is available
    try:
        subprocess.check_output('flac')
    except Exception as e:
        print('Error: The flac binary does not appear to be installed on your system.')
        raise e

    subprocess.call(['flac', '-' + str(compression_level), '-f', '{}'.format(os.path.normpath(flac_file))])