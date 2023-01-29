import pandas as pd
from sklearn.model_selection import train_test_split
import codecs

def convert_to_utf8(file_path):
    with codecs.open(file_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    with codecs.open(file_path, 'w', encoding='UTF-8') as f:
        f.write(content)


def split_data(file_name, test_size=0.2, swap_columns = False, header = None):
    # Read the CSV file into a DataFrame
    encoding = "utf-8"
    attempts = 0
    while attempts < 2:
        try:
            data = pd.read_csv(file_name, encoding= encoding, header= header)
            break
        except UnicodeDecodeError:
            attempts +=1
            convert_to_utf8(file_path=file_name)

    # Swap columns
    if swap_columns:
        data[data.columns[0]], data[data.columns[1]] = data[data.columns[1]], data[data.columns[0]]


    # Split the data into training and testing sets
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)



    # Output the training and testing sets to their own CSV files
    train_data.to_csv(r"tradingBot\modelData\sentimentData\sentiment_train_data.csv", index=False, header = None)
    test_data.to_csv(r"tradingBot\modelData\sentimentData\sentiment_test_data.csv", index=False, header = None)

# Example usage:
if __name__ == "__main__":
    split_data(r"tradingBot\modelData\sentimentData\all-data.csv", test_size=0.2, swap_columns = True)
