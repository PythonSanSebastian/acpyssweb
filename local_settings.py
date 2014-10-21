
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "efcf4de7-51f7-467a-93c3-f5d1ee210c2a2bbd2abe-f4f7-4abb-a421-c1f8a1c5da96a40eb47f-6f26-4023-9190-75c03a44fe2e"
NEVERCACHE_KEY = "5db37f1c-3af2-433a-bbdf-196a23473ed63647c771-96b2-4701-aca5-3c50e6003428ae691916-00f6-40ce-87f1-4c7433a3ea9c"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
