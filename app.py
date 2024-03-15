from flask import Flask, render_template, request, jsonify
import game

app = Flask(__name__, static_url_path='/static')  # Set static folder path

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/play")
def play():
  game_state = game.start_game()
  return render_template("game.html", game_state=game_state)

@app.route("/update_game", methods=["POST"])
def update_game():
  current_state = request.get_json()
  updated_state = game.run_game_loop(current_state)
  if game.is_game_over():
    # Send game over state
    return jsonify({"game_over": True})
  else:
    # Send updated state
    return jsonify(updated_state)

if __name__ == "__main__":
  app.run(debug=True)
