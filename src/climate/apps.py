from __future__ import unicode_literals

from django.apps import AppConfig
import app.main


class ClimateConfig(AppConfig):
    name = 'climate'
    
    def ready(self):
        model = self.get_model('Climate')
        app.main.ClimateApp(model).pullAtStartup()