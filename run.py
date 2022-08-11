from search.flights import FlightSearcher

print("Return or one way?")
return_or_oneway = input(">")
print("What class? (Economy, premium economy, business, first)")
flight_class_element = input(">")

print("Where are you travelling from?")
where_from = input(">")
print("Where are you travelling to?")
where_to = input(">")
print("What month are you going?")
check_in_month = input(">")
print("What day are you going?")
day_going = input(">")
if return_or_oneway.strip().lower() == "return":
    print("What month are you coming back?")
    check_out_month = input(">")
    print("What day are you coming back?")
    day_going_back = input(">")
print("How many adults (12+)")
adults = input(">")
print("How many children (2-11)")
children = input(">")
print("How many infants (<2)")
infants = input(">")
print("Best, Cheapest or Fastest flight?")
the_choice = input(">")

with FlightSearcher() as bot:
    if return_or_oneway.strip().lower() == "return":
        bot.first_page()
        bot.agree()
        bot.where_from(where_from)
        bot.where_to(where_to)
        bot.check_in_and_out_date(check_in_month, day_going)
        bot.check_in_and_out_date(check_out_month, day_going_back)
        bot.passengers(adults, children, infants)
        bot.flight_class(flight_class_element)
        bot.search()
        if the_choice.strip().lower() == "cheapest":
            bot.cheapest()
        elif the_choice.strip().lower() == "fastest":
            bot.fastest()
    else:
        bot.first_page()
        bot.agree()
        bot.one_way()
        bot.where_from(where_from)
        bot.where_to(where_to)
        bot.check_in_and_out_date(check_in_month, day_going)
        bot.passengers(adults, children, infants)
        bot.flight_class(flight_class_element)
        bot.search()
        if the_choice.strip().lower().capitalize() == "Cheapest":
            bot.cheapest()
        elif the_choice.strip().lower().capitalize() == "Fastest":
            bot.fastest()

    # MTAwNjE5NjgxNTk1MzE1NDA2OA.G4x8za.tqi6hfcvIMGtzJERFOGHHxxU8kQXegsLTB7XOI