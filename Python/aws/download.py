#
# Author: Rohtash Lakra
#
import csv
import json
from io import BytesIO, TextIOWrapper
from io import StringIO

import boto3
import pandas as pd


class S3Client:

    # read as csv
    def readCsvFile(self, csv_bytes):
        print("readCsvFile")
        csv_bytes.seek(0)
        reader = csv.DictReader(csv_bytes)
        print(f"reader={reader}")
        for row in reader:
            print(f"row={row}")

    def readCsvBytes(self, csv_bytes):
        print("readCsvBytes")
        """Reads the Csv Bytes as String"""
        # Decode bytes to a string and wrap in StringIO
        # with open(file_name, encoding='utf-8-sig') as csvfile:
        string_io = StringIO(csv_bytes.getvalue())
        # string_io = StringIO(csv_bytes)
        # Read the CSV data using csv.reader
        csv_bytes.seek(0)
        reader = csv.reader(string_io)
        # Convert to a list of dictionaries
        output_list = [dict(zip(reader.__next__(), row)) for row in reader]
        print(output_list)

    def readCsvByte(self, csv_bytes):
        print("readCsvByte")
        # Read the CSV data
        csv_bytes.seek(0)
        reader = csv.reader(TextIOWrapper(csv_bytes, encoding='utf-8-sig'))
        print(f"reader={reader}")
        for row in reader:
            print(f"row={row}")

    def jsonWriter(self, filepath: str, data):
        """Writes data to filepath"""
        with open(filepath, 'w', encoding='utf-8') as csvfile:
            json.dump(data, csvfile, ensure_ascii=False, indent=4)

    def readCsvWithPandas(self, csv_bytes):
        # Read the CSV data into a DataFrame
        print(f"readCsvWithPandas => csv_bytes={csv_bytes}")
        csv_bytes.seek(0)
        df = pd.read_csv(csv_bytes)
        print(f"reading pandas => df=\n{df}")

        # iterate CSV entries
        # for index, (key, value) in enumerate(df.items()):
        #     print(f"Iterating index={index}, key={key}, value={value}")
        #     for i, email in enumerate(value):
        #         if not pd.isna(email):
        #             print(f"Iterating i={i}, email={email}")

        # allEmails = []
        # for index, (key, value) in enumerate(df.items()):
        #     # print(f"Iterating index={index}, key={key}, value={value}")
        #     # only read email and avoid other values like index
        #     emails = [email for _, email in enumerate(value) if not pd.isna(email)]
        #     # print(f"List of [{len(emails)}] emails={emails}")
        #     allEmails.extend(emails)
        #
        # print(f"List of [{len(allEmails)}] emails={allEmails}")

        csvFileContents = dict()
        for index, (key, value) in enumerate(df.items()):
            # print(f"Iterating index={index}, key={key}, value={value}")
            emails = [email for _, email in enumerate(value) if not pd.isna(email)]
            csvFileContents[key] = emails

        # print(f"List of [{len(csvFileContents)}] csvFileContents={csvFileContents}")
        print()
        self.jsonWriter('data.json', csvFileContents)

        # emails = [value for key, value in csvFileContents.items()]
        emails = []
        for key, value in csvFileContents.items():
            print(f"Iterating key={key}")
            emails.extend(value)

        # write all emails
        # emails = []
        # for key, value in enumerate(csvFileContents):
        #     emails.extend(value)
        # emails = [value for key, value in csvFileContents]
        self.jsonWriter('emails.json', emails)
        # print(f"{json.dumps(csvFileContents)}")

        print()
        column_names, columns = zip(*df.items())
        print(f"column_names={column_names}")
        print(f"columns={columns}")

    def download(self, bucket_name, file_name) -> BytesIO:
        print(f"+download({bucket_name}, {file_name})")
        s3_file_bytes = BytesIO()  # Buffered I/O implementation using an in-memory bytes buffer.
        # print(f"s3_file_bytes={s3_file_bytes}")
        s3 = boto3.client('s3')
        s3.download_fileobj(bucket_name, file_name, s3_file_bytes)
        print(f"-download() {bucket_name}/{file_name}, s3_file_bytes={s3_file_bytes}")
        return s3_file_bytes


if __name__ == '__main__':
    s3Client = S3Client()
    bucket_name = "tod-s3-dev-ue1-push-notification-rxlo"
    file_name = "prod_11_28.csv"
    s3_file_bytes = s3Client.download(bucket_name, file_name)
    print(f"s3_file_bytes={s3_file_bytes}")
    # s3Client.readCsvFile(s3_file_bytes)  # not Working
    # s3Client.readCsvBytes(s3_file_bytes) # Not Working
    # s3Client.readCsvByte(s3_file_bytes) # Working
    s3Client.readCsvWithPandas(s3_file_bytes)  # Working
