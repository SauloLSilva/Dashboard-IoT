from datetime import date
from dateutil.relativedelta import relativedelta

six_months = date.today() + relativedelta(months=-12)
print(six_months)