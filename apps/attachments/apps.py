from django.apps import AppConfig


class AttachmentsConfig(AppConfig):
    name = 'attachments'
    verbose_name = "附件管理"

    def ready(self):
        import attachments.signals.file_handler
