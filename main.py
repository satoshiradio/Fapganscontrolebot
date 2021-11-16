import logging

from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Repository.unit_of_work import UnitOfWork
from FapgansControleBot.fapgans_controle_bot import FapgansControleBot


def main():
    logging.basicConfig(format='%(asctime)s - %(name)12s - %(levelname)s - %(message)s', level=logging.INFO)
    unit_of_work: IUnitOfWork = UnitOfWork()
    bot: FapgansControleBot = FapgansControleBot(unit_of_work)


if __name__ == "__main__":
    main()
