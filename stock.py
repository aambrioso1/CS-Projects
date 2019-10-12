"""
Given stock information for several days, we do a little analysis.

The problem
The manatees of the Indian River Lagoon have decided to play the market and they asked you to write some code to analyze the historical trends of the S&P 500. The S&P 500 is a stock market index that tracks the stocks of 500 coporation in the US with large market capitalization. They know that Yahoo is a good source for this data. It can be easily downloaded as a CSV file.
For example:

Date,Open,High,Low,Close,Adj Close,Volume
2019-10-01,2983.689941,2992.530029,2938.699951,2940.250000,2940.250000,3558040000
2019-10-02,2924.780029,2924.780029,2874.929932,2887.610107,2887.610107,3912520000
2019-10-03,2885.379883,2911.129883,2855.939941,2910.629883,2910.629883,3503640000
2019-10-04,2918.560059,2953.739990,2918.560059,2952.010010,2952.010010,2990830000

The first row are the column headings. The dates will always be in order; and no trading dates will be missing. There were always be at least two trading days in a data set.
The manatees wish to know the maximum daily gain, daily loss (in percent change), and the longest growth streak in the data. The data that is pertainent to the manatees' request is the adjusted close value and the trading date. The daily gain or loss is from adjusted closing to the next trading day's adjusted closing.

For the data above, the output is:

Max gain: 1.42% on Fri, 04 Oct 2019
Max loss: -1.79% on Wed, 02 Oct 2019
Longest growth streak: 2 days (Thu, 03 Oct 2019 to Fri, 04 Oct 2019)

Please, follow the format carefully.
All input is on the standard input stream; write all output to the standard output stream.
"""

from datetime import *

# Example data
text = """
Date,Open,High,Low,Close,Adj Close,Volume\n2019-10-01,2983.689941,2992.530029,2938.699951,2940.250000,2940.250000,3558040000\n2019-10-02,2924.780029,2924.780029,2874.929932,2887.610107,2887.610107,3912520000\n2019-10-03,2885.379883,2911.129883,2855.939941,2910.629883,2910.629883,3503640000\n2019-10-04,2918.560059,2953.739990,2918.560059,2952.010010,2952.010010,2990830000"""

# We split the data 
data = text.split('\n')

data_list = [data[i].split(',') for i in range(len(data))]



date_list = [data_list[i][0] for i in range(1,len(data))]
close_list = [float(data_list[i][5]) for i in range(2,len(data))]

    
# print(data_list)
# print(date_list)
print('print close list:', close_list)
# value_dict = dict(zip(date_list,close_list))
# print(value_dict)

# Create a list of percent gains for each daily pair.
# Compute the maximum and minimum of each list.

gains_list = [100.0*(close_list[i]-close_list[i-1])/close_list[i-1] for i in range(1, len(close_list))]

print(gains_list)

# Create function that take the input date format and produce the correct output format.
# For example:  Input:  '2019-10-03' becomes 'Thu, 03 Oct 2019'.
# Here's how we can get the proper date format
dt = datetime.strptime("1921-11-06", "%Y-%m-%d")
print('proper date format: ', dt.strftime('%a, %d %b %Y'))

# Use list of gains to find the longest growth strength:  streak_length
max_gain = max(gains_list)
date1 = 2
max_loss = min(gains_list)
date2 = 4
streak_length = 5
date3 = 6
date4 = 7

"""
Output information in the correct format:
"""
print('*************************')
print('Max gain: {0:5.2f}% on {1:f}\nMax loss: {2:5.2f}% on {3:f}\nLongest growth streak: {4:f} days ({5:f} to {6:f})'.format(max_gain, date1, max_loss, date2, streak_length, date3, date4))

