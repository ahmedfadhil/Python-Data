# sales_record = {
# 'price' : 23,
# 'num_items' : 4,
# 'person' : 'chris'}
#
# sales_statement = '{} bought {} items at a price of {} each for a total of {}'
#
# print(sales_statement.format(sales_record['person'],
# sales_record['num_items'],
# sales_record['price'],
# sales_record['num_items']* sales_record['price']))
import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

    # print(mpg[3:])
    # print(len(mpg))
    # print(mpg[0].keys())

summing = sum(float(d['origin']) for d in mpg) / len(mpg)

cylinders = set(d['cylinders'] for d in mpg)

cty_by_mpg = []
for c in cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cylinders'] == c:
            summpg += float(d['cylinders'])
            cyltypecount += 1
    cty_by_mpg.append((c, summpg / cyltypecount))

cty_by_mpg.sort(key=lambda x: x[0])

vehiclecalss = set(d['name'] for d in mpg)
hwy_mpg_by_class = []
for t in vehiclecalss:
    summpg = 0
    vclassaccount = 0
    for d in mpg:
        if d['name'] == t:
            summpg += float(d['model_year'])
            vehiclecalss += 1
    hwy_mpg_by_class.append(t, summpg / vclassaccount)

hwy_mpg_by_class.sort(key=lambda x: x[1])
print(cylinders)
