import json
import random
from datetime import datetime, timedelta

with open('inputFileContainingNewLineDelimitedDateFormatObjects.txt') as f, open('output.csv', 'w') as f1:
    array_of_formats = []
    for line in f:
        j_content = json.loads(line)
        print(dict(j_content)['format'])
        array_of_formats.append(dict(j_content)['format'])
    for i in range(len(array_of_formats)):
        for j in range(len(array_of_formats)):
            if j == (len(array_of_formats) - 1):
                f1.write('"' + datetime.now().strftime(array_of_formats[j]) + '"')
            else:
                f1.write('"' + (datetime.now() +
                                timedelta(days=random.randint(1, 200), hours=random.randint(1, 10))
                                ).strftime(array_of_formats[j]) + '",')
        f1.write("\n")
