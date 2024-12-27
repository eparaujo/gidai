from revenues.models import Revenue
from expenses.models import Expense
from goals.models import Goal
from outflows.models import Outflow
from inflows.models import Inflow
from deposits.models import Deposit
from categories.models import Category
from withdrawals.models import Withdrawal
from django.utils.formats import number_format
from django.utils import timezone
from django.db.models import Sum, F
 

def get_revenue_metrics():
    revenues = Revenue.objects.all()
    expenses = Expense.objects.all()
    goals    = Goal.objects.all()
    
    total_revenue = sum(revenue.value for revenue in revenues)
    total_expense = sum(expense.value for expense in expenses)
    balance = total_revenue - total_expense
    total_goal = sum(goal.goalvalue for goal in goals)

    return dict(
        total_revenue=number_format(total_revenue, decimal_pos=2, force_grouping=True),
        total_expense=number_format(total_expense, decimal_pos=2, force_grouping=True),
        balance=number_format(balance, decimal_pos=2, force_grouping=True),
        total_goal=number_format(total_goal, decimal_pos=2, force_grouping=True),
        )
 
def get_expense_metrics():
    revenues = Revenue.objects.all()
    expenses = Expense.objects.all()
    goals    = Goal.objects.all()
    
    total_revenue = sum(revenue.value for revenue in revenues)
    total_expense = sum(expense.value for expense in expenses)
    balance = total_revenue - total_expense
    total_goal = sum(goal.goalvalue for goal in goals)

    return dict(
        total_revenue=number_format(total_revenue, decimal_pos=2, force_grouping=True),
        total_expense=number_format(total_expense, decimal_pos=2, force_grouping=True),
        balance=number_format(balance, decimal_pos=2, force_grouping=True),
        total_goal=number_format(total_goal, decimal_pos=2, force_grouping=True),
        )

def get_goal_metrics():
    goals    = Goal.objects.all()
    deposits = Deposit.objects.all()
    withdrawals = Withdrawal.objects.all()

    total_goal = sum(goal.goalvalue for goal in goals)
    total_deposit = sum(deposit.value for deposit in deposits)
    total_withdrawal = sum(withdrawal.value for withdrawal in withdrawals) 
    total_balance = total_deposit - total_withdrawal

    return dict(
        total_goal=number_format(total_goal, decimal_pos=2, force_grouping=True),
        total_deposit=number_format(total_deposit, decimal_pos=2, force_grouping=True),
        total_withdrawal=number_format(total_withdrawal, decimal_pos=2, force_grouping=True),
        total_balance=number_format(total_balance, decimal_pos=2, force_grouping=True),
        )
    

def get_expense_data(): #esta função é usada para calcular e passar os dados no contexto da view, a ser utilizada no gráfico da home
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(30, -1, -1)] #aqui se cria uma lista com dados dos últimos 7 dias
    values = list()

    for date in dates:
        expense_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_expenses = Sum(F('expense__value')*1)
        )['total_expenses'] or 0
        values.append(float(expense_total))

    return dict(
        dates=dates,
        values=values,
    )

def get_revenues_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(30, -1, -1)] #aqui se cria uma lista com dados dos últimos 7 dias
    values = list()

    for date in dates:
        revenue_total = Inflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_revenue=Sum(F('revenue__value')*1)
        )['total_revenue'] or 0
        values.append(float(revenue_total))

    return dict(
        dates=dates,
        values=values,
    )

def get_graphic_deposit_metrics():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(30, -1, -1)] #aqui se cria uma lista com dados dos últimos 7 dias
    values = list()

    for date in dates:
        deposits_total = Deposit.objects.filter(
            created_at__date=date
        ).aggregate(
            total_deposit=Sum(F('value'))
        )['total_deposit'] or 0
        values.append(float(deposits_total))

    return dict(
        dates=dates,
        values=values,
    )    
'''
def get_graphic_expense_category_metric():
    categories = Category.objects.all()
    expenses = Expense.objects.all()

    result = {
    category.name: Expense.objects.filter(kindexpense=kindexpense).aggregate(total_value=Sum('value'))['total_value'] or 0
    for category in categories
    }

    return result
'''