"""
Copy translation files across to where they can be accessed.

Translations provided from crowdin are located in subdirectories,
but we need the .arb files to appear in this top level directory
to be accessed by the app.

So, simply copy them here!

"""

import os
import shutil

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


if __name__ == '__main__':

    here = os.path.abspath(os.path.dirname(__file__))

    for item in os.listdir(here):

        f = os.path.join(here, item)

        if os.path.exists(f) and os.path.isdir(item):
            copy_locale_file(f)
