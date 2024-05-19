#!/usr/bin/env python3

from PySide6 import QtWidgets, QtCore, QtGui
import argparse


def output_filename(output_file, filename):
    if output_file is not None:
        f = open(output_file, 'w')
        f.write(filename)
    else:
        print(filename)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    parser = argparse.ArgumentParser()
    parser.add_argument('--title')
#     Attach would be nice to have sometime, but it isn't super important.
    parser.add_argument('--attach')
    parser.add_argument('--directory', action='store_true')
    parser.add_argument('--save', action='store_true')
#     unused, in gtk it is a string 'Open', 'Save', 'Select Folder' or 'Create Folder'
    parser.add_argument('--accept')
#     Like attach, cancel is for window management and we can probably skip it.
    parser.add_argument('--cancel')
    parser.add_argument('--multiple', action='store_true')
    parser.add_argument('--confirm-overwrite',
                        action='store_true', dest='confirm_overwirte')
    parser.add_argument('--filename')
    parser.add_argument('--initial-directory', dest='initial_directory')
    parser.add_argument('--file-filter', action='append',
                        dest='file_filter', nargs='*')
#     place is trying to add custom locations to the quick menu on the left. Currently not supported
    parser.add_argument('--place', action='append')
    parser.add_argument('--output')

    args = parser.parse_args()

    filter = [f'{f[0]} ({f[1].replace(
        '|', ' ')})' for f in args.file_filter] if args.file_filter is not None else []
    filter = ';;'.join(filter)

    if args.directory:
        output_filename(args.output, QtWidgets.QFileDialog.getExistingDirectory(
            None, args.title, args.initial_directory))
        exit(0)
    if args.save:
        output_filename(args.output, QtWidgets.QFileDialog.getSaveFileName(
            None, args.title, args.initial_directory if args.filename is None else args.filename, filter)[0])
        exit(0)
    if args.multiple:
        output_filename(args.output, QtWidgets.QFileDialog.getOpenFileNames(
            None, args.title, args.initial_directory, filter)[0])
        exit(0)
    else:
        output_filename(args.output, QtWidgets.QFileDialog.getOpenFileName(
            None, args.title, args.initial_directory, filter)[0])
        exit(0)
