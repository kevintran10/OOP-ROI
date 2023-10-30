class RentalProperty():     # Parent Class
    def __init__(self, purchase_amount, annual_rent_income, costs):
        self.purchase_amount = purchase_amount
        self.annual_rent_income = annual_rent_income
        self.costs = costs


class ROI(RentalProperty):
    def __init__(self, purchase_amount, annual_rent_income, costs):
        super().__init__(purchase_amount, annual_rent_income, costs)
        self.purchase_amount = {}
        self.annual_rent_income = {}
    

    def income(self, income):
        self.income = income
        income = int(input('What is your total monthly income?'))
        income = self.purchase_amount[income]
        laundry = 0
        storage = 0
        misc = 0

    def cashflow(self, monthly_income, monthly_expenses):
        self.monthly_income = monthly_income   
        self.monthly_expenses = monthly_expenses

        monthly_income  = input('What is your monthly income?')
        monthly_expenses = input('What are your monthly expenses, if any?')
        self.annual_rent_income.append(monthly_income)


    def expenses(self, tax, insurance, utilities,):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities

    
    def calcROI(self):
        total_spending = self.monthly_expenses
        total_net_income = (self.annual_rent_income) - (self.costs)
        first_total_amount_spent = self.purchase_amount

        if first_total_amount_spent > 0:
            your_roi = (total_net_income / first_total_amount_spent) * 100
            return 'You made ${roi}.'
        else:
            return 'This might be a bad investment.'