## Instruccións de instalación

Requírese Python3 e PIP instalados.

Instalar dependencias:

```shell
pip3 install django
```

Verificación:

```shell
python3 -m django --version
```



## Creación do proxecto

```shell
django-admin startproject votaciones
```

Se o comando anterior non funciona, pode probarse a substituir `django-admin` por `python3 -m django`, indicando os argumentos adicionais.

Dende o terminal, crear entorno virtual:

```shell
cd votaciones
python3 -m virtualenv -p python3 .venv
```


Activar entorno virtual:

```shell
source .venv/bin/activate
```

Instalar Django coma dependencia específica do proxecto:

```shell
pip install django
```

Abra o cartafol do proxecto con VSCode e comece a traballar nel.

## Creación dunha 'app'

Un proxecto Django componse de varias apps. Utilícese este comando para crear unha:

```shell
python manage.py startapp polls
```

Neste caso creáse unha nova app co nome polls.

## Creación de vistas

Crear unha vista dentro de `polls/views.py`.

Crear un ficheiro de rutas, `polls/urls.py` e engadir as rutas correspondentes as vistas:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Enlazar este ficheiro de rutas dende o principal: `votaciones/urls.py`.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

Probe o funcionamento visitando http://localhost:8000.

## Creación dos modelos

En `polls/models.py` definir os modelos `Question` e `Choice`.

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Os modelos están definidos, pero non serán activados ata que no módulo `settings.py` (dentro de `votaciones`) se inclúa a app `polls` na lista `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls'
]
```

Tamén será necesario xerar unhas migracións, que se ocuparán de modificar a estrutura da base de datos para conter as táboas e relacións definidas nos modelos. Isto faise co seguinte comando:

```shell
python manage.py makemigrations
```

E agora procesaranse as migracións pendentes con este outro comando:

```python
python manage.py migrate 
```

## Creación dun superusuario

Un superusuario é quen de facer operacións administrativas no sitio web. Django incorpora unha interface administrativa na que só este tipos de usuarios poden entrar. Para iso, cómpre crear un destes usuarios. Proceda con este comando:

```shell
python manage.py createsuperuser
```

Responda as preguntas e terá o seu superusuario. Visite agora http://localhost:8000/admin e probe a iniciar sesión coas credenciais elexidas.

## Interface administrativa da app polls

Na área de administración poderá observar que non aparecen os modelos definidos para a app polls. Iso débese a que en ningún momento se estableceu que terían que aparecer. É necesario declaralo no ficheiro `polls/admin.py`. 

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

Garde os cambios e recargue a páxina de administración. Aparecerá o modelo Question no menú da esquerda.

