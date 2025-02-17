import csv
import random

if __name__== "__main__":


    def read_data(filepath: str, header=True, delimiter=",", start_index = 1, end_index = -1):
        labels = []
        data = []

        with open(filepath) as filehandler:
            reader = csv.reader
            for line_idx, line in enumerate(filehandler):
                data.append(line)
            if header:
                labels = data[0]
                data = data[1:]

            if start_index != 1 and end_index != -1:

                return labels, data[start_index: end_index]
            else:
                return labels, data

    data_header, data_data = read_data("winequality-red.csv", delimiter=",", start_index = 3, end_index = 25)

    def split_dataset(dataset, train, test, validate):
        random.shuffle(dataset)
        size = len(dataset)

        train_set = dataset[:int((size + 1) * train)]
        test_set = dataset[:int((size + 1) * test)]
        validate_set = dataset[:int((size + 1) * validate)]

        return train_set, test_set, validate_set


    wine_labels, wine_dataset = read_data("winequality-red.csv")
    train, test, validate = split_dataset(wine_dataset, 0.6, 0.3, 0.1)

    writer = csv.writer(open("train.csv", "w", newline=''))
    train = [sublst.split(",") for sublst in train]
    data_header = data_header.split(",")
    writer.writerow(data_header)
    for row in train:
        print(row[:-1])
        writer.writerow(row[:-1])

    def get_col(data, header_name, delim = ","):

        vals = []

        with open(data) as f:
            reader = csv.DictReader(f, delimiter = delim)

            for row in reader:
                row_val = row[header_name]
                vals.append(row_val)

        size = len(vals)
        return header_name, size



    print(get_col("winequality-red.csv", "volatile acidity"))


    def extract_data(data, header_name, value,  delim = ","):


        vals = []

        with open(data) as f:
            reader = csv.DictReader(f, delimiter=delim)

            for row in reader:
                row_val = row[header_name]
                if float(row_val) > value:
                    vals.append(row_val)

        out = {header_name: vals}
        return out

    subset = extract_data("winequality-red.csv", "volatile acidity", 0.5)
    print(subset)

    def get_col(data, header_name, delim = ","):


        vals = []

        with open(data) as f:
            reader = csv.DictReader(f, delimiter=delim)

            for row in reader:
                row_val = row[header_name]
                vals.append(row_val)

        out = {header_name: vals}
        return out

    print(get_col("winequality-red.csv", header_name= "residual sugar"))