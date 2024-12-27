import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics
 
#a view é que envia os dados para o HTML via context
@login_required(login_url='login')
def home(requests):
    revenue_metrics = metrics.get_revenue_metrics()
    expense_metrics = metrics.get_expense_metrics()
    goal_metrics = metrics.get_goal_metrics()
    daily_expenses_data = metrics.get_expense_data()
    daily_revenues_data = metrics.get_revenues_data()
    daily_deposits = metrics.get_graphic_deposit_metrics()
    #graphic_expense_category_metric = metrics.get_graphic_expense_category_metric()


    context = {
        'revenue_metrics': revenue_metrics,
        'expense_metrics': expense_metrics,
        'goal_metrics': goal_metrics,
        'daily_expenses_data': json.dumps(daily_expenses_data), #transforma um dicionário em json
        'daily_revenues_data': json.dumps(daily_revenues_data), #transforma um dicionário em json
        'daily_deposits': json.dumps(daily_deposits),
        #'expense_by_category': json.dumps(graphic_expense_category_metric),
    }
    return render(requests, 'home.html', context)

