from django.test import TestCase, Client
from notes.models import Category, Note


class MainTestCase(TestCase):
    def setUp(self) -> None:
        client = Client()

    def test_index_page(self):
        response = self.client.get("/index/")
        self.assertContains(response, 'Hello')


    metting = Category("meeting")
    metting.save()
    home = Category("home")
    home.save()
    work = Category("work")
    work.save()

    note_1 = Note(title="Meeting 1", text="prepare docs", reminder="Start at 10-00", category_id=metting)

