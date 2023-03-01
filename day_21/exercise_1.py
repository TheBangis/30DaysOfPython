import statistics

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