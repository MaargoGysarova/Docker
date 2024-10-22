import unittest
from my_app import app

class AppTestCase(unittest.TestCase):
    
    # Устанавливаем тестовый клиент Flask
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Тест: проверка, что приложение запускается и возвращает успешный статус
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Work!", response.data)
    
    # Тест: проверка подключения к базе данных (требует работающей базы)
    def test_db_connection(self):
        response = self.app.get('/db')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()


## python -m unittest discover -s . -p "test_*.py"

