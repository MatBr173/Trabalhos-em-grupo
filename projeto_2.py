# 1.0.0
from datetime import datetime
from typing import Any
from pathlib import Path
import sqlite3


TABLE_NAME = 'Produtos'
ROOT = Path(__file__).parent
SQL_FILE = ROOT / 'db.sqlite3'


class Product:
    def __init__(self, client: str | None = None, product: Any | None = None,
                 qtd: int | None = None,
                 price: float | None = None,
                 date: datetime | None = None):

        self._date = date
        self._client = client
        self._product = product
        self._qtd = qtd
        self._price = price

    @property
    def dateDefault(self):
        return self._date

    @dateDefault.setter
    def dateDefault(self, value):
        self._date = value

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value

    @property
    def qtd(self):
        return self._qtd

    @qtd.setter
    def qtd(self, value):
        self._qtd = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class ConfigProducts(Product):
    def getDate(self, editDate=None):
        print('Data padrão: Dia atual.')

        while True:
            answerToUserTheDate = input(
                'Quer mudar a data da venda? (s/n): ').lower().strip()

            if answerToUserTheDate in ['s', 'n']:
                break

            else:
                print('Opção não encontrada.')
                print('FAQ \n s = Sim \n n = Não')

        if answerToUserTheDate == 's':
            editDate = True

        if not editDate:
            self.dateDefault = datetime.today()

        else:
            while True:
                try:
                    year = int(input('Digite o ano da compra: '))
                    month = int(input('Digite o mês da compra (1-12): '))
                    day = int(input('Digite o dia da compra (1-31): '))
                    self.dateDefault = datetime(
                        year=year, month=month, day=day)

                    if self.dateDefault > datetime.today():
                        print('Não é possível registrar uma venda '
                              'com data futura.')
                        continue

                    break

                except ValueError:
                    print('Erro ao inserir a data. Por favor, '
                          'insira números válidos.')
                    continue

        formatDate = '%d/%m/%Y'
        self.date = self.dateDefault.strftime(formatDate)

        while True:
            continueOrCancel = input(
                f'A data será: {self.date}, '
                'deseja continuar? (s/n): ').lower().strip()

            if continueOrCancel in ['s', 'n']:
                break

            else:
                print('Não existe essa opção')
                continue

        if continueOrCancel == 's':
            return self.date

        else:
            while True:
                answerContinueOrNot = input(
                    'Deseja refazer a data? (s/n): ').lower().strip()

                if answerContinueOrNot in ['s', 'n']:
                    break

                else:
                    print('Opção não encontrada. (s/n)')

            if answerContinueOrNot == 's':
                return self.getDate()
            else:
                return None

    def addClient(self):
        while True:
            client = input('Digite o nome do cliente: ')
            confirm = input(
                f'Cliente: {client}, deseja prosseguir? (s/n): '
            ).lower().strip()

            if confirm in ['s', 'n']:
                break

            else:
                print('Não existe essa opção')
                continue

        if confirm == 's':
            return client

        elif confirm == 'n':
            remake = input(
                'Gostaria de refazer as informações do cliente (s/n): ')

            if remake == 's':
                return self.addClient()
            elif remake == 'n':
                return None

    def addProduct(self):
        try:
            nameProduct = input('Digite o nome do produto: ')

            priceProduct = float(input('Digite o preço do produto: '))

            qtdProduct = int(input('Digite a quantidade vendida: '))
        except ValueError:
            print('Digite apenas coisas validas')
            return

        return nameProduct, priceProduct, qtdProduct


class RegisterSales(ConfigProducts):
    def __init__(self, client: str | None = None, product: Any | None = None,
                 qtd: int | None = None, price: float | None = None,
                 date: datetime | None = None):
        super().__init__(client, product, qtd, price, date)

    def register(self):
        client = self.addClient()
        addProduct = self.addProduct()
        date = self.getDate()

        if addProduct is None:
            return

        try:
            product, price, qtd = addProduct
        except TypeError:
            return

        item = self.viewDict(client, product, price, qtd, date)

        sql = (
            f'INSERT INTO {TABLE_NAME} (cliente, produto, preco, qtd, data) '
            'VALUES (:client, :product, :price, :qtd, :date)'
        )

        try:
            cursor.execute(sql, item)
            connection.commit()
            print('Venda registrada com sucesso!')

        except sqlite3.Error as e:
            print(f'Erro ao registrar a venda: {e}')

        finally:
            cursor.close()
            connection.close()

    def viewDict(self, client=None, product=None,
                 price=None, qtd=None, date=None):

        return {
            'client': client,
            'product': product,
            'price': price,
            'qtd':  qtd,
            'date': date,
        }


def createTableIfNotExists():
    sql = (
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'cliente TEXT, '
        'produto TEXT, '
        'preco REAL, '
        'qtd INTEGER, '
        'data TEXT'
        ')'
    )
    cursor.execute(sql)
    connection.commit()
    return


def main():
    createTableIfNotExists()
    print('Processo de registro de venda iniciado')

    user = RegisterSales()
    user.register()


if __name__ == '__main__':

    connection = sqlite3.connect(SQL_FILE)
    cursor = connection.cursor()
    main()