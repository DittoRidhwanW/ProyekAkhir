import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

f_data = pd.read_csv('D:\Submission\Dashboard\Day.csv')

# Mapping untuk nama musim
season_map = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
f_data['season'] = f_data['season'].map(season_map)

#Konfigurasi Sidebar
st.sidebar.header("Bike Sharing Data Analysis")
year_option = st.sidebar.selectbox("Pilih Tahun", options=['2011', '2012'])
season_option = st.sidebar.multiselect("Pilih Musim", options=['Springer', 'Summer', 'Fall', 'Winter'], default=['Springer', 'Summer', 'Fall', 'Winter'])

st.sidebar.markdown("**Tentang**: Dashboard ini menunjukkan tren penggunaan sepeda berdasarkan tahun dan musim.")

#Tren Pengguna Sepeda per tahun
st.title("Tren Penggunaan Sepeda")
st.subheader(f"Total Penggunaan Sepeda per Tahun ({year_option})")

yearly_data = f_data[f_data['yr'] == int(year_option) - 2011].groupby('yr')['cnt'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_data, x='yr', y='cnt', marker='o')
plt.title(f'Total Penggunaan Sepeda pada Tahun {year_option}')
plt.xlabel('Tahun')
plt.ylabel('Total Pengguna')
plt.xticks([0, 1], ['2011', '2012'])
st.pyplot(plt)

#Rata-rata Pengguna Sepeda per Hari per Musim
st.subheader(f"Rata-rata Pengguna Sepeda per Hari Berdasarkan Musim ({year_option})")

season_avg = f_data[(f_data['yr'] == int(year_option) - 2011) & (f_data['season'].isin(season_option))].groupby('season')['cnt'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=season_avg, x='season', y='cnt')
plt.title(f'Rata-rata Pengguna Sepeda per Hari Berdasarkan Musim ({year_option})')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Pengguna Harian')
st.pyplot(plt)

#Perbandingan Pengguna Casual vs Registered per Musim
st.subheader("Perbandingan Pengguna Casual vs Registered per Musim")

season_users = f_data[(f_data['yr'] == int(year_option) - 2011) & (f_data['season'].isin(season_option))].groupby('season')[['casual', 'registered']].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=season_users.melt(id_vars='season'), x='season', y='value', hue='variable')
plt.title('Perbandingan Pengguna Casual vs Registered per Musim')
plt.xlabel('Musim')
plt.ylabel('Total Pengguna')
plt.legend(title='Tipe Pengguna', loc='upper left')
st.pyplot(plt)
