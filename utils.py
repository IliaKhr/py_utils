import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s.%(msecs)03d - [%(levelname)s] %(name)s [%(module)s.%(funcName)s:%(lineno)d]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False


def fast_df_apply(df, func):
    """
    df <- датафрейм (срез колонок), к которому применяется функция
    func <- python callableы, функция, которую необходимо применить к датафрейму
    """
    cols = list(df.columns)
    data, index = [], []
    for row in df.itertuples(index=True):
        row_dict = {f:v for f,v in zip(cols, row[1:])}
        data.append(func(row_dict))
        index.append(row[0])

    return pd.Series(data, index=index)

logger.info('Библиотека импортирована')