import pandas as pd

#skip the first row and then load the data frame
df = pd.read_csv('data/stock_data.csv', skiprows=1)

#Renaming the row header names
df1 = pd.read_csv('data/stock_data.csv', header=1, names=['stock_sym', "eps", "revenue", "price", "chief"])

#Get just 2 rows
df2 = pd.read_csv('data/stock_data.csv', header=1, nrows=2)

#handling na values. Convert values from specific column to NaN
df3 = pd.read_csv('data/stock_data.csv', header=1, na_values = {
    "eps": ['not available'],
    'revenue':[-1],
    'people':['n.a.']
})
#print(df3)

#Converting NaN generically instead of column names
df4 = pd.read_csv('data/stock_data.csv', header=1, 
    names=['stock_sym', "eps", "revenue", "price", "chief"],
    na_values = ['not available', -1, 'n.a.'])
#print(df4)

df4['pe']= df4['price'].astype(float) / df4['eps'].astype(float)

#print(df4)

df4.to_csv('result/stock_pe.csv', index=False)

def standardise_currency(curr):
    if curr == 'SS' or curr == 'Dollars':
        return "USD"
    return "USD"

df_movies = pd.read_excel("data/movies_db.xlsx", 'movies')

df_financials = pd.read_excel("data/movies_db.xlsx", 'financials', converters = {
    'currency': standardise_currency
})

print(df_financials[['movie_id', 'budget', 'revenue', 'currency']].head(5))

df_merged = pd.merge(df_movies, df_financials, on="movie_id")
#print(df_merged.head(5))

df_merged.to_excel('result/movies_merged.xlsx', sheet_name="movie_financials", index=False)

df_stocks = pd.DataFrame({
    'stock_sym': ['GOOG', 'APPL', 'MSFT'],
    'price':[100, 200, 300],
    'pe':[10, 20, 40],
    'eps': [10, 20, 25]
})
df_weather = pd.DataFrame({
    'day': ['1/1/2024', '2/1/2024', '3/1/2024'],
    'temperature': [30, 32, 40],
    'event': ['Rain', 'Sunny', 'Sunny']
});
print(df_stocks)
print(df_weather)

with pd.ExcelWriter('result/stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")