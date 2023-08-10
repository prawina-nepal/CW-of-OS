import unittest
from main import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system= FileSystem()
        
    def test_create_file(self):
        self.assertEqual(self.file_system.create_file("file1.txt"), None)
        self.assertEqual(self.file_system.create_file("file1.txt"), "File already exists")
        
    def test_read_file(self):
        self.file_system.create_file("file1.txt", "File content")
        self.assertEqual(self.file_system.read_file("file1.txt"), "File content")
        self.assertEqual(self.file_system.read_file("nonexistent.txt"), "File not found")
        
    def test_write_file(self):
        self.file_system.write_file("file1.txt", "New content")
        self.assertEqual(self.file_system.read_file("file1.txt"), "New content")
        self.file_system.write_file("file2.txt", "Content for new file")
        self.assertEqual(self.file_system.read_file("file2.txt"), "Content for new file")
        
    def test_create_directory(self):
        self.assertEqual(self.file_system.create_directory("dir1"), None)
        self.assertEqual(self.file_system.create_directory("dir1"), "Directory already exists")
        
    def test_change_directory(self):
        self.assertEqual(self.file_system.change_directory("dir1"), "Directory not found")
        self.file_system.create_directory("dir1")
        self.assertEqual(self.file_system.change_directory("dir1"), None)
        
    def test_list_directory(self):
        self.file_system.create_file("file1.txt")
        self.file_system.create_directory("dir1")
        subdirs, files = self.file_system.list_directory()
        self.assertIn("file1.txt", files)
        self.assertIn("dir1", subdirs)

if __name__ == '__main__':
    unittest.main()
