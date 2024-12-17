from django.core.management.base import BaseCommand
import subprocess
import sys


class Command(BaseCommand):
    help = 'Запускает сервер разработки с использованием Daphne'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('Установка requirements.txt...'))
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        except subprocess.CalledProcessError:
            self.stdout.write(self.style.ERROR('Ошибка при установке зависимостей.'))
            return

        # Выполнение миграций
        self.stdout.write(self.style.NOTICE('Выполнение миграций...'))
        try:
            subprocess.check_call([sys.executable, 'manage.py', 'migrate'])
        except subprocess.CalledProcessError:
            self.stdout.write(self.style.ERROR('Ошибка при выполнении миграций.'))
            return

        # Запуск Daphne в фоновом режиме
        self.stdout.write(self.style.NOTICE('Запуск сервера с использованием Daphne...'))
        command = ['daphne', '-b', '0.0.0.0', '-p', '8000', 'course_work.asgi:application']
        try:
            process = subprocess.Popen(command)
            self.stdout.write(self.style.SUCCESS('Сервер запущен.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при запуске Daphne: {e}'))
