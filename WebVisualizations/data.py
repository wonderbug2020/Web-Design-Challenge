import pandas as pd
data_df = pd.read_csv('Resources/cities.csv')

htmlData = data_df.to_html()

data_df.to_html('table.html')

text_file = open("data.html", "w")
text_file.write(htmlData)
text_file.close()
