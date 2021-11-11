from Bot.Repository.i_unit_of_work import IUnitOfWork
from Bot.Repository.unit_of_work import UnitOfWork


def main():
    unit_of_work: IUnitOfWork = UnitOfWork()


if __name__ == "__main__":
    main()
