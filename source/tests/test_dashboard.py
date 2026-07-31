import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
import pandas as pd
from dashboard import total_por_categoria


class TestDashboard(unittest.TestCase):
    def test_total_por_categoria(self):
        dados_teste = {
            'Categoria': ['Lazer', 'Lazer', 'Mercado', 'Mercado', 'Lazer', 'Saúde'],
            'Valor': [50, 30, 100, 200, 150, 80]
        }
        df_teste = pd.DataFrame(dados_teste)

        resultado = total_por_categoria(df_teste)

        self.assertEqual(resultado['Lazer'], 230)
        self.assertEqual(resultado['Mercado'], 300)
        self.assertEqual(resultado['Saúde'], 80)


if __name__ == '__main__':
    unittest.main()