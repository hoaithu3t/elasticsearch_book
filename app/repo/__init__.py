# coding=utf-8
import logging

import elasticsearch.helpers
from elasticsearch import Elasticsearch

__author__ = 'team16'
_logger = logging.getLogger(__name__)


def get_update_body_query(data):
    return {
        "doc": data,
        "doc_as_upsert": True
    }


class EsRepoInterface:
    def __init__(self):
        self.es = Elasticsearch("http://localhost:9200")
        self._index = None
        self.id_key = ''
        self.settings = {}
        self.mappings = {}

    def create_index_if_not_exist(self):
        """
        :return:
        """
        if not self.es.indices.exists(index=self._index):
            self.es.indices.create(self._index, body=dict(
                settings=self.settings, mappings=self.mappings))
        self.es.indices.put_mapping(index=self._index, body=self.mappings)

    def store(self, data, get_body_query_func=get_update_body_query):
        """
        index dữ liệu đơn lẻ vào elastic search
        :param data: EsData
        :param get_body_query_func: function
        :return:
        """
        _id = data.get(self.id_key)
        body = get_body_query_func(data)
        if self.es.indices.exists(index=self._index):
            res = self.es.update(index=self._index,
                                 id=_id, body=body, retry_on_conflict=5)
            return res
        else:
            raise Exception('Index not exist')

    def store_all(self, list_data, get_body_query_func=get_update_body_query,
                  chunk_size=100):
        """
        Bulk index list data to elastic search
        :param list_data: EsData
        :param get_body_query_func: function
        :param chunk_size: int
        :return:
        """
        body = [
            {
                "retry_on_conflict": 5,
                "_op_type": "update",
                "_id": data.get(self.id_key),
                **get_body_query_func(data)
            }
            for data in list_data
        ]
        if self.es.indices.exists(index=self._index):
            res = elasticsearch.helpers.bulk(self.es, body, index=self._index,
                                             chunk_size=chunk_size,
                                             max_retries=5
                                             )
            return res
        else:
            raise Exception('Index not exist')

    def get(self, _id):
        return self.es.get(self._index, _id).get("_source")

    def create_alias_index(self, alias_index):
        if not self.es.indices.exists(index=alias_index):
            self.es.indices.create(alias_index, body=dict(
                settings=self.settings, mappings=self.mappings))
        self.es.indices.put_mapping(index=alias_index, body=self.mappings)
        self.es.indices.update_aliases({
            "actions": [
                {"add": {"index": alias_index, "alias": self._index}}
            ]
        })

    def remove_alias_index_if_exist(self, alias_index):
        if self.es.indices.exists_alias(index=alias_index, name=self._index):
            self.es.indices.update_aliases({
                "actions": [
                    {"remove": {"index": alias_index, "alias": self._index}}
                ]
            })

    def remove_index_if_exist(self):
        if self.es.indices.exists(index=self._index):
            self.es.indices.delete(self._index)
