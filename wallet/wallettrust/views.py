from django.shortcuts import render
# from django.http import HttpResponse
from django.db import connection

def info(request, WALLET_UUID):

    table = ''

    amount = request.GET.get('amount')
    operation = request.GET.get('operationType')
    balans = amount

    with connection.cursor() as cursor:
        # добовляет значение текущей строки в БВЗЕ ДАННЫХ
        if operation == 'dep':
            cursor.execute(f'UPDATE wallet_table SET balans = balans + {balans} WHERE walletid = {WALLET_UUID};')

            #cursor.execute(f"insert into wallet_table (walletid, balans) values ('{WALLET_UUID}','{balans}')") # это строка для созжания новой позиции в БАЗЕ ДАННЫХ

        # отнимает значение текущей строки в БВЗЕ ДАННЫХ
        elif operation == 'w':
            cursor.execute(f'UPDATE wallet_table SET balans = balans - {balans} WHERE walletid = {WALLET_UUID};')


        cursor.execute(f"select * from wallet_table")
        rowss = cursor.fetchall()  # получаем все строки

        for row in rowss:
            table = row[1]





    data = {"text": f'{table}'}
    # return HttpResponse(f'номер кошелька {WALLET_UUID},сумма {amount}, баланс {balans}')
    # return HttpResponse(f'{table}')
    return render(request, 'index.html', context= data)