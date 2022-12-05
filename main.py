import pandas as pd
import sys


def main():
    input_name = sys.argv[1]
    with open(input_name, 'r') as input_file:
        df = pd.read_csv(input_file, header=None)
    df.columns = ['ID', 'Area', 'Product', 'Quantity', 'Brand']
    pa = df.groupby('Product')['Quantity'].agg(
        [('Avg. Qty.', lambda x: x.sum())]).reset_index()
    pa['Avg. Qty.'] = pa['Avg. Qty.'] / len(df)
    pa.to_csv('0_' + input_name, header=None, index=None)
    pb = df.groupby(['Product', 'Brand'])['ID'].agg(['count']).reset_index()
    pb = pb.sort_values('count', ascending=False).drop_duplicates(['Product'])
    pb = pb.drop(columns='count')
    pb.to_csv('1_' + input_name, header=None, index=None)


if __name__ == "__main__":
    main()
