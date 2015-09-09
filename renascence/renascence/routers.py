class DjangoRouter(object):
    django_apps = ["auth", "sessions", "contenttypes", "admin", "migrations"]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.django_apps:
            return 'django'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.django_apps:
            return 'django'
        return None
