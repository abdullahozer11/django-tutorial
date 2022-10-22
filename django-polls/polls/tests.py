import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose `pub_date` is
        in the future.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose `pub_date` is
        older than 1 day.
        """
        old_time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=old_time)
        self.assertFalse(old_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose `pub_date` is
        withing the last day.
        """
        recent_time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        recent_question = Question(pub_date=recent_time)
        self.assertTrue(recent_question.was_published_recently())

def create_question(question_text, days):
    """
    Create a question with the given `question_test` and the number of `days`
    offset from the publication to now (negative for questions published in the
    past, positive for question that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        """
        Questions with a pub_date in the past are displayed on the index page.
        """
        question = create_question("Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )

    def test_future_questions(self):
        """
        Questions with a pub_date in the future aren't displayed on the index
        page.
        """
        create_question("Past question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_questions(self):
        """
        Even if both past and future questions exist, only past questions are
        displayed
        """
        past_question = create_question("Past question.", days=-30)
        create_question("Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_question]
        )

    def test_tow_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        past_question1 = create_question("Past question.", days=-30)
        past_question2 = create_question("Past question.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_question2, past_question1]
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future returns a
        404 not found.
        """
        future_question = create_question("Future question", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the
        question text.
        """
        past_question = create_question("Past question", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)