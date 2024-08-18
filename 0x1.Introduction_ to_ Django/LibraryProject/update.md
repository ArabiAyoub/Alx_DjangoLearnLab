**update.md**
```markdown
# Update Operation

**Command:**
```python
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book)

"Nineteen Eighty-Four by George Orwell, published in 1949"