import subprocess
import sys

from build_pip import copy_linux_library, build_pip, upload_pip, clean_pip

pyexe = 'python'
if sys.platform.startswith('darwin'):
    pyexe = 'python3'

copy_linux_library('../../opensees/SRC/interpreter/opensees.so')
build_pip(pyexe)
upload_pip(pyexe)
clean_pip()
