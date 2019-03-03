from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Board, List, Label
from trello import views

#Create temporary user to login API
def setup_user():
    User = get_user_model()
    return User.objects.create_user(
        'test',
        email='testuser@test.com',
        password='test'
    )

# Test case class to Unittest /boards/
class TestBoard(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = views.BoardList.as_view()
        self.uri = '/boards/'
        self.user = setup_user()

    def test_boardlist(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create_board(self):
        self.client.login(username="test", password="test")
        params = {
            "name": "Test Board create",
            "is_active": 'true'
            }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(Board.objects.count(), 1)
        board = Board.objects.get(id=1)
        print("board_id = ",board)
        List.objects.create(name="Doing",cards_order=[], board=board, is_active=True)
        lis = List.objects.get(name="Doing", cards_order=[], board=board, is_active=True)
        self.assertEqual(List.objects.count(), 1)

# Test case class to Unittest /lists/
class TestList(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = views.ListList.as_view()
        self.uri = '/lists/'
        self.user = setup_user()

    def test_Listlist(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create_list(self):
        self.client.login(username="test", password="test")
        Board.objects.create(name="Test Board",is_active=True)
        board = Board.objects.get(id=3)
        params = {
                   "name": "Doing",
                   "cards_order": [],
                   "board":3,
                   "is_active":'true'
                }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

# Test case class to Unittest /cards/
class TestCard(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = views.CardList.as_view()
        self.uri = '/cards/'
        self.user = setup_user()

    def test_cardlist(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create_card(self):
        self.client.login(username="test", password="test")
        Board.objects.create(name="Test Board for Card",is_active=True)
        board = Board.objects.get(id=2)
        List.objects.create(name="Test List for Card",cards_order=[], board=board, is_active=True)
        Label.objects.create(name="Test Priority",is_active=True)
        lab = Label.objects.get(id=1)
        params = {
                "title": "test card 1",
                "list": 2,
                "Description": "Compete the test as expected",
                "Label": 1,
                "is_active": 'true'
                }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

# Test case class to Unittest /labels/
class TestLabel(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = views.LabelList.as_view()
        self.uri = '/labels/'
        self.user = setup_user()

    def test_labellist(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
