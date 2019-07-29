from ..model.db_exception import DatabaseException
from ..service.question_dao import QuestionDao


class ChoiceDao:
    collection_name = "questions"

    @staticmethod
    def get_by_id(q_id: str, c_id: int) -> dict:
        """
        Gets choice by question id and choice id.

        :param q_id: str of question id.
        :param c_id: int of choice id.
        :return: choice as dict.
        """
        c_list = QuestionDao.get_by_id(q_id).get('choices')
        try:
            return next((item for item in c_list if item['_id'] == c_id), None)
        except Exception as e:
            raise DatabaseException(e)

    @staticmethod
    def vote(q_id: str, c_id: int):
        """
        Votes for choice in question by its id.
        If "action" in body is "vote" - increase number of votes by 1.
        If "action" in body is "undo" - decrease number of votes by 1.

        :param q_id: question id.
        :param c_id: choice id.
        :return: question as dict.
        :raise: DatabaseException if question couldn't be updated.
        """
        ch_list = QuestionDao.get_by_id(q_id).get('choices')
        if c_id > len(ch_list):
            raise DatabaseException('No choice with this id')
        else:
            n_votes = ChoiceDao.get_by_id(q_id, c_id).get('votes')
            ch_list[c_id - 1].update({'votes': n_votes + 1})
            QuestionDao.update(q_id, {'choices': ch_list})

    @staticmethod
    def rate_choice(q_id: str, c_id: int, rate: float):
        """
        Rates choice in question by its id.

        :param q_id: question id.
        :param c_id: choice id.
        :param rate: new rate of choice.
        :return: question with choice's updated rate.
        """
        ch_list = QuestionDao.get_by_id(q_id).get('choices')
        if c_id > len(ch_list):
            raise DatabaseException('No choice with this id')
        else:
            rate_count = ch_list[c_id - 1].get('rate_count') + 1
            rate_ = ch_list[c_id - 1].get('rate') + rate
            ch_list[c_id - 1].update({'rate_count': rate_count})
            if rate_count > 2:
                ch_list[c_id - 1].update({'rate': round((rate_ / 2), 2)})
            else:
                ch_list[c_id - 1].update({'rate': round((rate_ / rate_count), 2)})
            QuestionDao.update(q_id, {'choices': ch_list})
