def tally_melons():
    log_file = open("orders-by-type.txt")
    tally_by_type = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    for line in log_file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        tally_by_type[melon_type] += melon_count

    log_file.close()

    return tally_by_type


def sum_revenue(tally_by_type, price_by_type):
    revenue_by_type = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    for melon_type in tally_by_type:
        price = price_by_type[melon_type]
        revenue = price * tally_by_type[melon_type]
        revenue_by_type[melon_type] += revenue

    return revenue_by_type


SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80
price_by_type = {"Musk": 1.15,
                 "Hybrid": 1.30,
                 "Watermelon": 1.75,
                 "Winter": 4.00}


print "*" * DORKY_LINE_LENGTH

#tally up sales by melon type
tally_by_type = tally_melons()

#calculate revenue per type
revenue_by_type = sum_revenue(tally_by_type, price_by_type)

#report tally and revenue by type
for melon_type in tally_by_type:
    out_str = ("We sold {count} {type} melons at {price_per:.2f} each, " +
               "for a total revunue of ${total_revenue:,.2f}.")
    print out_str.format(count = tally_by_type[melon_type],
                         type = melon_type,
                         price_per = price_by_type[melon_type],
                         total_revenue = revenue_by_type[melon_type])

    # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (tally_by_type[melon_type], melon_type, price, revenue)
    # print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(tally_by_type[melon_type], melon_type, price, revenue)
print "******************************************"
log_file = open("orders-with-sales.txt")
sales = [0, 0]
for line in log_file:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
print "Internet sales generated ${:.2f} in revenue.".format(sales[0])
if sales[1] > sales[0]:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"
print "******************************************"
