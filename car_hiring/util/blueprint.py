# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint as FlaskBlueprint


class AppBlueprint(FlaskBlueprint):

    def GET(self, *varg, **kwargs):
        kwargs['methods'] = ['GET']
        return self.route(*varg, **kwargs)

    def POST(self, *varg, **kwargs):
        kwargs['methods'] = ['POST']
        return self.route(*varg, **kwargs)

    def PUT(self, *varg, **kwargs):
        kwargs['methods'] = ['PUT']
        return self.route(*varg, **kwargs)

    def DELETE(self, *varg, **kwargs):
        kwargs['methods'] = ['DELETE']
        return self.route(*varg, **kwargs)
