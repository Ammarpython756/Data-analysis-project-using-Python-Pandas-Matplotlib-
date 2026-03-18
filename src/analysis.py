import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def analyze_data(df):
    # Total revenue
    df['revenue'] = df['quantity'] * df['price']

    # Revenue by product
    revenue_by_product = df.groupby('product')['revenue'].sum()

    # Revenue by customer
    revenue_by_customer = df.groupby('customer')['revenue'].sum()

    print("Revenue by product:")
    print(revenue_by_product)
    print("\nRevenue by customer:")
    print(revenue_by_customer)


def main():
    file_path = "data/processed/cleaned_data.csv"
    df = load_data(file_path)
    analyze_data(df)


if __name__ == "__main__":
    main()
