import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_python_part_2')))
from task_read_write_2 import write_files, generate_words
import os

def test_write_files(tmpdir):
    file1_path = os.path.join(tmpdir, 'file1.txt')
    file2_path = os.path.join(tmpdir, 'file2.txt')

    words = ['abc', 'def', 'xyz']

    write_files(file1_path, file2_path, words)

    with open(file1_path, 'r', encoding='utf-8') as f1:
        content_file1 = f1.read()
    assert content_file1 == "abc\ndef\nxyz"

    with open(file2_path, 'r', encoding='cp1252') as f2:
        content_file2 = f2.read()
    assert content_file2 == "xyz,def,abc"

def test_generate_words():
    words = generate_words(5)
    assert len(words) == 5 
    for word in words:
        assert 3 <= len(word) <= 10  