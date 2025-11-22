from flask import Flask, render_template, request, jsonify,  redirect
from manager.urlStrGenerator import generateKey
from manager.global_urls import dictionary, serverURL

app = Flask(__name__)

# @app.route("/")
# def uri():
#     return jsonify(dic)

@app.route("/<key>")
def redirect_url(key):
    original = dictionary.get(key)
    if original:
        return redirect(original)
    return jsonify({"message": "Invalid URL"}), 404


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        link = request.form.get("url")
        key = generateKey()

        try:
            dictionary[key] = link

            print(dictionary)
            print("Original URL:", link)
            print("Generated Key:", key)

            short_url =  serverURL + key

            return jsonify({"url": short_url}), 200
        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "something went wrong"}), 500
    else:
        return jsonify({"message": "method not allowed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
