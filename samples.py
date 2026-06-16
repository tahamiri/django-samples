books = Book.objects.select_related("author")

for book in books:
    print(book.title, book.author.name)




articles = Article.objects.prefetch_related("tags")

for article in articles:
    print(article.title)

    for tag in article.tags.all():
        print(tag.name)