from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calcular_agua():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])

            if peso <= 0:
                return render_template('agua.html', erro="O peso deve ser maior que zero!")

            # Cálculo: 35 ml por kg de peso
            agua_ml = peso * 35
            agua_litros = agua_ml / 1000

            return render_template('agua.html',
                                   peso=peso,
                                   agua_ml=round(agua_ml, 1),
                                   agua_litros=round(agua_litros, 2))

        except ValueError:
            return render_template('agua.html', erro="Por favor, digite um peso válido!")

    return render_template('agua.html')


if __name__ == '__main__':
    app.run(debug=True)