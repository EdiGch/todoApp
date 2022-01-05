Assessment System
============

# Instalacja nowego projektu DjangoRest

## Podstawy
Chcąc uniknąć instalacji w przestrzeni globalnej należy użyć wirtualnego
środowiska. W przypadku, gdy mamy kilka projektów i te potrzebują do działania różnych wersji tej samej biblioteki mamy
problem. Rozwiązaniem jest użycie biblioteki virtualenv. Pozwala ona na tworzenie odizolowanych środowisk z Pythonem i
zależnościami.

* Stworzenie środowiska wirtualnego env. 
    * Aby zainstalować virtualenv wpisujemy w konsoli:
      ```shell
        pip install virtualenv
      ```
    * Instalacja virtualenv w katalogu projektu:
      ```shell
      virtualenv -p python3.10 env
      ```
    * Wejście/uruchomienie środowiska wirtualnego:
      ```shell
      source env/bin/activate
      ```
    * Wyjście/dezaktywacja środowiska wirtualnego:
      ```shell
      deactivate
      ```

Tworząc projekt warto podać w pliku requirements.txt listę zależności, które są wymagane by uruchomić projekt.
* Instalacja zależności z pliku
    * Wejście/uruchomienie środowiska wirtualnego:
      ```shell
      source env/bin/activate
      ```
    * Instalacja z pliku:
      ```shell
      pip install -r requirements.txt
      ```
      
Menadżer pakietów pip. Lista podstawowych komend:
 ```shell
pip install <package>           # instalacja pakietu
pip install <package> --upgrade # aktualizacja pakietu
pip uninstall                   # odinstalowuje pakiety
pip list                        # wyświetla listę zainstalowanych pakietów
pip list --outdated             # wyświetla listę nieaktualnych pakietów
pip show                        # wyświetla szczegóły na temat pakietu
pip freeze                      # wyświetla listę zainstalowanych pakietów w formacie plików requirements.txt
pip freeze > requirements.txt   # Zapisuje w pliku listę zainstalowanych pakietów
pip install -r requirements.txt # instaluje zależności z pliku requirements.txt
```
      
## Instalacja nowego projektu django-rest
Tworzy strukturę katalogów projektu Django, upewnij się, że masz aktywowane środowisko wirtualne ```source env/bin/activate```. Kod, który ustanowi projekt Django – zbiór ustawień dla instancji Django, w tym konfigurację bazy danych, opcje specyficzne dla Django i ustawienia specyficzne dla aplikacji.
```shell
django-admin startproject assessment_system
```

## Uruchomienie lokalnie webserwera 
Chcąc uruchomić lokalnie serwer musimy znajdować się w katalogu z plikiem o nazwie manage.py, upewnij się, że masz aktywowane środowisko wirtualne ```source env/bin/activate```
```shell
python manage.py runserver
```

Aby utworzyć aplikację, upewnij się, że jesteś w tym samym katalogu, co manage.py i wpisz to polecenie:
```shell
python manage.py startapp todoapp
```

### Migracje

Stworzenie bazy danych wraz z tabelami 
```shell
python manage.py migrate
```

Stworzenie pliku migracji, np po dodaniu nowego modelu 
```shell
python manage.py makemigrations todoapp
```

Wykonanie migracji z stworzonego pliku do bazy danych 
```shell
python manage.py migrate todoapp
```

### Interaktywna powłoka Pythona

wejście
```shell
python manage.py shell
```

#### Dodanie do bazy danych rekordów

Dodaj rekord do tabeli bez relacji. 

* Importuj model ```from todoapp.models import ToDoList, Item```
* t = ToDoList(name="Tims List")
* t.save()
* ToDoList.objects.all()
* ToDoList.objects.get(id=1)
* ToDoList.objects.get(name="Tims List")

Dodaj rekord do tabeli z relacją.
* t.item_set.all()
* t.item_set.create(text="Go to the mall", complete=False)
* t.item_set.get(id=1)

exit()

#### Dodaki do interaktywnej powłoki 

```shell
pip install django-extensions
```
Konfiguracja. Będziesz musiał dodać aplikację django_extensions do ustawienia INSTALLED_APPS pliku settings.py

wejście
```shell
python manage.py shell_plus
```

Instalacja IPython

```shell
pip install ipython
```

wejście
```shell
python manage.py shell_plus --ipython
```
todolist = Todo.objects.all()

todolist = Todo.objects.get(id=1)

todolist = Todo.objects.filter(id=1)

todolist = Todo.objects.filter(id__gt=3)

todolist = Todo.objects.filter(id__lt=3)

todolist = Todo.objects.filter(id__lte=3)

todolist = Todo.objects.filter(created__year=2022)

todolist = Todo.objects.filter(created__day=3)

todolist = Todo.objects.filter(important__isnull=True)

todolist = Todo.objects.filter(title__contains="do")

todolist = Todo.objects.filter(title__startswith="No")

todolist = Todo.objects.filter(title__iendswith="pi")

todolist = Todo