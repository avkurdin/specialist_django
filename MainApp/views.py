from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

author = {
    'name': 'Иван',
    'middle': 'Петрович',
    'surname': 'Иванов',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
}


def get_item(request, id):
    for item in items:
         if item['id'] == id:
    #         result = f"""
    #                 <h1>Имя: {item["name"]}</h1>
    #                 <p>Количество: {item['quantity']}</p>
    #                 <a href='/items'>Назад</a>
    #                 """
    #         return HttpResponse(result)
    # return HttpResponseNotFound(f'Item with id={id} not found')
            context = {
                'item': item
            }
            return render(request, 'items_page.html', context)
    return HttpResponseNotFound(f'Item with id={id} not found')

# Create your views here.
def home(request):
    #     text = """<<h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # """
    #     return HttpResponse (text)
    contex = {
        'name': 'ABS',
        'email': 'abs@abs.ru'
    }
    return render(request, 'index.html', contex)
def about(request):
    text = f"""
        <strong>Имя: </strong><i>{author['name']}</i><br>
        <strong>Отчество:  </strong><i>{author['middle']}</i><br>
        <strong>Фамилия:  </strong><i>{author['surname']}</i><br>
        <strong>Иелефон:  </strong><i>{author['phone']}</i><br>
        <strong>email:  </strong><i>{author['email']}</i><br>
        </strong>
        """
    return HttpResponse (text)
def items_list(request):
    # result = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</li>"
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        'items': items
    }
    return render(request, 'items-list.html', context)
