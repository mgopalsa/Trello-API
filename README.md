# A Simple Trello-API functionalities using Django

# Installation
1. Install dependencies:
      ```
      cd Trello-API/
      pip install -r requirements.txt
      ```

2. Start your PostgreSQL server and create a database using the details found under `DATABASES` in `~/Trello-API/trelloapi/settings.py` :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'postgres',
        'USER': 'trellouser',
        'PASSWORD':'trellouser',
        'HOST':'localhost',
        'PORT': '5432',
    }
}
```
3. Run the project:
    * on http://localhost:8000
      ```
      cd Trello-API/trelloapi/
      python manage.py runserver
      ```
## Testing the APIs
> 1. http://localhost:8000/boards/
> 2. http://localhost:8000/lists/
> 3. http://localhost:8000/cards/
> 4. http://localhost:8000/labels/
> 5. http://localhost:8000/login/

## SWAGGER API DOC
  http://localhost:8000/swagger-docs/
  http://localhost:8000/docs/
  
## Detailed Description
Trello consists of the following constructs:
•	Boards, which can contain zero to many Lists
•	Lists, which can contain zero to many Cards
•	Cards, which have a mandatory Title and can include a number of optional parameters, including: Description, Due Date, Label and Members
•	Members, which can be assigned to a card 

Actions which can be performed on each item include:
•	Boards can be created, renamed and archived
•	Lists can be created, archived, renamed and reordered
•	Cards can be created, archived, renamed, reordered within a list, or moved to another list
•	Members can be created, renamed, archived and assigned to cards
•	Labels can be renamed and assigned to cards. Each card can only have one label


## Unit Test Framework
To run the tests ==> $ python manage.py test

Test cases are written for the following using the Django APIClient/APITestcase Frameworks.
1) Creation of Boards
2) Creation of Cards
3) Creation of Lists
4) Creation of Labels
4) Get the Boards/Cards and Lists URL successfully.
5) GET The labels URL successfully

