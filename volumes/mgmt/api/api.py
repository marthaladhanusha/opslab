from flask import Flask, request
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'SkyHigh Network Operations',
    'description': 'House Keeper Backend API\'s'
}
Swagger(app)
CONFIG = {'AMQP_URI': "amqp://shnops:shnpass@rabbitmq.opslab.local"}


@app.route('/compute', methods=['POST'])
def compute():
    """
    Micro Service Based Compute and Mail API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            operation:
              type: string
              enum:
                - sum
                - mul
                - sub
                - div
            email:
              type: string
            value:
              type: integer
            other:
              type: integer
    responses:
      200:
        description: Please wait the calculation, you'll receive an email with results
    """
    operation = request.json.get('operation')
    value = request.json.get('value')
    other = request.json.get('other')
    email = request.json.get('email')
    msg = "Please wait the calculation, you'll receive an email with results"
    subject = "API Notification"
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning and email notification
        rpc.mail.send.async(email, subject, msg)
        # asynchronously spawning the compute task
        result = rpc.compute.compute.async(operation, value, other, email)
        return msg, 200

@app.route('/confluence', methods=['POST'])
def confluencepublish():
    """
    Micro Service Based Confluence API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            operation:
              type: string
              enum:
                - sum
                - mul
                - sub
                - div
            email:
              type: string
            value:
              type: integer
            other:
              type: integer
    responses:
      200:
        description: Please wait the calculation, you'll receive an email with results
    """
    operation = request.json.get('operation')
    value = request.json.get('value')
    other = request.json.get('other')
    email = request.json.get('email')
    msg = "Please wait the calculation, you'll receive an email with results"
    subject = "API Notification"
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning and email notification
        rpc.mail.send.async(email, subject, msg)
        # asynchronously spawning the compute task
        result = rpc.compute.compute.async(operation, value, other, email)
        return msg, 200

@app.route('/exporttopdf', methods=['POST'])
def exporttopdf():
    """
    Micro Service Based Confluence API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            operation:
              type: string
              enum:
                - sum
                - mul
                - sub
                - div
            email:
              type: string
            value:
              type: integer
            other:
              type: integer
    responses:
      200:
        description: Please wait the calculation, you'll receive an email with results
    """
    operation = request.json.get('operation')
    value = request.json.get('value')
    other = request.json.get('other')
    email = request.json.get('email')
    msg = "Please wait the calculation, you'll receive an email with results"
    subject = "API Notification"
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning and email notification
        rpc.mail.send.async(email, subject, msg)
        # asynchronously spawning the compute task
        result = rpc.compute.compute.async(operation, value, other, email)
        return msg, 200

@app.route('/publishtoflowdock', methods=['POST'])
def publishtoflowdock():
    """
    Micro Service Based Confluence API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            operation:
              type: string
              enum:
                - sum
                - mul
                - sub
                - div
            email:
              type: string
            value:
              type: integer
            other:
              type: integer
    responses:
      200:
        description: Please wait the calculation, you'll receive an email with results
    """
    operation = request.json.get('operation')
    value = request.json.get('value')
    other = request.json.get('other')
    email = request.json.get('email')
    msg = "Please wait the calculation, you'll receive an email with results"
    subject = "API Notification"
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning and email notification
        rpc.mail.send.async(email, subject, msg)
        # asynchronously spawning the compute task
        result = rpc.compute.compute.async(operation, value, other, email)
        return msg, 200
        
@app.route('/pagerduty', methods=['POST'])
def pagerduty():
    """
    file: specifications/pagerduty_post.yml
    """
    operation = request.json.get('operation')
    value = request.json.get('value')
    other = request.json.get('other')
    email = request.json.get('email')
    msg = "Please wait the calculation, you'll receive an email with results"
    subject = "API Notification"
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning and email notification
        rpc.mail.send.async(email, subject, msg)
        # asynchronously spawning the compute task
        result = rpc.compute.compute.async(operation, value, other, email)
        return msg, 200
                
app.run(host='0.0.0.0', debug=True)