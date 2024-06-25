def extract_transform_load(file):
    import pandas as pd
    
    df = pd.read_csv(file)
    df_cru = df.copy()

    # Meses em numeros para poupar memória
    df.loc[ df['Mês'] == 'Jan', 'Mês'] = 1
    df.loc[ df['Mês'] == 'Fev', 'Mês'] = 2
    df.loc[ df['Mês'] == 'Mar', 'Mês'] = 3
    df.loc[ df['Mês'] == 'Abr', 'Mês'] = 4
    df.loc[ df['Mês'] == 'Mai', 'Mês'] = 5
    df.loc[ df['Mês'] == 'Jun', 'Mês'] = 6
    df.loc[ df['Mês'] == 'Jul', 'Mês'] = 7
    df.loc[ df['Mês'] == 'Ago', 'Mês'] = 8
    df.loc[ df['Mês'] == 'Set', 'Mês'] = 9
    df.loc[ df['Mês'] == 'Out', 'Mês'] = 10
    df.loc[ df['Mês'] == 'Nov', 'Mês'] = 11
    df.loc[ df['Mês'] == 'Dez', 'Mês'] = 12

    # Algumas limpezas
    df['Valor Pago'] = df['Valor Pago'].str.lstrip('R$ ')
    df.loc[df['Status de Pagamento'] == 'Pago', 'Status de Pagamento'] = 1
    df.loc[df['Status de Pagamento'] == 'Não pago', 'Status de Pagamento'] = 0

    # Transformando em int tudo que der
    df['Chamadas Realizadas'] = df['Chamadas Realizadas'].astype(int)
    df['Dia'] = df['Dia'].astype(int)
    df['Mês'] = df['Mês'].astype(int)
    df['Valor Pago'] = df['Valor Pago'].astype(int)
    df['Status de Pagamento'] = df['Status de Pagamento'].astype(int)
    
    return df, df_cru

def new_func(file, pd):
    return pd.read_csv(file)





