from django.apps import AppConfig


class ContentsConfig(AppConfig):
    name = 'contents'
    verbose_name = "内容管理"

    def ready(self):
        import contents.signals
