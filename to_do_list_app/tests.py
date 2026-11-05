from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Task
from .forms import TaskForm, TaskEditForm


class TaskModelTest(TestCase):
    """Test suite for the Task model."""

    def setUp(self):
        self.task = Task.objects.create(
            title="Complete Web Dev Assignment",
            description="Build CRUD functionality with Django",
            done=False
        )

    def test_task_creation(self):
        """Verify task attributes and defaults."""
        self.assertEqual(self.task.title, "Complete Web Dev Assignment")
        self.assertEqual(self.task.description, "Build CRUD functionality with Django")
        self.assertFalse(self.task.done)
        self.assertIsNotNone(self.task.created_at)

    def test_str_representation(self):
        """Verify string representation returns the title."""
        self.assertEqual(str(self.task), "Complete Web Dev Assignment")

    def test_created_property(self):
        """Verify formatted created string matches YYYY-MM-DD HH:MM."""
        expected = self.task.created_at.strftime('%Y-%m-%d %H:%M')
        self.assertEqual(self.task.created, expected)


class TaskFormsTest(TestCase):
    """Test suite for task forms."""

    def test_task_form_valid(self):
        form = TaskForm(data={'title': 'New Task', 'description': 'Some details'})
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_empty_title(self):
        form = TaskForm(data={'title': '', 'description': 'Missing title'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_task_edit_form_valid(self):
        form = TaskEditForm(data={'title': 'Updated Task', 'description': 'Updated details', 'done': True})
        self.assertTrue(form.is_valid())


class TaskViewsTest(TestCase):
    """Test suite for To-Do List views and CRUD workflow."""

    def setUp(self):
        self.client = Client()
        self.task1 = Task.objects.create(
            title="Maths Work1",
            description="Test Work1",
            done=True
        )
        self.task2 = Task.objects.create(
            title="Clean Desk",
            description="Organize workspace",
            done=False
        )

    def test_home_view(self):
        """Test home view renders correctly with tasks."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Maths Work1")
        self.assertContains(response, "Clean Desk")
        self.assertContains(response, "All Tasks")

    def test_home_view_empty_state(self):
        """Test home view shows empty state when no tasks exist."""
        Task.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks yet.")

    def test_add_task_get(self):
        """Test GET request to add task page."""
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_task.html')
        self.assertIsInstance(response.context['form'], TaskForm)

    def test_add_task_post(self):
        """Test creating a new task via POST."""
        response = self.client.post(reverse('add_task'), {
            'title': 'Submit Assignment',
            'description': 'Push repository to GitHub'
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Task.objects.filter(title='Submit Assignment').exists())
        created_task = Task.objects.get(title='Submit Assignment')
        self.assertFalse(created_task.done)

    def test_edit_task_get(self):
        """Test GET request to edit task page."""
        response = self.client.get(reverse('edit_task', args=[self.task2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_task.html')
        self.assertEqual(response.context['task'].id, self.task2.id)

    def test_edit_task_post(self):
        """Test updating an existing task via POST."""
        response = self.client.post(reverse('edit_task', args=[self.task2.id]), {
            'title': 'Clean Desk & Study Room',
            'description': 'Dust desk and sweep floor',
            'done': True
        })
        self.assertRedirects(response, reverse('home'))
        self.task2.refresh_from_db()
        self.assertEqual(self.task2.title, 'Clean Desk & Study Room')
        self.assertTrue(self.task2.done)

    def test_toggle_task(self):
        """Test toggling task completion status."""
        self.assertFalse(self.task2.done)
        response = self.client.post(reverse('toggle_task', args=[self.task2.id]))
        self.assertRedirects(response, reverse('home'))
        self.task2.refresh_from_db()
        self.assertTrue(self.task2.done)

        # Toggle back to pending
        response = self.client.post(reverse('toggle_task', args=[self.task2.id]))
        self.task2.refresh_from_db()
        self.assertFalse(self.task2.done)

    def test_delete_task(self):
        """Test deleting a task."""
        task_id = self.task1.id
        response = self.client.get(reverse('delete_task', args=[task_id]))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Task.objects.filter(id=task_id).exists())

    def test_404_for_nonexistent_task(self):
        """Test 404 is returned when modifying a nonexistent task."""
        response = self.client.get(reverse('edit_task', args=[99999]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse('delete_task', args=[99999]))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse('toggle_task', args=[99999]))
        self.assertEqual(response.status_code, 404)
