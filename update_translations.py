"""
Copy translation files across to where they can be accessed.

Translations provided from crowdin are located in subdirectories,
but we need the .arb files to appear in this top level directory
to be accessed by the app.

So, simply copy them here!

"""

import os
import shutil
import re
import json

def process_locale_file(filename):
    """
    Process a locale file after copying

    - Ensure the 'locale' matches
    """

    # Extract the locale name from the filename
    f = os.path.basename(filename)
    locale = re.search(r"^app\_(\w+)\.arb$", f).groups()[0]

    with open(filename, 'r') as input_file:

        lines = input_file.readlines()

    with open(filename, 'w') as output_file:
        # Using JSON processing would be simpler here,
        # but it does not preserve unicode data!
        for line in lines:
            if '@@locale' in line:
                line = f'    "@@locale": "{locale}",\n'

            output_file.write(line)


def copy_locale_file(path):
    """
    Locate and copy the locale file from the provided directory
    """

    here = os.path.abspath(os.path.dirname(__file__))

    for f in os.listdir(path):

        src = os.path.join(path, f)
        dst = os.path.join(here, f)

        if os.path.exists(src) and os.path.isfile(src) and f.endswith('.arb'):

            print(f"Copying file '{f}'")
            shutil.copy(src, dst)

            process_locale_file(dst)


if __name__ == '__main__':

    here = os.path.abspath(os.path.dirname(__file__))

    for item in os.listdir(here):

        f = os.path.join(here, item)

        if os.path.exists(f) and os.path.isdir(item):
            copy_locale_file(f)
