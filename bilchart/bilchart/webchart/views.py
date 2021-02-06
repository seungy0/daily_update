from django.shortcuts import render
from django.http import HttpResponse
from .models import Bilchart
# Create your views here.


def index(request):
    bilcharts = Bilchart.objects.all()  # bilchart에 있는 모든 객체를 불러와 candidates에 저장
    str = ''  # 리턴해줄 문자열(14번째줄)
    for bilchart in bilcharts:
        str += "<p>rank {}  title {}<br>".format(bilchart.rank, bilchart.song)  # <br>은 html코드로 다음줄로 줄내림할때 사용
        str += "{}</p>".format(Bilchart.singer)  # <p>는 html코드로 단락이동할때
    #  return HttpResponse(str)
    return render(request, 'webchart/index.html')

# # 새로 import 하는 모듈

# from django.db import connection
# def BookListView(request):
#     # books = Book.objects.all()
#     try:
#         cursor = connection.cursor()

#         strSql = "SELECT code, name, author FROM bookstore_book"
#         result = cursor.execute(strSql)
#         datas = cursor.fetchall()

#         connection.commit()
#         connection.close()

#         datas = []
#         for data in books:
#             row = {'code': data[0],
#                    'name': data[1],
#                    'author': data[2]}

#             books.append(row)

#     except:
#         connection.rollback()
#         print("Failed selecting in BookListView")


#     return render(request, 'book_list.html', {'books': datas})