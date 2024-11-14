class TripExpenses:
    def __init__(self, people):
        self.people = people
        self.balances = {person: {other: 0 for other in people if other != person} for person in people}

    def add_expense(self, payer, amount):
        split_amount = round(amount / len(self.people), 2)
        for person in self.people:
            if person != payer:
                self.balances[person][payer] += split_amount

    def record_payment(self, from_person, to_person, amount):
        self.balances[from_person][to_person] = round(self.balances[from_person][to_person] - amount, 2)

    def calculate_total_balances(self):
        final_balances = {}
        for person1 in self.people:
            for person2 in self.people:
                if person1 != person2:
                    amount = self.balances[person1][person2] - self.balances[person2][person1]
                    if amount > 0:
                        final_balances[(person1, person2)] = amount
                    elif amount < 0:
                        final_balances[(person2, person1)] = -amount
        return final_balances

    def show_detailed_balances(self):
        total_balances = self.calculate_total_balances()
        if not total_balances:
            print("Everyone is good")
        else:
            print("Here are the final balances:")
            for (person1, person2), amount in total_balances.items():
                print(f"{person1} owes {person2} ${amount:.2f}")


people = ["A", "B", "C"]
trip = TripExpenses(people)

trip.add_expense("A", 506.67)
trip.record_payment("B", "A", 168.89)
trip.add_expense("C", 300)
trip.add_expense("A", 60)
trip.show_detailed_balances()
trip.record_payment("B", "A", 20)
trip.record_payment("C", "A", 88.89)
trip.record_payment("B", "C", 100)
trip.show_detailed_balances()
