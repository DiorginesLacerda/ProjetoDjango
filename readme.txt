#README

1 - Criar um ambiente isolado
$ virtualenv --python=python3.5 virtualenv

2 - Ativar o ambiente
$ source virtual/bin/activate
# Após a ativação do ambiente o terminal irá mudar

3 - Instalar o Django
$ pip install Django

4 - Iniciar um projeto Django no diretorio atual
$ django-admin starproject mysite .
# se não utilizar o '.'(ponto) o djando criará uma pasta para o projeto

5 - Alterar o arquivo mysite/settings.py nas seguintes linhas
    TIME_ZONE = 'America/Sao_Paulo'
    LANGUAGE_CODE = 'pt-br'

    5.2 Adicionar o caminho para arquivos estáticos, adicionado a linha STATIC_ROOT ao arquivo settings.py
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    5.3 Banco de dados
        O banco de dados é setado em DATABASES, estando como default o sqlite3

6 - Criar o banco de dados para o arquivo
$ python manage.py migrate
# após o comando o arquivo db.sqlite3 é criado, confirmando a criação do banco de dados

7 - Criar uma aplicação
$ python manage.py startapp blog
# a pasta blog será criada

8 - Adicionar blog à sua lista de APPs
    No arquivo mysite/settings.py adicione 'blog', na lista INSTALLED_APPS
    a vírgula depois do nome é necessária!
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'blog',
         ]

9 - Criar a model post, editando o arquivo blog/models.py
        mais detalhes em https://tutorial.djangogirls.org/pt/django_models/

10 - Criar as tabelas para o Banco
    Criar um arquivo de migração de banco
    $ python manage.py makemigrations blog

    Aplicar o arquivo de migração
    $ python manage.py migrate blog

11 - Alterar o arquivo blog/admin.py
    Para que o django admin administre os posts, criados a partir do modelo models
    detalhes em https://tutorial.djangogirls.org/pt/django_admin/

12 - Criar superuser para administrar o django-admin
    $ python manage.py createsuperuser
        utilisei:
            user: admin
            password: administrator

13 - Incluir as URLs do blog às urls do mysite
    Edite o arquivo mysite/urls.py
        from django.conf.urls import include, url
        from django.contrib import admin

        urlpatterns = [
            url(r'^admin/', include(admin.site.urls)),
            url(r'', include('blog.urls')),
        ]

14 - Cria o arquivo blog/urls.py com o conteúdo:
    from django.conf.urls import include, url
    from . import views

    urlpatterns = [
    url(r'^$', views.post_list),
    ]

15 - Edite o arquivo blog/views.py
    inclua no fim do arquivo
        def post_list(request):
            return render(request, 'blog/post_list.html', {})
    
    # esta função aponta para um template
16 - criar o arquivo blog/templates/blog/post_list.html
    #será necessário criar a árvore de dretórios



       






