from unittest import TestCase

from dumper.configuration.api_config import APIConfig
from dumper.configuration.fs_config import FSConfig
from dumper.configuration.kafka_producer_config import KafkaProducerConfig


class TestParseFromLines(TestCase):

    def test_api_parse_from_lines(self):
        lines = [
            "API_host   :   some.api.com",
            "api_KEY : 12xf-yyy2-xxxx-As4g"
        ]
        actual = APIConfig.parse_from_lines(lines)
        expected = APIConfig("12xf-yyy2-xxxx-As4g", "some.api.com")

        self.assertEqual(actual, expected, "API Configs are not equal")

    def test_fs_parse_from_lines(self):
        lines = [
            "Dir   :  /users/hdfs/dumper/test_out/ ",
            "Host : 10.0.2.5:8088"
        ]
        actual = FSConfig.parse_from_lines(lines)
        expected = FSConfig("/users/hdfs/dumper/test_out/", "10.0.2.5:8088")
        self.assertEqual(actual, expected, "FS Configs are not equal")

    def test_kafka_parse_from_lines(self):
        lines = [
            "SERVERS : localhost:9092,kafka:9092",
            "CLIENT_ID : some_client_id"
        ]
        actual = KafkaProducerConfig.parse_from_lines(lines)
        expected = KafkaProducerConfig("localhost:9092,kafka:9092",
                                       "some_client_id",
                                       lambda v: v.encode("utf-8"),
                                       lambda v: v.encode("utf-8"),
                                       1,
                                       None,
                                       0,
                                       16384,
                                       1048576,
                                       30000,
                                       "PLAINTEXT")
        self.assertEqual(actual, expected, "Kafka Configs are not equal")

    def test_kafka_parse_from_lines1(self):
        lines = [
            "SERVERS : localhost:9092,kafka:9092",
            "CLIENT_ID : some_client_id",
            "Acks : 2",
            "MAX_request_SIZE : 1024"
        ]
        actual = KafkaProducerConfig.parse_from_lines(lines)
        expected = KafkaProducerConfig("localhost:9092,kafka:9092",
                                       "some_client_id",
                                       lambda v: v.encode("utf-8"),
                                       lambda v: v.encode("utf-8"),
                                       2,
                                       None,
                                       0,
                                       16384,
                                       1024,
                                       30000,
                                       "PLAINTEXT")
        self.assertEqual(actual, expected, "Kafka Configs are not equal")