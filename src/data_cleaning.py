import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    return df


def save_data(df, output_path):
    df.to_csv(output_path, index=False)


def main():
    input_path = "data/raw/sales_data.csv"
    output_path = "data/processed/cleaned_data.csv"

    df = load_data(input_path)
    df = clean_data(df)
    save_data(df, output_path)

    print("Data cleaned and saved successfully!")


if __name__ == "__main__":
    main()
