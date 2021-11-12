import unittest

from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Repository.unit_of_work import UnitOfWork


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.unit_of_work: IUnitOfWork = UnitOfWork(database_uri="sqlite://")

    def test_inserting_inserts_1(self):
        self.unit_of_work.get_credit_repository().add(Credit(70000))
        self.unit_of_work.complete()
        self.assertEqual(len(self.unit_of_work.get_credit_repository().all()), 1)

    def test_starting_fills_end_time(self):
        credit: Credit = Credit(70000)
        self.unit_of_work.get_credit_repository().add(credit)
        self.unit_of_work.complete()
        self.assertIsNone(credit.end_time)
        credit.start()
        self.assertIsNotNone(credit.end_time)


if __name__ == '__main__':
    unittest.main()
