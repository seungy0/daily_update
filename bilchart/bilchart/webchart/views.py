from django.shortcuts import render

# Create your views here.


def index(request):
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