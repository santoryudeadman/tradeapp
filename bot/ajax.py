import pickle
from flask import Flask, request, jsonify
from query_data import get_chain2

app = Flask(__name__)

# Load vectorstore and create QA chain
with open("vectorstore.pkl", "rb") as f:
    vectorstore = pickle.load(f)
qa_chain = get_chain2(vectorstore)
chat_history = []

@app.route("/")
def index():
    return """
    <html>
      <head>
        <title>AJAX Post Request Example</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
      </head>
      <body>
        <h1>Ask a Question</h1>
        <div>
          <label for="question">Question:</label>
          <input type="text" id="question" name="question">
          <button id="submit">Submit</button>
        </div>
        <div id="result"></div>
        <script>
          // Send the AJAX post request using jQuery
          $('#submit').click(function() {
            var question = $('#question').val();
            $.ajax({
              type: 'POST',
              url: '/ajax',
              data: { question: question },
              success: function(response) {
                // Display the response from the server
                $('#result').html('Answer: ' + response);
              },
              error: function(xhr, status, error) {
                // Handle errors
                console.log(error);
              }
            });
          });
        </script>
      </body>
    </html>
    """

@app.route("/ajax", methods=["POST"])
def ajax():
    # Get the question from the AJAX post request
    question = request.form.get("question")
    # Use the QA chain to get the answer
    result = qa_chain({"question": question, "chat_history": chat_history})
    chat_history.append((question, result["answer"]))
    response = jsonify(result["answer"])
    response.headers.add('Access-Control-Allow-Origin', '*')

    # Return the answer as a JSON response
    return response

if __name__ == "__main__":
    app.run(debug=True, port=3535)

