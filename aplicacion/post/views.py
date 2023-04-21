from django.shortcuts import render
import requests
#https://jsonplaceholder.typicode.com/posts
def users(request):
    # Realizar petición GET a la API
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    if response.status_code == 200:
        # Convertir los datos JSON a una lista de diccionarios de Python
        data = response.json()
        # Pasar los datos a la plantilla
        return render(request, 'user/users.html', {'data': data})
    else:
        # Si la petición no fue exitosa, regresar un error 404
        raise Http404("API no disponible")
    

def postDeUnUsuario(request, id):
    print(id)
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
   
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    data = response.json()
    
    if response.status_code == 200:
        # Convertir los datos JSON a una lista de diccionarios de Python
        data = response.json()
        
        usersArray = users.json()
        
        posts = [post for post in data if post['userId'] == id] or []

        user = [user for user in usersArray if user['id'] == id] or []

        # Pasar los datos a la plantilla
        return render(request, 'user/postUser.html', {'user': user[0], 'posts': posts})
    else:
        # Si la petición no fue exitosa, regresar un error 404
        raise Http404("API no disponible")