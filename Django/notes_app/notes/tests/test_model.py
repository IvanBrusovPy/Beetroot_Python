from unittest import TestCase

from notes_app.notes.models import Job


class JobTestCase(TestCase):
    def setUp(self) -> None:
        self.job_seo = Job.objects.create(title=1, min_saary = 200, max_salary=500)

    def test_salary_range(self):
        ceo = Job.objects.get(id=self.job_seo.id)
        self.assertEquals(ceo.get_salary_range(), f"{self.job_seo.max_salary -self.job_seo.mix_salary}")