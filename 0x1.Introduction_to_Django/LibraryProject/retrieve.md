**retrieve.md**
```markdown
# Retrieve Operation

**Command:**
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)

"1984 by George Orwell, published in 1949"