from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from app.kernel.utils.response import resp_to_json

from datetime import datetime

from webargs import fields
from webargs import ValidationError
from webargs.flaskparser import use_kwargs

from flask_restful import Resource


class BlogCategoryValidate:
    @staticmethod
    def validate_category_name(category_name):
        if Model.BlogContentCategory \
                .query \
                .filter_by(category_name=category_name) \
                .first():
            raise ValidationError('tag_name {} was exist!'.format(category_name))


class BlogCategory(Resource):
    @use_kwargs({})
    def get(self):
        query: list[Model.BlogContentCategory] = Model \
            .BlogContentCategory \
            .query \
            .all()
        items = [
            ModelHelper.serialize(item)
            for item in query
        ]
        return resp_to_json(items=items)

    @use_kwargs({
        'hidden': fields.Bool(missing=False),
        'category_name': fields.Str(required=True,
                                    max=32,
                                    validate=BlogCategoryValidate.validate_category_name)
    })
    def post(self, hidden, category_name):
        params = {
            '_hidden': hidden,
            'category': category_name,
            'change_at': datetime.now()
        }
        category: Model.BlogContentCategory = Model.BlogContentCategory(**params)
        DB.session.add(category)
        DB.session.commit()
        return 201


class BlogCategoryDetail(Resource):

    @use_kwargs({
        'hidden': fields.Bool(missing=False),
        'category_name': fields.Str(required=True,
                                    max=32,
                                    validate=BlogCategoryValidate.validate_category_name)
    })
    def patch(self, blog_category_id, hidden, category_name):
        category: Model.BlogContentCategory = Model.BlogContentCategory.query.get(blog_category_id)
        if category is None:
            return 'blog_category_id {} is not exist'.format(blog_category_id)
        category._hidden = hidden
        if category_name:
            category.category_name = category_name
        category.change_at = datetime.now()
        DB.session.commit()
        return 201
