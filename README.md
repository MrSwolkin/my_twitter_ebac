# my_twitter_ebac

## Descrição
Projeto de conclusão do curso Ebac Full stack Pyhthon. O projeto é uma replica da rede social Twitter. 


## Pré-requisitos
```
Python 3.10
poetry
```

## Execução

1. Clone o projeto: 
    ```shell
    git clone https://github.com/MrSwolkin/my_twitter_ebac.git

    ```

2. Instale as dependências:
    ```shell
    cd my_twitter
    poetry install
    ``` 

3. Criando as migrações:
    ```shell
    poetry run python manage.py makemigrations
    ````

4. Sincronizando banco de dados: 
    ```shell
    poetry run manage.py migrate
    ```

5. Criando superusuário (admin):
    ```shell
    poetry ru python manage.py createsuperuser 
    ````

6. Inicie o Localserver:
    ```shell
    poetru run python manage.py runserver
    ```

