#Данные об email-адресах студентов хранятся в словаре: {домен:логины} . Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен
emails = {'rea.ru': ['misha', 'pasha'],
'study.com': ['olga', 'nastay', 'igor']}
print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep = '\n')