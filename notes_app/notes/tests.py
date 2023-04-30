from django.test import TestCase
from notes.models import Notes, Categories


class CreateNoteTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(title='Test Category')

    def test_create_valid_note(self):
        note = Notes.objects.create(
            title='Test Note',
            text='This is a test note',
            reminder='test',
            category=self.category
        )
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.text, 'This is a test note')
        self.assertEqual(note.reminder, 'test')
        self.assertEqual(note.category, self.category)

    def test_create_invalid_note(self):
        with self.assertRaises(Exception):
            Notes.objects.create(
                title='Test Note',
                text='This is a test note',
                category='invalid_category'
            )


class UpdateNoteTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(title='Test Category')
        self.note = Notes.objects.create(
            title='Test Note',
            text='This is a test note',
            reminder='test',
            category=self.category
        )

    def test_update_note_valid(self):
        self.note.title = 'Updated Note Title'
        self.note.text = 'Updated note text'
        self.note.reminder = 'updated'
        self.note.category = Categories.objects.create(title='Updated Category')
        self.note.save()

        updated_note = Notes.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Note Title')
        self.assertEqual(updated_note.text, 'Updated note text')
        self.assertEqual(updated_note.reminder, 'updated')
        self.assertEqual(updated_note.category.title, 'Updated Category')

    def test_delete_note_valid(self):
        note_id = self.note.id
        self.note.delete()
        with self.assertRaises(Notes.DoesNotExist):
            Notes.objects.get(id=note_id)
