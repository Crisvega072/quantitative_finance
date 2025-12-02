import pandas as pd
import numpy as np
import scipy.stats as stats
from .backend import market_prices

def portfolio_volatility(
        df:pd.DataFrame,
        vector_w:np.array
        ) -> float:
   '''
   Calculo de la volatlidad de un portafolio
   de inversiones

    df (pd.DataFrame):
        Dataframe de Retornos del portafolio.
    vector_w (np.array)
        vector de pesos de los instrumentos del portafolio

    Return (float): volatlidad del portafolio
    '''
   
   # matriz varianza covarianza
   m_cov = df.cov()

   # vector transpuesto
   vector_w_t = np.array([vector_w])

   # varianza
   vector_cov = np.dot(m_cov,vector_w_t)
   varianza = np.dot(vector_cov,vector_w)

   # volatilidad
   vol = np.sqrt(varianza)

   return vol






