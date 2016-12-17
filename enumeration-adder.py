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

class EnumerationAdder:
    def __init__(self, logger = Logger(), minimumZerosPadding = MINIMUM_ZEROS_PADDING):
        self.minimumZerosPadding = minimumZerosPadding
        self.logger = logger

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
        for fileName in files:
            newFileName = os.path.join(mainPath, ((numberFileNamePattern) % (orderNumber)))
            if fileName != newFileName:
                os.rename(fileName, newFileName)

            self.logger.log(fileName + ' -> ' + numberFileNamePattern % (orderNumber))
            orderNumber += 1


if __name__ == '__main__':
    renamer = EnumerationAdder(Logger())

    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    # for Python < 3.0: mainPath = u"<file name>"
    renamer.convertFilesNameFromPath("/home/ziomioslaw/filestobeenumare", "txt")
