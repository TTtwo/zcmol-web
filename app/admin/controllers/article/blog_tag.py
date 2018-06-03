from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from app.kernel.utils.response import resp_to_json

from datetime import datetime

from webargs import fields
from webargs import ValidationError
from webargs.flaskparser import use_kwargs

from flask_restful import Resource


class BlogTagValidate:
    @staticmethod
    def validate_tag_name(tag_name):
        if Model.BlogTag.query.filter_by(tag_name=tag_name).first():
            raise ValidationError('tag_name {} was exist!'.format(tag_name))


class BlogTag(Resource):

    @use_kwargs({})
    def get(self):
        query: list[Model.BlogTag] = Model.BlogTag.query.all()
        items = [
            ModelHelper.serialize(item)
            for item in query
        ]
        return resp_to_json(items=items)

    @use_kwargs({
        'hidden': fields.Bool(missing=False),
        'tag_name': fields.Str(max=32,
                               validate=BlogTagValidate.validate_tag_name)
    })
    def post(self, hidden, tag_name):
        params = {
            '_hidden': hidden,
            'tag_name': tag_name,
            'change_at': datetime.now()
        }
        if Model.BlogTag.query.filter_by(tag_name=tag_name).first():
            return 'tag_name {} was exists !'.format(tag_name), 2001
        tag: Model.BlogTag = Model.BlogTag(**params)
        DB.session.add(tag)
        DB.session.commit()
        return 201


class BlogTagDetail(Resource):
    @use_kwargs({
        'hidden': fields.Bool(missing=False),
        'tag_name': fields.Str(max=32,
                               validate=BlogTagValidate.validate_tag_name)
    })
    def patch(self, blog_tag_id, hidden, tag_name):
        tag: Model.BlogTag = Model.BlogTag.query.get(blog_tag_id)
        if tag is None:
            return 'blog_tag_id {} is not exits'.format(blog_tag_id)
        if tag_name:
            tag.tag_name = tag_name
        tag._hidden = hidden
        tag.change_at = datetime.now()
        DB.session.commit()
        return 201
