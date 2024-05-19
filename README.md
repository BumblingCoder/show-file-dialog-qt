# show-file-dialog-qt
Gives KDE file selectors for Bitwig.

This python script allows for native KDE file dialogs in Bitwig, instad of the GTK dialogs.


## Requirements.
This script requires that you have PySide6 installed. The only other dependencies are the python standard library.

## Installing:
Navigate to your bitwig install directory and replace `bin/show-file-dialog-gtk3` with `show-file-dialog-qt.py`. This can be a symlink back to a chekout of this repository, or the downloaded python file.

Ensure that the script in the bin directory is named `show-file-dialog-gtk3`
Ensure the script is marked executable with `chmod +x show-file-dialog-gtk3`

This script does not currently work with the flatpak version of bitwig due to missing dependencies.

