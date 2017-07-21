import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv("Intermarriage.csv")
print (data.columns)
data.columns = ["state", "rate"]
data.rate.hist()
plt.show()
