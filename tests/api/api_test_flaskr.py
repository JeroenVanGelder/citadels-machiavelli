import os
import tempfile
import unittest
import json
from machiavelli_webserver import webserver

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.app = webserver.test_client()
        pass

    def tearDown(self):
        print("teardown")
        del self.app
        pass

    def test_run(self):
        rv = self.app.get('/')
        assert b'play machiavelli' in rv.data

    def test_starting_state(self):
        rv = self.app.get('/state')
        jsonData = json.loads(rv.data)
        assert "StartingGameState" == jsonData["game_state"]

    def test_add_one_player(self):
        rv = self.app.get('/players')
        jsonData = json.loads(rv.data)
        print(jsonData)
        pass #assert "jeroen" == jsonData["player"][4]["name"]

    def test_add_four_remaining_players(self):
        self.add_user("robin")
        self.add_user("martijn")
        self.add_user("casper")
        self.add_user("sander")
        self.add_user("jeroen")
        rv = self.app.get('/players')
        jsonData = json.loads(rv.data)
        print(jsonData)
        pass
    
    def add_user(self, username):
        return self.app.post('/players',
            data=json.dumps(dict(name=username)),
            content_type='application/json')