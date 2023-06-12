import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats

def calculate_anova(data, alpha):
    k = len(data) 
    n = [len(group) for group in data] 
    N = np.sum(n) 

    grand_mean = np.mean(np.concatenate(data)) 

    ss_within = np.sum([(np.var(group) * (len(group) - 1)) for group in data])
    ss_between = np.sum([(np.mean(group) - grand_mean) ** 2 * len(group) for group in data])

    df_within = N - k
    df_between = k - 1

    ms_within = ss_within / df_within
    ms_between = ss_between / df_between

    f_value = ms_between / ms_within

    f_critical = stats.f.ppf(1 - alpha, df_between, df_within)

    # Keputusan dan kesimpulan
    if f_value > f_critical:
        decision = "Tolak H0"
        conclusion = "Terdapat perbedaan yang signifikan antara setidaknya dua kelompok"
    else:
        decision = "Gagal Tolak H0"
        conclusion = "Tidak terdapat perbedaan yang signifikan antara kelompok-kelompok"

    # Tabel ANOVA
    anova_data = {'Sumber Variasi': ['Between', 'Within'],
                  'DF': [df_between, df_within],
                  'SS': [ss_between, ss_within],
                  'MS': [ms_between, ms_within]}
    df_anova = pd.DataFrame(anova_data)

    return df_anova, df_between, df_within, ss_between, ss_within, ms_between, ms_within, f_value, f_critical, decision, conclusion

def main():
    st.title("Uji ANOVA - Analysis of Variance")
    st.write("Analisis Statistik yang Menguji Perbedaan Rerata Antar Populasi")

    st.sidebar.title("Masukkan Data")
    num_groups = st.sidebar.number_input("Jumlah Kelompok (K)", min_value=2, step=1, value=3)
    alpha = st.sidebar.number_input("Nilai Alpha", min_value=0.01, max_value=0.99, step=0.01, value=0.05)

    data = []
    for i in range(num_groups):
        group_data = st.sidebar.text_input(f"Data Kelompok {i+1} (pisahkan dengan koma)")
        if group_data:
            group_data = np.array(group_data.split(','), dtype=np.float64)
            data.append(group_data)

    if data:
        st.header("Uji ANOVA")
        st.write("Jumlah Kelompok (K):", num_groups)
        st.write("Nilai Alpha:", alpha)

        df_anova, df_between, df_within, ss_between, ss_within, ms_between, ms_within, f_value, f_critical, decision, conclusion = calculate_anova(data, alpha)

        st.subheader("Tabel ANOVA")
        st.dataframe(df_anova)

        st.write("F Hitung:", f_value)
        st.write("F Tabel:", f_critical)

        st.subheader("Keputusan")
        st.write("Keputusan:", decision)
        st.write("Kesimpulan:", conclusion)


if __name__ == '__main__':
    main()
