# coding=utf-8
import logging

from app.repo.book import ElasticBookRepository

__author__ = 'team16'
_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    es = ElasticBookRepository()
    es.create_index_if_not_exist()
