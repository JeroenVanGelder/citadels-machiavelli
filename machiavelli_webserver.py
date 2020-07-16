from flask import Flask, request, jsonify, abort, redirect, url_for, session
from machiavalli_game import MachiavelliGame
from player.playerDescriptions import PlayerDescription
from flask_marshmallow import Marshmallow
from functools import wraps
from marshmallow import (
    Schema,
    fields,
    validate,
    pre_load,
    post_dump,
    post_load,
    ValidationError,
)

webserver = Flask(__name__)
webserver.secret_key = "SUPERS3CR3T"
marsh = Marshmallow(webserver)
machiavelli_game = MachiavelliGame()

class PlayerSchema(marsh.Schema):
    class Meta:
        fields = ('name', 'position', 'gold')

        # We add a post_dump hook to add an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        key = "players" if many else "player"
        return {key: data}


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

@webserver.route('/', methods=['GET'])
def base_route():
    return "play machiavelli"

@webserver.route('/state', methods=['GET'])
def get_game_state():
    return jsonify({"game_state": machiavelli_game.getState()})

@webserver.route('/players', methods=['GET'])
def get_players():
    players = machiavelli_game.getAllPlayers()
    return players_schema.dump(players)

@webserver.route('/players', methods=['POST'])
def add_player():
    player_name = request.json['name']
    player = PlayerDescription(player_name)
    try:
        machiavelli_game.registerPlayer(player)
        added_player = machiavelli_game.getPlayer(player_name)
        return player_schema.jsonify(added_player)
    except ValueError:
        abort(400, "player already exists")
    except RuntimeError:
        abort(403, "action not allowed")

@webserver.route('/start', methods=['POST'])
def start_game():
    try:
        machiavelli_game.startGame()
        return redirect(url_for('get_game_state'))
    except RuntimeError:
        abort(403, "action nout allowed")

@webserver.route('/active/drafting', methods=['GET'])
def get_drafting_player():
    player = machiavelli_game.getDraftingPlayer()
    return player_schema.jsonify(player)


@webserver.route('/active/playing', methods=['GET'])
def get_playing_player():
    player = machiavelli_game.getCurrentPlayer()
    return player_schema.jsonify(player)

# run server
if __name__ == '__main__':
    webserver.run(debug=True)

