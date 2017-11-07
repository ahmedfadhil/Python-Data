import pandas as pd
import numpy as np

# pd.Series?
sports = {
    'c1': 'item1',
    'c2': 'item2',
    'c3': 'item3',
    'c4': 'item4',
}

s = pd.Series(sports)
# print(s)

jacomi = s.iloc[3]
jacomi2 = s.loc['c3']

print(jacomi2)

somemore = pd.Series([100, 23, 345, 432, 456])

tot = 0
for i in somemore:
    tot += i
# print(tot)

total = np.sum(somemore)
# print(total)

data = pd.Series(np.random.randint(0, 100, 1000))
# print(len(data))

summery = 0
for i in data:
    summery += i

# print(summery)
summery2 = np.sum(data)

print(summery2)

for label, values in data.iteritems():
    data.set_value(label, values + 2)

whack = data.head()
print(whack)

data2 = pd.Series(np.random.randint(0, 100, 1000))

data2 += 2
print(data2)

original_sport = pd.Series({
    'Austria': 'something1',
    'Japan': 'something2',
    'USA': 'something3',
    'UK': 'something4',
})

another_list = pd.Series(['country1', 'country2', 'country3', 'country4'],
                         index=[
                             'list',
                             'list',
                             'list',
                             'list'
                         ])

all_list = original_sport.append(another_list)



print(another_list)
