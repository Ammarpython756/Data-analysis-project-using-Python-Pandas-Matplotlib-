import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def plot_revenue(df):
    # إضافة عمود الإيرادات
    df['revenue'] = df['quantity'] * df['price']

    # الإيرادات حسب المنتج
    revenue_by_product = df.groupby('product')['revenue'].sum()
    revenue_by_product.plot(kind='bar', title='Revenue by Product', color='skyblue')
    plt.ylabel('Revenue')
    plt.savefig('outputs/revenue_by_product.png')
    plt.clf()

    # الإيرادات حسب العميل
    revenue_by_customer = df.groupby('customer')['revenue'].sum()
    revenue_by_customer.plot(kind='bar', title='Revenue by Customer', color='orange')
    plt.ylabel('Revenue')
    plt.savefig('outputs/revenue_by_customer.png')
    plt.clf()


def main():
    file_path = "data/processed/cleaned_data.csv"
    df = load_data(file_path)
    plot_revenue(df)
    print("Charts saved in outputs folder!")


if __name__ == "__main__":
    main() 
