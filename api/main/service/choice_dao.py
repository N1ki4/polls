from api.main.model.db_exception import DatabaseException
from api.main.service.question_dao import QuestionDao


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
        return next((item for item in c_list if item['_id'] == c_id), None)

    @staticmethod
    def vote(q_id: str, c_id: int) -> dict:
        """
        Votes for choice in question by its id.
        If "action" in body is "vote" - increase number of votes by 1.
        If "action" in body is "undo" - decrease number of votes by 1.

        :param q_id: question id.
        :param c_id: choice id.
        :return: question as dict.
        :raise: DatabaseException if question couldn't be updated.
        """
        n_votes = ChoiceDao.get_by_id(q_id, c_id).get('votes')
        ch_list = QuestionDao.get_by_id(q_id).get('choices')
        ch_list[c_id - 1].update({'votes': n_votes + 1})
        result = QuestionDao.update(q_id, {'choices': ch_list})
        if result:
            return result
        else:
            raise DatabaseException
