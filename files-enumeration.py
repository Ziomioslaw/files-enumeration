#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import os
import math

MINIMUM_ZEROS_PADDING = 2

class Logger:
    def log(self, entry):
        print(entry)

class NonLogger:
    def log(self, entry):
        pass

class FileEnumeration:
    def __init__(self, logger = None, minimumZerosPadding = MINIMUM_ZEROS_PADDING):
        self.minimumZerosPadding = minimumZerosPadding
        self.logger = logger if logger != None else Logger()

    def convertFilesNameFromPath(self, mainPath, extension):
        if not os.path.isdir(mainPath):
            raise Exception('Path "%s" is not directory' % mainPath)

        filesFilter = os.path.join(mainPath, "*." + extension)
        self.logger.log('Seeking files for: %s' % filesFilter)

        files = glob.glob(filesFilter)
        files.sort()
        filesCount = len(files)

        if filesCount == 0:
            raise Exception('There no files in location: "%s"' % mainPath)

        numberFileNamePattern = "%0" + str(self.__countNumberOfPaddingsZeros(filesCount)) + "d." + extension
        self.__renameToNumbersNames(mainPath, files, numberFileNamePattern)
        self.logger.log("Operation finished")

    def __countNumberOfPaddingsZeros(self, numberOfElements):
        if numberOfElements < 10**self.minimumZerosPadding:
            return self.minimumZerosPadding

        return math.ceil(math.log10(numberOfElements))

    def __renameToNumbersNames(self, mainPath, files, numberFileNamePattern):
        orderNumber = 1
        for filePath in files:
            newFileName = (numberFileNamePattern) % orderNumber
            newFilePath = os.path.join(mainPath, newFileName)
            if filePath != newFilePath:
                os.rename(filePath, newFilePath)

            self.logger.log(filePath + ' -> ' + newFileName)
            orderNumber += 1

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: <directory with files> <extension files>')
        sys.exit()

    renamer = FileEnumeration(Logger())
    renamer.convertFilesNameFromPath(sys.argv[1], sys.argv[2])
