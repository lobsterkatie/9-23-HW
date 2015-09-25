def main():
    #these were actually backwards
    # SALESPERSON_INDEX = 0
    # INTERNET_INDEX = 1
    DORKY_LINE_LENGTH = 80
    price_by_type = {"Musk": 1.15,
                     "Hybrid": 1.30,
                     "Watermelon": 1.75,
                     "Winter": 4.00}
    # log_by_type_path = "orders-by-type.txt"


    #tally up sales by melon type
    tally_by_type = tally_melons()

    #calculate revenue per type
    revenue_by_type = sum_revenue(tally_by_type, price_by_type)

    #report tally and revenue by type
    print "*" * DORKY_LINE_LENGTH

    for melon_type in tally_by_type:
        out_str = ("We sold {count} {type} melons at {price_per:.2f} each, " +
                   "for a total revunue of ${total_revenue:,.2f}.")
        print out_str.format(count = tally_by_type[melon_type],
                             type = melon_type,
                             price_per = price_by_type[melon_type],
                             total_revenue = revenue_by_type[melon_type])

    #tally sales by source (salesperson or online)
    sales_by_source = tally_sales_by_source()

    #report and comment upon results
    print "*" * (DORKY_LINE_LENGTH / 2)

    out_str = "Salespeople generated ${rev:,.2f} in revenue."
    print out_str.format(rev = sales_by_source["human"])

    out_str = "Internet sales generated ${rev:,.2f} in revenue."
    print out_str.format(rev = sales_by_source["internet"])

    if sales_by_source["human"] > sales_by_source["internet"]:
        print "Guess there's some value to those salespeople after all!"
    else:
        print "Time to fire the sales team! Online sales rule all!"

    print "*" * (DORKY_LINE_LENGTH / 2)



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


def tally_sales_by_source():
    log_file = open("orders-with-sales.txt")
    sales_tally = {"human": 0, "internet": 0}
    # sales = [0, 0]
    for line in log_file:
        data = line.split("|")
        sale_source = data[2]
        sale_amount = float(data[3])
        if sale_source == "ONLINE":
            sales_tally["internet"] += sale_amount
        else:
            sales_tally["human"] += sale_amount

    return sales_tally


main()
