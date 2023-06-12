import streamlit as st
import numpy as np
import scipy.stats as stats

def main():
    st.title("Uji Homogenitas Varians")
    st.write("Menampilkan Pengujian : Harley - Bartlet - Cochran - Levene Test")

    st.sidebar.title("Masukkan Data")
    num_populations = st.sidebar.number_input("Jumlah Populasi (k)", min_value=2, step=1, value=2)
    alpha = st.sidebar.number_input("Nilai Alpha", min_value=0.01, max_value=0.99, step=0.01, value=0.05)

    data = []
    for i in range(num_populations):
        data_input = st.sidebar.text_input(f"Data Sampel Populasi {i+1} (pisahkan dengan koma)")
        if data_input:
            data.append(np.fromstring(data_input, sep=','))

    if data:
        st.header("Uji Homogenitas Varians")
        st.write("Jumlah Populasi (k):", num_populations)
        st.write("Nilai Alpha:", alpha)

        n = []
        variances = []
        for i, population_data in enumerate(data):
            n_i = len(population_data)
            var_i = np.var(population_data, ddof=1)
            n.append(n_i)
            variances.append(var_i)
            st.write(f"Data Sampel Populasi {i+1}:", population_data)
            st.write(f"Ukuran Sampel Populasi {i+1}:", n_i)
            st.write(f"Varians Populasi {i+1}:", var_i)

        df_between = num_populations - 1
        df_within = np.sum(np.array(n) - 1)

        chi2_harley = ((np.max(variances) / np.min(variances)) - 1) * df_within
        chi2_bartlett = (np.sum((np.array(n) - 1) * np.log(variances)) - df_within * np.log(np.sum(variances) / df_within)) / (1 + (1 / (3 * (num_populations - 1))))
        chi2_cochran = (np.max(variances) * (np.sum(n) - num_populations)) / (np.sum(variances))
        levene_stat, levene_pvalue = stats.levene(*data)

        chi2_critical = stats.chi2.ppf(1 - alpha, df_between)

        st.subheader("Harley Test")
        st.write("Chi-square Value (X hitung): {:.4f}".format(chi2_harley))
        st.write("Chi-square Value (X tabel): {:.4f}".format(chi2_critical))
        if chi2_harley > chi2_critical:
            st.write("Keputusan: Tolak H0")
        else:
            st.write("Keputusan: Gagal Tolak H0")
        st.write("Kesimpulan: Varians tidak homogen") if chi2_harley > chi2_critical else st.write("Kesimpulan: Varians homogen")

        st.subheader("Bartlett Test")
        st.write("Chi-square Value (X hitung): {:.4f}".format(chi2_bartlett))
        st.write("Chi-square Value (X tabel): {:.4f}".format(chi2_critical))
        if chi2_bartlett > chi2_critical:
            st.write("Keputusan: Tolak H0")
        else:
            st.write("Keputusan: Gagal Tolak H0")
        st.write("Kesimpulan: Varians tidak homogen") if chi2_bartlett > chi2_critical else st.write("Kesimpulan: Varians homogen")

        st.subheader("Cochran Test")
        st.write("Chi-square Value (X hitung): {:.4f}".format(chi2_cochran))
        st.write("Chi-square Value (X tabel): {:.4f}".format(chi2_critical))
        if chi2_cochran > chi2_critical:
            st.write("Keputusan: Tolak H0")
        else:
            st.write("Keputusan: Gagal Tolak H0")
        st.write("Kesimpulan: Varians tidak homogen") if chi2_cochran > chi2_critical else st.write("Kesimpulan: Varians homogen")

        st.subheader("Levene Test")
        st.write("Levene Statistic (X hitung): {:.4f}".format(levene_stat))
        st.write("Levene Statistic (X tabel): {:.4f}".format(chi2_critical))
        if levene_stat > chi2_critical:
            st.write("Keputusan: Tolak H0")
        else:
            st.write("Keputusan: Gagal Tolak H0")
        st.write("Kesimpulan: Varians tidak homogen") if levene_stat > chi2_critical else st.write("Kesimpulan: Varians homogen")

if __name__ == '__main__':
    main()
