# План рефакторинга

После анализа кода решили внести следующие изменения в src/main.py для улучшения его качества:

1. Заменить переменную min_lenght на константу MIN_LENGTH_DEFAULT
2. Переименовать функцию summ на summarize_text
3. Переименовать аргумент articleInput на argument_input
4. Возвращаемое значение функции summarizedArticle переименовать  на summarized_article
5. Название экземпляра ifrace переименовать на interface
6. Переменные min_length_of_article и max_length_of_article переименовать в min_length и max_length соответственно
