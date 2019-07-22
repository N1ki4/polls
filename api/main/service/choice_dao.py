from api.main.model.db_exception import DatabaseException
from api.main.model.mongodb import Database
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
    def vote(q_id: str, c_id: int):
        """
        Add plus 1 to the vote field of the choice.

        :params - question ID, choice ID
        :return updated vote field of choice
        """
        choice = ChoiceDao.get_by_id(q_id, c_id)
        data = {'choices.$': {'_id': choice['_id'], 'text': choice['text'],
                              'votes': choice['votes'] + 1}}
        print('Choice:', choice)
        print('Data:', data)
        result = Database.update_one(QuestionDao.collection_name, q_id, data,
                                     extra_params={
                                         'choices._id': choice['_id']})
        if result:
            print('Result:', result)
            # result['_id'] = str(result['_id'])
            return result
        else:
            raise DatabaseException

    # @staticmethod
    # def vote(q_id: str, c_id: int, json_data: dict) -> dict:
    #     choice = ChoiceDao.get_by_id(q_id, c_id)
    #     question = QuestionDao.get_by_id(q_id)
    #     if json_data.get('action') == 'vote':
    #         n_votes = choice.get('votes')
    #         choice.update({'votes': n_votes + 1})
    #         q_list = question.get('choices')
    #         for ch in q_list:
    #             ch.update()
    #         # print(choice)
    #         # votes = (question.get('choices')[choice.get('_id') - 1])
    #         # print(QuestionDao.update(q_id, {votes['votes']: n_votes + 1}))
    #         return choice
