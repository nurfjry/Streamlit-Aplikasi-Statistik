import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Karakteristik Data")
    st.write("Menyajikan Mean, Median, Standar Deviasi, Nilai Min dan Maks Serta Visualiasi Histogram")

    st.sidebar.title("Masukkan Data")
    num_populations = st.sidebar.number_input("Jumlah Populasi (k)", min_value=1, step=1, value=3)

    populations = []
    for i in range(num_populations):
        population_data = st.sidebar.text_input(f"Data Populasi {i+1} (pisahkan dengan koma)")
        if population_data:
            population_data = np.array(population_data.split(','), dtype=np.float64)
            populations.append(population_data)

    population_stats = []
    for i, population in enumerate(populations):
        population_stats.append({
            'Populasi': f"Populasi {i + 1}",
            'Mean': np.mean(population),
            'Median': np.median(population),
            'Standar Deviasi': np.std(population),
            'Minimum': np.min(population),
            'Maksimum': np.max(population)
        })

    df_populations = pd.DataFrame(population_stats)

    st.header("Karakteristik Data Populasi")
    st.dataframe(df_populations)

    st.header("Visualisasi")
    for i, population in enumerate(populations):
        st.subheader(f"Populasi {i + 1}")
        plt.hist(population, bins='auto')
        plt.xlabel("Data")
        plt.ylabel("Frekuensi")
        st.pyplot(plt)

    st.header("Keterangan")
    st.write("Karakteristik data menunjukkan statistik deskriptif seperti mean, median, standar deviasi, minimum, dan maksimum dari setiap populasi.")
    st.write("Visualisasi histogram menunjukkan distribusi data untuk setiap populasi.")


if __name__ == '__main__':
    main()
