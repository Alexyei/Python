import sys
import string

password = sys.stdin.readline()

password_len = len(password)

# третий аргумент заменяет переданный в качестве третьего аргумента символы на None,
# в результате данный символы будут удалены из строки. Символы из первого аргумента
# будут замененены соответствующими символами из второго, так же как и при вызове функциии
# maketrans с двумя аргументами. При вызове функции maketrans с олним аргументом ей передаётся словарь,
# ключами которого соответсвуют символы требующие замены,
# а значения символы на которые необходимо заменить данные символы.

if password_len < 10:
    sys.stdout.write("BAD")
elif password.lower().find('kaspersky') != -1:
    sys.stdout.write("BAD")
elif len(set(password)) <= 5:
    sys.stdout.write("BAD")
elif len(password) == len(password.translate(str.maketrans("", "", string.digits))):
    sys.stdout.write("BAD")
elif len(password) == len(password.translate(str.maketrans("", "", string.punctuation))):
    sys.stdout.write("BAD")
elif len(password) == len(password.translate(str.maketrans("", "", string.ascii_lowercase))):
    sys.stdout.write("BAD")
elif len(password) == len(password.translate(str.maketrans("", "", string.ascii_uppercase))):
    sys.stdout.write("BAD")
else:
    sys.stdout.write("GOOD")
