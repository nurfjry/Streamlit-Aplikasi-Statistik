import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    st.title("Uji Korelasi dan Analisis Regresi Linear Sederhana")

    st.write("Masukkan nilai x dan y:")
    x_values = st.text_input("Nilai x (pisahkan dengan koma), nilai koma gunakan titik")
    y_values = st.text_input("Nilai y (pisahkan dengan koma), nilai koma gunakan titik")

    x_values = [float(x.strip()) for x in x_values.split(',')]
    y_values = [float(y.strip()) for y in y_values.split(',')]

    data = pd.DataFrame({'x': x_values, 'y': y_values})

    st.write("Data yang dimasukkan:")
    st.write(data)

    correlation = data['x'].corr(data['y'])
    st.write("Korelasi antara x dan y: {:.2f}".format(correlation))

    x = np.array(data['x']).reshape((-1, 1))
    y = np.array(data['y'])

    model = LinearRegression()
    model.fit(x, y)

    coefficient = model.coef_[0]
    intercept = model.intercept_

    st.subheader("Model Regresi:")
    st.write("y = {:.2f}x + {:.2f}".format(coefficient, intercept))

    predictions = model.predict(x)

    fig, ax = plt.subplots()
    ax.scatter(x, y, color='b', label='Data Asli')
    ax.plot(x, predictions, color='r', label='Regresi Linear')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    st.pyplot(fig)

    mse = mean_squared_error(y, predictions)
    r2 = r2_score(y, predictions)

    st.subheader("Uji Kebaikan Model:")
    st.write("R-squared (R2): {:.2f}".format(r2))

    st.subheader("Keterangan:")
    st.write("Korelasi antara x dan y adalah sebuah ukuran statistik yang menggambarkan hubungan linier antara kedua variabel. Nilai korelasi berada dalam rentang -1 hingga 1. Jika nilainya mendekati 1, maka hubungan antara x dan y cenderung positif. Jika mendekati -1, maka hubungan cenderung negatif. Jika mendekati 0, maka tidak ada hubungan linier yang jelas antara kedua variabel.")
    st.write("Berdasarkan scatterplot dan persamaan regresi linear sederhana, dapat dilihat bahwa terdapat hubungan positif antara x dan y. Persamaan regresi linear sederhana menggambarkan garis lurus yang mewakili hubungan tersebut, dengan koefisien regresi menunjukkan besarnya perubahan y yang dijelaskan oleh perubahan x. Scatterplot menunjukkan sejauh mana data yang diamati cocok dengan garis regresi linear.")
    st.write("Hasil uji kebaikan model R-squared (R2), memberikan informasi tentang seberapa baik model regresi linear memprediksi data yang diamati. R2 menggambarkan seberapa baik variabilitas data target dijelaskan oleh model.")

if __name__ == '__main__':
    main()
