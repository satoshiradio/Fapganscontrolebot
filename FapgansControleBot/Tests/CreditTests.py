import unittest

from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Repository.unit_of_work import UnitOfWork


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.unit_of_work: IUnitOfWork = UnitOfWork(database_uri="sqlite://")

    def test_starting_fills_end_time(self):
        credit: Credit = Credit(70000)
        self.unit_of_work.get_credit_repository().add(credit)
        self.unit_of_work.complete()
        self.assertIsNone(credit.end_time)
        credit.start()
        self.assertIsNotNone(credit.end_time)

    def test_inserting_inserts_1(self):
        self.unit_of_work.get_credit_repository().add(Credit(70000))
        self.unit_of_work.complete()
        self.assertEqual(len(self.unit_of_work.get_credit_repository().all()), 1)

    def test_credit_can_be_activated(self):
        credit = Credit(70000)
        self.unit_of_work.get_credit_repository().add(credit)
        self.unit_of_work.complete()
        self.assertFalse(credit.is_active)
        credit.start()
        self.assertTrue(credit.is_active)

    def test_get_active_credit(self):
        credit = Credit(70000)
        self.unit_of_work.get_credit_repository().add(credit)
        self.unit_of_work.complete()
        credit.start()
        self.assertEqual(self.unit_of_work.get_credit_repository().active_gans_periods(), credit)


if __name__ == '__main__':
    unittest.main()
