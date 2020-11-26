# coding=utf-8
import datetime
import logging
import time

from app.faker_data.books import Faker
from app.repo.book import ElasticBookRepository

__author__ = 'team16'
_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    faker = Faker()
    es = ElasticBookRepository()
    es.create_index_if_not_exist()
    start = time.time()
    for bash in range(10):
        books = [faker.book() for i in range(10)]
        es.store_all(books, chunk_size=10000)
        print("Insert completely {} books in {} seconds".format((bash + 1) * 1000, time.time() - start))
