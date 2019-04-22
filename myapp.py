
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
app =Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how are you")
def hello():
    return "I am good, how about you?"
    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=9988)

