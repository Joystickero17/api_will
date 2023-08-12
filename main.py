from flask import Flask, request,render_template_string, render_template
from datetime import datetime
from weasyprint import HTML
from send_email_module import send_email

app = Flask(__name__)



@app.route("/generate_pdf", methods=['GET', 'POST'])
def generate_pdf():
    data = request.get_json()
    str_template = render_template("receipt.html", **{"order":data})
    byte_data = HTML(string=str_template).write_pdf()
    content="""
        <h1>Gracias por tu compra!</h1>
        <br>
        <p>Nos complace anunciarte que tu compra ha sido exitosa, acontinuacion se adjunta el recibo generado</p>

        <p>Atentamente,</p>
        <p>Swift Store</p>
        """
    send_email(data['user']['email'], content, "Gracias por tu compra",{"name":"Recibo {}.pdf".format(data['id']),"file":byte_data})
    return {
        "result":"Factura enviada con éxito"
                }