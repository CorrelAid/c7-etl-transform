import pickle as pkl

MAPPING = pkl.load(open("../data/mapping.pkl", "rb"))


def get_question_from_code(key: str) -> str:
    """

    :param: key shortened question id
    :return: full text question
    """
    return MAPPING[key]
