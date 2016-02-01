import csv


class Reader:

    def __init__(self):
        self.file = None
        self.data = []
        self.field_names = ('Description', 'Country', 'ADM1', 'ADM2', 'ADM3', 'ADM4', 'Latitude', 'Longitude', 'Name',
                          'pcode', 'fips', 'iso_alpha2', 'iso_alpha3', 'iso_num', 'stanag', 'tld')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # close the file on exit
        if self.file is not None:
            self.file.close()

    # This method will take in a file name intended to be read, and then will proceed to parse the file line by
    # line and save the data to the object.
    def file_input(self, file_name, enc=None):
        try:
            self.file = open(file_name, 'r', encoding=enc)
            return True
        except FileNotFoundError:
            print("The file could not be opened.")
            return False

    # import the data from the file that is of type csv, this will iterate the file, drop the header, and then map the
    # key-value data
    def import_csv(self):
        # ensure that the file exists and is open
        if self.file is not None:
            # using DictReader, read in the lines that are not the CSV header and append them to the mapped data var
            dr = csv.DictReader(self.file, self.field_names)
            next(dr)
            for line in dr:
                self.data.append(line)
            return True
        print("Could not import CSV, no file.")
        return False

