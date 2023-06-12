import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats


def tukey(data, alpha):
    k = len(data)
    n = [len(group) for group in data]
    N = np.sum(n)

    all_data = np.concatenate(data)
    mean = np.mean(all_data)
    q = stats.t.ppf(1 - alpha / 2, N - k)

    t_critical = q * np.sqrt(np.sum([(np.std(group, ddof=1) ** 2) / len(group) for group in data]))

    pairwise_comparisons = []
    for i in range(k):
        for j in range(i + 1, k):
            mean_diff = np.abs(np.mean(data[i]) - np.mean(data[j]))  # Menggunakan np.abs() untuk nilai mutlak
            se_diff = np.sqrt((np.var(data[i], ddof=1) / len(data[i])) + (np.var(data[j], ddof=1) / len(data[j])))
            t_value = mean_diff / se_diff

            pairwise_comparisons.append({
                'Kelompok 1': f"Kelompok {i + 1}",
                'Kelompok 2': f"Kelompok {j + 1}",
                'Mean Difference': mean_diff,
                'SE Difference': se_diff,
                'T Hitung': t_value,
                'T Tabel': t_critical,
                'Keputusan': 'Tolak' if np.abs(t_value) > t_critical else 'Gagal Tolak'
            })

    df_tukey = pd.DataFrame(pairwise_comparisons)
    return df_tukey


def lsd(data, alpha):
    k = len(data)
    n = [len(group) for group in data]
    N = np.sum(n)

    all_data = np.concatenate(data)
    mean = np.mean(all_data)
    q = stats.t.ppf(1 - alpha / 2, N - k)

    t_critical = q * np.sqrt(np.sum([(np.std(group, ddof=1) ** 2) / len(group) for group in data]))

    pairwise_comparisons = []
    for i in range(k):
        for j in range(i + 1, k):
            mean_diff = np.abs(np.mean(data[i]) - np.mean(data[j]))  # Menggunakan np.abs() untuk nilai mutlak
            se_diff = np.sqrt((np.var(data[i], ddof=1) / len(data[i])) + (np.var(data[j], ddof=1) / len(data[j])))
            t_value = mean_diff / se_diff

            pairwise_comparisons.append({
                'Kelompok 1': f"Kelompok {i + 1}",
                'Kelompok 2': f"Kelompok {j + 1}",
                'Mean Difference': mean_diff,
                'SE Difference': se_diff,
                'T Hitung': t_value,
                'T Tabel': t_critical,
                'Keputusan': 'Tolak' if np.abs(t_value) > t_critical else 'Gagal Tolak'
            })

    df_lsd = pd.DataFrame(pairwise_comparisons)
    return df_lsd


def main():
    st.title("Uji Tukey & LSD")
    st.write("Membandingkan Seluruh Rata-rata Perlakuan Setelah Uji ANOVA Dilakukan")

    st.sidebar.title("Masukkan Data")
    num_groups = st.sidebar.number_input("Jumlah Kelompok (K)", min_value=2, step=1, value=3)
    alpha = st.sidebar.number_input("Nilai Alpha", min_value=0.01, max_value=0.99, step=0.01, value=0.05)

    data = []
    for i in range(num_groups):
        group_data = st.sidebar.text_input(f"Data Kelompok {i + 1} (pisahkan dengan koma)")
        if group_data:
            group_data = np.array(group_data.split(','), dtype=np.float64)
            data.append(group_data)

    if data:
        st.header("Uji Tukey")
        st.write("Jumlah Kelompok (K):", num_groups)
        st.write("Nilai Alpha:", alpha)

        df_tukey = tukey(data, alpha)

        st.subheader("Hasil Uji Tukey")
        st.dataframe(df_tukey)

        st.header("Uji LSD")
        st.write("Jumlah Kelompok (K):", num_groups)
        st.write("Nilai Alpha:", alpha)

        df_lsd = lsd(data, alpha)

        st.subheader("Hasil Uji LSD")
        st.dataframe(df_lsd)


if __name__ == '__main__':
    main()
