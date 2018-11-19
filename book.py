# -*- coding:utf-8 -*-
"""
@Time   : 2018/11/19 19:25
@Author : zhaoguoqing600689
"""
from flask import *
from .models import Book
from .forms import BookForm

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/new', methods=['GET', 'POST'])
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('book.list_books'))
    return render_template('baseFormEdit.html', form=form, title='new book')


# @bp.route('/all')
# # @app.route('/books/<int:page>')
# def list_books():
#     books = [b.title for b in Book.query.all()]
#     return jsonify(books)

@bp.route('/all')
@bp.route('/all/<int:page>')
def list_books(page=1):
    title = u'Books list'
    pagination = Book.query.paginate(page=page, per_page=5)
    return render_template('book/showAll.html', pagination=pagination, title=title)


@bp.route('/delete/<id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    book.remove()
    return redirect(url_for('book.list_books'))


@bp.route('/edit/<id>')
def edit_book(id):
    book = Book.query.get(id)
    form = BookForm(document=book)
    return render_template('baseFormEdit.html', form=form, book=book, title='edit book')


@bp.route('/edit/<id>', methods=['POST'])
def update_book(id):
    book = Book.query.get(id)
    form = BookForm()
    if form.validate_on_submit():
        form.instance = book
        form.save()
        return redirect(url_for('book.list_books'))
    form = BookForm(document=book)
    return render_template('baseFormEdit.html', form=form, book=book, title='edit book')
