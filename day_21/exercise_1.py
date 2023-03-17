import statistics

'''ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# you output should look like this
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
'''

class Statistics:

    def __init__(self, age = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]):
        self.age = age

    def count(self):
       return len(self.age)
    
    def sum(self):
        return sum(self.age)
    
    def min(self):
        return min(self.age)
    
    def max(self):
        return max(self.age)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return statistics.mean(self.age)
    
    def median(self):
        return statistics.median(self.age)
    
    def mode(self):
        mode = statistics.mode(self.age)
        count = self.age.count(mode)
        return (mode, count)
    
    def standard_deviation(self):
        return statistics.stdev(self.age)
    
    def variance(self):
        return statistics.variance(self.age)
    
    def show_sta(self):
        print('count:', self.count())
        print('sum:', self.sum())
        print('min:', self.min())
        print('mix:', self.max())
        print('range:', self.range())
        print('sum:', self.mean())
        print('Mode: ', self.mode())
        print('Standard Deviation: ', self.standard_deviation()) 
        print('Variance: ', self.variance())

a = Statistics()
a.show_sta()


