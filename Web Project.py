import streamlit as st
import numpy as np
import sympy as sp
from sympy import symbols, diff, latex, sympify, simplify
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Kalkulus: Plot & Turunan",
    page_icon="📈",
    layout="wide"
)

# Sidebar navigasi
st.sidebar.title("📌 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Beranda", "📈 Analisis Fungsi"]
)

# ================= HALAMAN BERANDA =================
if menu == "🏠 Beranda":
    st.title("📈 Aplikasi Kalkulus Interaktif")
    st.markdown("""
    Aplikasi ini dibuat untuk membantu memvisualisasikan fungsi matematika,
    menghitung turunan simbolik, dan menampilkan grafik fungsi beserta turunannya.
    
    ### ✨ Fitur:
    - Plot grafik fungsi
    - Hitung turunan simbolik otomatis
    - Tampilkan grafik turunan fungsi
    - Interface interaktif & edukatif
    """)

# ================= HALAMAN ANALISIS =================
elif menu == "📈 Analisis Fungsi":
    st.title("📈 Visualisasi Fungsi & Turunan")

    col1, col2 = st.columns([3, 1])

    with col1:
        input_fungsi = st.text_input(
            "Masukkan Fungsi f(x):",
            value="x**2 + 3*x + 2",
            help="Gunakan variabel x, contoh: x**2, sin(x), exp(x)"
        )

    with col2:
        rentang = st.slider("Rentang X", -20, 20, (-10, 10))

    try:
        x = symbols('x')
        ekspresi_fungsi = sympify(input_fungsi)

        st.markdown("### 🧾 Fungsi dalam Format LaTeX")
        st.latex(f"f(x) = {latex(ekspresi_fungsi)}")

        if st.button("Hitung Turunan"):
            turunan = diff(ekspresi_fungsi, x)
            turunan_sederhana = simplify(turunan)

            st.success("Turunan berhasil dihitung!")
            st.latex(f"\\boxed{{f'(x) = {latex(turunan_sederhana)}}}")

            # Konversi ke fungsi numerik numpy
            f_numeric = sp.lambdify(x, ekspresi_fungsi, "numpy")
            d_numeric = sp.lambdify(x, turunan_sederhana, "numpy")

            xs = np.linspace(rentang[0], rentang[1], 400)
            ys = f_numeric(xs)
            dys = d_numeric(xs)

            colA, colB = st.columns(2)

            # Plot fungsi asli
            with colA:
                st.markdown("### 📊 Grafik Fungsi f(x)")
                fig = plt.figure()
                plt.plot(xs, ys, linewidth=2)
                plt.grid(True)
                st.pyplot(fig)

            # Plot turunan
            with colB:
                st.markdown("### 📉 Grafik Turunan f'(x)")
                fig2 = plt.figure()
                plt.plot(xs, dys, linewidth=2, color="red")
                plt.grid(True)
                st.pyplot(fig2)

    except Exception as e:
        st.error("Terjadi kesalahan, pastikan format fungsi benar.")
        st.write(e)
