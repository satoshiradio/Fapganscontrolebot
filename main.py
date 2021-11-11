from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Repository.unit_of_work import UnitOfWork
from FapgansControleBot.fapgans_controle_bot import FapgansControleBot


def main():
    unit_of_work: IUnitOfWork = UnitOfWork()
    bot: FapgansControleBot = FapgansControleBot(unit_of_work)


if __name__ == "__main__":
    main()