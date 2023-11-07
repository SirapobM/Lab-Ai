def calculate_electricity_cost(unit):
    if unit <= 150:
        if unit <= 15:
            electricity_usage = unit * 2.3488
        elif unit <= 25:
            electricity_usage = 15 * 2.3488 + (unit - 15) * 2.9882
        elif unit <= 35:
            electricity_usage = 15 * 2.3488 + 10 * 2.9882 + (unit - 25) * 3.2405
        elif unit <= 100:
            electricity_usage = (
                15 * 2.3488 + 10 * 2.9882 + 10 * 3.2405 + (unit - 35) * 3.6237
            )
        else:
            electricity_usage = (
                15 * 2.3488
                + 10 * 2.9882
                + 10 * 3.2405
                + 65 * 3.6237
                + (unit - 100) * 3.7171
            )
        service_fee = 8.19
    else:
        if unit <= 150:
            electricity_usage = unit * 3.2484
        elif unit <= 400:
            electricity_usage = 150 * 3.2484 + (unit - 150) * 4.2218
        else:
            electricity_usage = 150 * 3.2484 + 250 * 4.2218 + (unit - 400) * 4.4217
        service_fee = 38.22

    ft_fee = unit * 0.2048
    vat = (ft_fee + electricity_usage) * 7 / 100
    payment = ft_fee + electricity_usage + vat + service_fee
    return payment


while True:
    name = input("Enter your name : ")
    print("Press exit to end program")
    if name.lower() == "exit":
        break
    else:
        unit = int(input("Enter your unit : "))
        payment = calculate_electricity_cost(unit)
        print(f"Unit {name}: {payment:.2f} Baht")
        print("\n")
    except ValueError:
        print("Enter your number : ")
