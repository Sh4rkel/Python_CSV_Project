import pandas as pd
import matplotlib.pyplot as plt


class CrimeDataAnalyzer:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)

    def analyze_monthly_crimes(self):
        self.data['Date Rptd'] = pd.to_datetime(self.data['Date Rptd'], format='%m/%d/%Y %I:%M:%S %p')
        self.data['DATE OCC'] = pd.to_datetime(self.data['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')

        self.data['Month Rptd'] = self.data['Date Rptd'].dt.month
        self.data['Month OCC'] = self.data['DATE OCC'].dt.month

        combined_data = pd.concat([self.data['Month Rptd'], self.data['Month OCC']])
        monthly_counts = combined_data.value_counts().sort_index()

        return monthly_counts

    def plot_monthly_crimes(self, title="Monthly Crime Report"):
        monthly_counts = self.analyze_monthly_crimes()

        plt.bar(monthly_counts.index, monthly_counts.values)
        plt.xlabel("Month")
        plt.ylabel("Number of Crimes")
        plt.title(title)

        month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        plt.xticks(monthly_counts.index, month_labels)

        plt.show()


if __name__ == '__main__':
    data_file = 'Crime_Data_from_2020_to_Present.csv'  
    analyzer = CrimeDataAnalyzer(data_file)
    analyzer.plot_monthly_crimes()
