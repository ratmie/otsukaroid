#!C:\Users\takeg\AppData\Local\Programs\Python\Python37\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'future==0.17.0','console_scripts','pasteurize'
__requires__ = 'future==0.17.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('future==0.17.0', 'console_scripts', 'pasteurize')()
    )
