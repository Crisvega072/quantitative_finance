import pandas as pd
import numpy as np
from modules.financials_functions import portfolio_volatility, portfolio_returns, VaR 
from modules.backend import tickers_by_issuer


if __name__ == "__main__": 

    #obetener tickers de ishares 
    tickers = tickers_by_issuer(issuer="iShares")

    #potafolio de renta fija 
    tickers_rf = tickers[tickers["CATEGORIA"] == "ETF RF"]
    list_tickers_rf = list(tickers_rf["TICKER"])

    #portafolio de renta variable 
    tickers_rv = tickers[tickers["CATEGORIA"]== "ETF RV"]
    list_tickers_rv = list(tickers_rv["TICKER"])

    #rango de fechas (menos años "corto plazo", mas años "historico")
    start= "2024-01-01"
    end = "2024-12-31"

    #nivel de confianza  (99% extremo 95% datos atipicos)
    confidence= 0.05
    lst= []

    for portafolio in [list_tickers_rf, list_tickers_rv]: 
        print(portafolio)

        #obtener retornos 
        df = portfolio_returns(tickers = portafolio, start=start, end=end)
        print(df.head(5))

        vector_w = np.array([1/len(portafolio)] * len(portafolio))
        print(vector_w)

        #calcular volatilidad
        sigma = portfolio_volatility(df=df, vector_w=vector_w)
        print(sigma)

        #calcular VaR 
        var = VaR(sigma=sigma, confidence=confidence)
        var = np.abs(var)
        var_mensual = var * np.sqrt(20)
        lst.append(var_mensual)
        print(var)

    df_final = pd.DataFrame(
        {
            "PORTAFOLIO": ["Ishares Renta Fija", "Ishares Renta Variable "],
            f"Value At Risk: {1-confidence}%" : lst 

        }
    )
    df_final = df_final.sort_values(
        by=f"Value At Risk: {1-confidence}%",
        ascending= False)
    print(df_final)





